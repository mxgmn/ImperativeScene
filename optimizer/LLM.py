# Copyright (C) 2025 Maxim Gumin, The MIT License (MIT)

from enum import Enum
import json
import time
import requests
from openai import OpenAI
import anthropic
from groq import Groq

from .Settings import Settings
from .logger import info
from .keys import OPENAI_KEY, ANTHROPIC_KEY, GEMINI_KEY, LLAMA_KEY


class SERVICE(Enum):
    GPT = 0
    CLAUDE = 1
    GEMINI = 2
    LLAMA = 3


class LLM:
    model: str
    service: SERVICE
    system: str
    messages: list[dict[str, str]]
    average_time: float
    queries_so_far: int

    def __init__(self, model: str, dialog: list[str]):
        info(f"CREATING A {model} LLM AGENT WITH {len(dialog)} MESSAGES")
        #for i, s in enumerate(dialog):
        #    info(f"{i}. {s}\n")
        self.model = model
        self.system = dialog[0]
        if model[0:3] == "gpt" or model[0:2] == "o1" or model[0:2] == "Ch":
            self.service = SERVICE.GPT
        elif model[0:6] == "claude":
            self.service = SERVICE.CLAUDE
        elif model[0:6] == "gemini":
            self.service = SERVICE.GEMINI
            #genai.configure(api_key=GEMINI_KEY)
            #self.gemini_model = genai.GenerativeModel(model_name=model, system_instruction=dialog[0])
            self.openai_client = OpenAI(api_key=GEMINI_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
        elif model[0:5] == "llama":
            self.service = SERVICE.LLAMA
            self.groq_client = Groq(api_key=LLAMA_KEY)
        else:
            raise Exception(f"unknown llm {model}")

        if self.service == SERVICE.GPT or self.service == SERVICE.GEMINI or self.service == SERVICE.LLAMA:
            self.messages = [{"role": "system", "content": self.system}]
        else:
            self.messages = []
            self.client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
        for i in range(1, len(dialog)):
            self.messages.append({"role": "user" if i % 2 == 1 else "assistant", "content": dialog[i]})
        self.average_time = 0.0
        self.queries_so_far = 0


    def run(self, query: str) -> str:
        info(f'Awaiting {Settings.MODEL} response for "{query.splitlines()[0]}" ...')
        start_time = time.time()
        if self.service == SERVICE.GPT:
            url = "https://api.openai.com/v1/chat/completions" if self.service == SERVICE.GPT else "https://generativelanguage.googleapis.com/v1beta/openai/"
            key = OPENAI_KEY if self.service == SERVICE.GPT else GEMINI_KEY
            question_dict = {
                "model": Settings.MODEL,
                "temperature": 0,
                "messages": self.messages + [{"role": "user", "content": query}],
            }
            response = requests.post(
                url,
                data=json.dumps(question_dict),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {key}",
                },
            )
            answer_dict = response.json()
            info(answer_dict)
            answer = answer_dict["choices"][0]["message"]["content"]
        elif self.service == SERVICE.LLAMA:
            chat_completion = self.groq_client.chat.completions.create(
                messages=self.messages + [{"role": "user", "content": query}],
                model=Settings.MODEL,
                temperature=0.0,
            )
            info(chat_completion)
            answer = chat_completion.choices[0].message.content
            """
            question_dict = {
                "model": Settings.MODEL,
                "temperature": 0,
                "messages": self.messages + [{"role": "user", "content": query}],
            }
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                data=json.dumps(question_dict),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {LLAMA_KEY}",
                },
            )
            print("Status Code:", response.status_code)
            print("Response Text:", response.text)
            answer_dict = response.json()
            info(answer_dict)
            answer = answer_dict["choices"][0]["message"]["content"]
            """
        elif self.service == SERVICE.GEMINI:
            final_messages = self.messages + [{"role": "user", "content": query}]
            response = self.openai_client.chat.completions.create(
                model=Settings.MODEL,
                n=1,
                max_tokens=3000,
                temperature=0.0,
                messages=final_messages
            )
            answer = response.choices[0].message.content
            #answer = self.gemini_model.generate_content("Write a story about a magic backpack.")
            #print(answer)
        elif self.service == SERVICE.CLAUDE:
            final_messages = self.messages + [{"role": "user", "content": query}]
            message = self.client.messages.create(
                model=Settings.MODEL,
                max_tokens=3000,
                temperature=0.0,
                system=self.system,
                messages=final_messages,
            )
            answer = message.content[0].text
        else:
            raise Exception(f"unknown service {self.service}")

        time_spent = time.time() - start_time
        self.average_time = (self.average_time * self.queries_so_far + time_spent) / (self.queries_so_far + 1.0)
        self.queries_so_far += 1
        info(f"{Settings.MODEL} took {int(time_spent)} seconds to respond, average time = {self.average_time:.1f} in {self.queries_so_far} queries")
        return str(answer)
