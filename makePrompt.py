import asyncio
import json
import os
import time

from defaults import OPERATE_PROMPT, OPERATE_FIRST_MESSAGE_PROMPT, get_system_prompt
from ollama_host import MODEL, model_from_llava
from operating_system import OperatingSystem


def get_user_prompt():
    prompt = OPERATE_PROMPT
    return prompt


def get_user_first_message_prompt():
    prompt = OPERATE_FIRST_MESSAGE_PROMPT
    return prompt


def make_ss_dir():
    cwd = os.getcwd()
    ss_dir = "ss_dir"
    if not os.path.exists(os.path.join(cwd, ss_dir)):
        os.makedirs(os.path.join(cwd, ss_dir))
        print(f"Created directory: {ss_dir}")
    else:
        print(f"Directory already exists: {ss_dir}")

    return os.path.join(cwd, ss_dir)


def return_os_keys():
    os_object = OperatingSystem()
    if os_object.os_name == "Darwin":
        cmd_string = "command"
        os_search_str = ["command", "space"]
        # operating_system = "Mac"
    elif os_object.os_name == "Windows":
        cmd_string = "ctrl"
        os_search_str = ["win"]
        # operating_system = "Windows"
    else:
        cmd_string = "ctrl"
        os_search_str = ["win"]
        # operating_system = "Linux"

    return cmd_string, os_search_str, os_object


def clean_json(content):
    if content.startswith("```json"):
        content = content[
                  len("```json"):
                  ].strip()  # Remove starting ```json and trim whitespace
    elif content.startswith("```"):
        content = content[
                  len("```"):
                  ].strip()  # Remove starting ``` and trim whitespace
    if content.endswith("```"):
        content = content[
                  : -len("```")
                  ].strip()  # Remove ending ``` and trim whitespace

    # Normalize line breaks and remove any unwanted characters
    content = "\n".join(line.strip() for line in content.splitlines())

    return content


class ModelPrompt:

    def __init__(self, objective, software, client):
        self.cmd_string, self.os_search_str, self.operating_system = return_os_keys()
        self.model = MODEL
        self.messages = []
        self.objective = objective
        self.software = software
        self.client = client

    def get_prompt(self):
        prompt = get_system_prompt(
            software=self.software,
            objective=self.objective,
            cmd_string=self.cmd_string,
            os_search_str=self.os_search_str,
            operating_system=self.operating_system.os_name,
        )
        return prompt

    async def call_ollama_llava(self):

        screenshots_dir = make_ss_dir()
        time.sleep(1)

        try:
            screenshot_filename = os.path.join(screenshots_dir, "screenshot.png")

            self.operating_system.screenshot(screenshot_filename)

            if len(self.messages) == 1:
                user_prompt = get_user_first_message_prompt()
            elif len(self.messages) == 0:
                return
            else:
                user_prompt = get_user_prompt()

            print("user prompt created")

            vision_message = {
                "role": "user",
                "content": user_prompt,
                "images": [screenshot_filename],
            }

            self.messages.append(vision_message)

            with open(os.path.join(screenshots_dir, "screenshot.txt"),"w") as f :
                f.write('\n'.join(str(i) for i in self.messages))

            response = await self.client.chat(
                model=MODEL,
                messages=self.messages,
            )

            # Important: Remove the image path from the message history.
            # Ollama will attempt to load each image reference and will
            # eventually time out.

            self.messages[-1]["images"] = None

            content = response["message"]["content"].strip()
            content = clean_json(content)

            assistant_message = {"role": "assistant", "content": content}
            content = json.loads(content)

            self.messages.append(assistant_message)
            return content

        except Exception as e:
            print("[makePrompt][ollama call]:", e)
