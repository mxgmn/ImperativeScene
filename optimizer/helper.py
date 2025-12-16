# Copyright (C) 2025 Maxim Gumin, The MIT License (MIT)

import ast
import astor
import re
import os
import random

direction_names = ["EAST", "NORTH", "WEST", "SOUTH"] # эти имена только для жсона
hopposite = [2, 3, 0, 1]

def whole_folder(bigfolder: str, folder: str) -> list[str]:
    #return [f"{folder}/{os.path.basename(item[0:-3])}" for item in os.listdir(folder) if os.path.isfile(f"{folder}/{item}")]
    fullpath = os.path.join(bigfolder, folder)
    return [f"{folder}/{item[0:-3]}" for item in os.listdir(fullpath) if os.path.isfile(os.path.join(fullpath, item))]

def comma(i: int, objects) -> str:
    return ',' if i < len(objects) - 1 else ''

def delete_all_files(folder: str):
    os.makedirs(folder, exist_ok=True)
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            os.unlink(file_path)

#def remove_nth_line(s, n) -> str:
#    lines = s.splitlines()
#    del lines[n]
#    return '\n'.join(lines)

def remove_trailing_numbers(s: str) -> str:
    return re.sub(r"\s+\d+$", "", s)

def myhash(s: str) -> int:
    seed = 0
    for i, c in enumerate(s):
        seed += (i + 1) * ord(c)
    return seed


