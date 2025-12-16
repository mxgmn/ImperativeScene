# Copyright (C) 2025 Maxim Gumin, The MIT License (MIT)

from enum import Enum

class ERROR(Enum):
    HALLUCINATION = 0
    PYTHON = 1
    MISUSE = 2
    SUBGRAPH = 3
    LOSS = 4
    WARNING = 5
    FATAL = 6

class Error:
    type: ERROR
    message: str

    legend = { ERROR.HALLUCINATION: "HALLUCINATION", ERROR.PYTHON: "PYTHON", ERROR.MISUSE: "MISUSE", ERROR.SUBGRAPH: "SUBGRAPH", ERROR.LOSS: "LOSS", ERROR.WARNING: "WARNING", ERROR.FATAL: "FATAL" }

    def __init__(self, type: ERROR, message: str):
        self.type = type
        self.message = message

    @staticmethod
    def has(errors: list["Error"], type: ERROR) -> str:
        for e in errors:
            if e.type == type:
                return '1'
        return '0'
