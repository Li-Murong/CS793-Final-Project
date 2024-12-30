from openai import OpenAI
import google.generativeai as genai
from typing import List, Dict
from functools import wraps
import yaml


class Agent:
    def __init__(self, llm):
        self.name = llm
        self.config = self.load_config()
        if llm not in self.config:
            raise ValueError(f"LLM '{llm}' not found in configuration.")
        self.model = self.config[llm]["model"]
        self.api_key = self.config[llm]["api_key"]

    @staticmethod
    def load_config(config_file="config.yaml"):
        with open(config_file, "r") as file:
            return yaml.safe_load(file)

    @staticmethod
    def call_llm(func):
        @wraps(func)
        def wrapper(self, prompt: str):
            try:
                client = func(self)

                response = client.chat.completions.create(
                    model=self.model,  # 替换为你需要使用的模型
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful assistant.",
                        },
                        {"role": "user", "content": prompt},
                    ],
                )
                return response.choices[0].message.content
            except Exception as e:
                print(f"{self.name} call failed: {e}")
                return "Error: Unable to process your request."

        return wrapper

    @call_llm
    def call_openai(self):
        client = OpenAI(api_key=self.api_key)
        return client

    @call_llm
    def call_llama(self):
        client = OpenAI(
            api_key=self.api_key,
            base_url="https://api.llama-api.com",
        )
        return client

    def get_answer(self, prompt: str):
        if self.name == "openai":
            return self.call_openai(prompt)
        elif self.name == "llama":
            return self.call_llama(prompt)
        else:
            raise ValueError(f"Invalid LLM: {self.name}")


class Judger:
    def __init__(self):
        self.name = "gemini"
        self.config = self.load_config()
        self.model = self.config[self.name]["model"]
        self.api_key = self.config[self.name]["api_key"]

    @staticmethod
    def load_config(config_file="config.yaml"):
        with open(config_file, "r") as file:
            return yaml.safe_load(file)

    def get_best_response(self, QAs: Dict):
        analysis_prompt = f"question: {QAs['question']}. response 1:{QAs['openai']} response 2:{QAs['llama']}.Which response is more informative to the quesion? Directly output the better response."

        genai.configure(api_key=self.api_key)
        model = genai.GenerativeModel(self.model)
        response = model.generate_content(analysis_prompt)
        return response.text

