import asyncio
import time

from prompt_toolkit import prompt

from config import Config
from defaults import get_system_prompt
from makePrompt import ModelPrompt
from operating_system import OperatingSystem

current_system = OperatingSystem()
current_config = Config()


def operate_with_args(
        api, verbose_mode
):
    current_system.verbose = verbose_mode

    print("[USER]")
    software = prompt('Enter the name of the software you would like to operate: ')
    print("[USER]")
    objective = prompt('Enter the objective or task you need help with : ')

    model_prompt = ModelPrompt(objective=objective, software=software)

    system_prompt = model_prompt.get_prompt()

    system_message = {"role": "system", "content": system_prompt}
    model_prompt.messages.append(system_message)

    loop_count = 0
    session_id = None

    while True:
        print("[Self Operating Computer] loop_count", loop_count)

        try:
            operations, session_id = asyncio.run(
                model_prompt.call_ollama_llava()
            )

            stop = operate(operations)
            if stop:
                break

            loop_count += 1
            if loop_count > 10:
                break
        except Exception as e:
            print(f"[Operate with args] Loop[] ", e)
            break


def operate(operations):
    for operation in operations:
        # wait one second
        time.sleep(1)
        operate_type = operation.get("operation").lower()
        operate_thought = operation.get("thought")

        operate_detail = ""

        if operate_type == "press" or operate_type == "hotkey":
            keys = operation.get("keys")
            operate_detail = keys
            current_system.press(keys)
        elif operate_type == "write":
            content = operation.get("content")
            operate_detail = content
            current_system.write(content)
        elif operate_type == "click":
            x = operation.get("x")
            y = operation.get("y")
            click_detail = {"x": x, "y": y}
            operate_detail = click_detail
            current_system.mouse(click_detail)
        elif operate_type == "done":
            summary = operation.get("summary")
            return True
        else:
            print("failed unrecognised output")
            return False

    return False
