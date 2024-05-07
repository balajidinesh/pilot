import time

from llava_logs import *


def choose_to_rerun():
    print("what would you like to rerun? :")
    print(''.join([f"{i + 1}. {x["log_objective"]} \n" for i, x in enumerate(operation_list)]))

    choice = int(input("Enter your Number of choice: "))

    if choice in range(1, len(operation_list) + 1):
        return choice - 1
    else:
        return None


def run():
    index = choose_to_rerun()

    if index is None:
        return

    log_dict = operation_list[index]

    operations = log_dict['operations']

    operate_logs(operations)


def operate_logs(operations):
    for operation in operations:
        # wait one second
        time.sleep(1)
        operate_type = operation.get("operation").lower()
        # operate_thought = operation.get("thought")

        operate_detail = ""

        if operate_type == "press" or operate_type == "hotkey":
            keys = operation.get("data")
            operate_detail = keys
            current_system.press_keys(keys)
        elif operate_type == "write":
            content = operation.get("data")
            operate_detail = content
            current_system.write(content)
        elif operate_type == "click":
            cords = operation.get("data")
            x = cords.get("x")
            y = cords.get("y")
            click_detail = {"action": "click", "x": x, "y": y}
            operate_detail = click_detail
            current_system.mouse_actions(click_detail)
        elif operate_type == "done":
            summary = operation.get("data")
            return True
        else:
            print("failed unrecognised output")
            return False

    return False


if __name__ == "__main__":
    run()