def wrap_constants(s: str) -> tuple[str, list[float]]:
    def find_matching_paren(s, start_pos):
        count = 1
        for i in range(start_pos + 1, len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
                if count == 0:
                    return i
        return -1  # No matching closing parenthesis found

    excluded_functions = ['Object', 'set_size', 'Door', 'Window']
    excluded_ranges = []

    # 1) Exclude function calls for the listed functions
    for func_name in excluded_functions:
        pattern_func = re.compile(r'\b' + re.escape(func_name) + r'\s*\(')
        for match in pattern_func.finditer(s):
            start = match.start()
            paren_pos = s.find('(', match.end() - 1)
            end = find_matching_paren(s, paren_pos)
            if end != -1:
                excluded_ranges.append((start, end + 1))

    # 2) Exclude lines that contain "Object" (Not just function calls, but any line with "Object")
    def find_lines_with_object(s):
        object_line_ranges = []
        lines = s.split('\n')
        pos = 0
        for line in lines:
            if 'Object' in line:
                start = pos
                end = pos + len(line)
                object_line_ranges.append((start, end))
            pos += len(line) + 1
        return object_line_ranges

    object_ranges = find_lines_with_object(s)
    excluded_ranges.extend(object_ranges)

    # 3) Exclude comment ranges (lines that begin with "#")
    def find_comments(s):
        comment_ranges = []
        lines = s.split('\n')
        pos = 0
        for line in lines:
            stripped_line = line.lstrip()
            if stripped_line.startswith('#'):
                start = pos + line.find('#')
                end = pos + len(line)
                comment_ranges.append((start, end))
            pos += len(line) + 1
        return comment_ranges

    comment_ranges = find_comments(s)
    excluded_ranges.extend(comment_ranges)

    # Sort all excluded ranges
    excluded_ranges.sort()

    # 4) Wrap numeric constants outside excluded ranges
    parts = []
    last_pos = 0
    index = 0
    values = []

    pattern = re.compile(r'\b(?!3\.14)\d+\.\d+\b')
    for match in pattern.finditer(s):
        num_start, num_end = match.start(), match.end()
        inside_excluded = False
        for ex_start, ex_end in excluded_ranges:
            if ex_start <= num_start < ex_end:
                inside_excluded = True
                break

        parts.append(s[last_pos:num_start])

        if inside_excluded:
            parts.append(s[num_start:num_end])  # Keep as-is
        else:
            value = match.group()
            parts.append(f'number({index}, {value})')
            values.append(float(value))
            index += 1

        last_pos = num_end

    # Append whatever is left
    parts.append(s[last_pos:])
    new_s = ''.join(parts)
    return new_s, values


#def add_index_to_constructors(code: str) -> tuple[str, int]:
#    pattern = r'\b(Object|Door|Window)\('
#    counter = 0
#    def replace_constructor(match):
#        nonlocal counter
#        replacement = f"{match.group(0)}{counter}, "
#        counter += 1
#        return replacement
#    return re.sub(pattern, replace_constructor, code), counter


def remove_comments(code: str) -> str:
    code_no_single = re.sub(r'#.*', '', code)
    code_no_comments = re.sub(r'(""".*?"""|\'\'\'.*?\'\'\')', '', code_no_single, flags=re.DOTALL)
    return code_no_comments

def remove_markdown(code_str: str) -> str:
    stripped = code_str.strip()
    if stripped.startswith("```") and stripped.endswith("```"):
        lines = stripped.splitlines()
        return "\n".join(lines[1:-1]).rstrip()
    return code_str
def remove_imports(s: str) -> str:
    return "\n".join(line for line in s.splitlines() if not line.lstrip().startswith("import"))

def lerp(a: list[float], b: list[float], t: float) -> list[float]:
    return [(1.0 - t) * ai + t * bi for ai, bi in zip(a, b)]

#def boolean_vectors(n) -> list[list[int]]:
#    return [list(vec) for vec in product([0, 1, 2, 3], repeat=n)]

#def all_combinations(list_of_lists: list[list[int]]):
#    return [list(combination) for combination in product(*list_of_lists)]

def intersect(l1: list[int], l2: list[int]) -> bool:
    for i in range(len(l1)):
        if l1[i] and l2[i]:
            return True
    return False

def merge(vec: list[float]) -> tuple[list[int], list[float]]:
    prev_constant = vec[0] + 1.0 if len(vec) > 0 else -1.11
    values = []
    mapping = []
    distinct_so_far = -1
    for i in range(len(vec)):
        if vec[i] == 0:
            mapping.append(-1)
        else:
            if vec[i] != prev_constant:
                values.append(vec[i])
                distinct_so_far += 1
            mapping.append(distinct_so_far)
            prev_constant = vec[i]
    return mapping, values


class SafeListAccessTransformer(ast.NodeTransformer):
    def visit_Subscript(self, node):
        self.generic_visit(node) # Recursively transform child nodes first
        # Handle any index expression that isn't a slice
        if not isinstance(node.slice, ast.Slice):
            # Create len() call for the sequence
            len_call = ast.Call(
                func=ast.Name(id='len', ctx=ast.Load()),
                args=[node.value],
                keywords=[]
            )
            # Create modulo operation: (complex_expression) % len(sequence)
            safe_index = ast.BinOp(
                left=node.slice,
                op=ast.Mod(),
                right=len_call
            )
            # Replace the original index with our safe version
            node.slice = safe_index
            # Add parentheses for clarity
            node.slice = ast.parse(f'({astor.to_source(node.slice).strip()})').body[0].value
        return node

def make_list_access_safe(s: str) -> str:
    tree = ast.parse(s)
    # тут неплохо бы вернуть ошибку, если строка не является питоном
    transformer = SafeListAccessTransformer()
    transformed_tree = transformer.visit(tree)
    transformed_code = astor.to_source(transformed_tree, pretty_source=lambda x: "".join(x))
    return transformed_code

def ast_to_lisp(node: ast.AST | list | str | int | float | None) -> str:
    if isinstance(node, ast.AST):
        fields = [f"({key} {ast_to_lisp(value)})" for key, value in ast.iter_fields(node)]
        return f"({node.__class__.__name__} {' '.join(fields)})"
    elif isinstance(node, list):
        return f"[{' '.join(ast_to_lisp(item) for item in node)}]"
    elif isinstance(node, (str, int, float, type(None))):
        return repr(node)
    else:
        raise TypeError(f"Unsupported type: {type(node)}")

def to_lisp(source_code: str) -> str:
    return ast_to_lisp(ast.parse(source_code))

def random_list(length: int, MAX: int, rng: random.Random) -> list[int]:
    if length == 1:
        return [0]
    elif length <= MAX:
        return rng.sample(range(MAX), length)
    else:
        result = list(range(MAX))
        result.extend(rng.choices(range(MAX), k=length - MAX))
        rng.shuffle(result)
        return result
