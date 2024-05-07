from makePrompt import ModelPrompt
from ollama_host import CLIENT2
from operating_system import OperatingSystem

current_system = OperatingSystem()
current_prompt_head = ModelPrompt(objective='', software='', client=CLIENT2)


def make_op(
        operation, datas
):
    return {
        "operation": operation,
        "data": datas
    }


operation_list = [
    {
        "log_objective": "open google chrome",
        "operations": [
            make_op('press', current_prompt_head.os_search_str),
            make_op("write", "Google Chrome"),
            make_op("press", ["enter"]),
            make_op("press", ["ctrl", 'l']),
            make_op("write", ["Biryani"]),
            make_op("press", ["enter"]),
            make_op("done", "process completed")
        ],
        "safety": "safe"
    }
]
