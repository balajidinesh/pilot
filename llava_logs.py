from makePrompt import ModelPrompt
from ollama_host import CLIENT2
from operating_system import OperatingSystem

current_system = OperatingSystem()
current_prompt_head = ModelPrompt(objective='', software='', client=CLIENT2)

mouse_actions = ["left_click", "right_click", "double_click", "scroll", "mouse_drag"]
safety_levels = ["safe", "moderate", "danger", "extremely_dangerous_commands"]


def make_op(
        operation, datas
):
    return {
        "operation": operation,
        "data": datas
    }


def mouse_mapper(index, x=None, y=None, vector=None, amount=None, side=0, hold=False):
    action = mouse_actions[index]
    data = {"action": action, "x": x, "y": y, "vector": vector, "amount": amount}

    side_ar = ['left', 'middle', 'right']

    if action == "scroll":
        data["amount"] = amount
    elif action == "mouse_drag":
        data["side"] = side_ar[side]
        data["vector"] = vector
        data["hold"] = hold
    else:
        # Assuming no other parameters needed for simple mouse actions
        pass
    return data


operation_list = [
    {
        "log_objective": "open google chrome",
        "operations": [
            make_op('press', current_prompt_head.os_search_str),
            make_op("write", "Google Chrome"),
            make_op("press", ["enter"]),
            make_op("press", [current_prompt_head.cmd_string, 'l']),
            make_op("write", "Biryani"),
            make_op("press", ["enter"]),
            make_op("done", "process completed")
        ],
        "safety_level": 0
    },
    {
        "log_objective": "open rhino and create a polygon",
        "operations": [
            make_op('press', ["win"]),  # Open search bar
            make_op("write", "Rhino"),  # Search for Rhino
            make_op("press", ["enter"]),  # Launch Rhino
            make_op("wait", 30),  # wait for rhino to open
            # make_op("press", ["win", "up"]),  # Maximize Rhino window (assuming "win" + "up" is the shortcut)
            make_op("write", "_MaxViewport"),  # Maximize perspective
            make_op("press", ["enter"]),
            make_op("write", "Polygon"),  # Use command to create a polygon
            make_op("press", ["enter"]),
            make_op("write", "N"),  # to change the num of sides default is 3
            make_op("press", ["enter"]),
            make_op("write", "5"),
            make_op("press", ["enter"]),
            make_op("write", "0"),  # to make the origin as center of polygon
            make_op("press", ["enter"]),
            make_op("write", "0,10,10"),  # to make one of the vertices at the that point
            make_op("press", ["enter"]),
            make_op("done", "Opened Rhino and created a polygon with 5 edges")  # Objective completed
        ],
        "safety_level": 1
    },
    {
        "log_objective": "create two polygons and loft them in rhino",
        "operations": [
            make_op("wait", 30),  # wait for rhino to open give time for the user to set up rhino
            make_op("write", "_MaxViewport"),  # Maximize perspective
            make_op("press", ["enter"]),
            make_op("write", "Polygon"),  # Use command to create a polygon
            make_op("press", ["enter"]),
            make_op("write", "N"),  # to change the num of sides default is 3
            make_op("press", ["enter"]),
            make_op("write", "5"),
            make_op("press", ["enter"]),
            make_op("write", "0"),  # to make the origin as center of polygon
            make_op("press", ["enter"]),
            make_op("write", "0,10,10"),  # to make one of the vertices at the that point
            make_op("press", ["enter"]),
            make_op("write", "Polygon"),  # Create another polygon
            make_op("press", ["enter"]),
            make_op("write", "N"),  # Change number of sides
            make_op("press", ["enter"]),
            make_op("write", "5"),
            make_op("press", ["enter"]),
            make_op("write", "0"),  # Center at origin
            make_op("press", ["enter"]),
            make_op("write", "0,-10,10"),  # Place at a different point
            make_op("press", ["enter"]),
            make_op("write", "_Loft"),  # Loft command
            make_op("press", ["enter"]),
            make_op("done", "Created two polygons and lofted them in Rhino")  # Objective completed
        ],
        "safety_level": 1
    },
    {
        "log_objective": "Create a shoe sole shape in 2D using points and then make a closed spline",
        "operations": [
            make_op("wait", 30),  # Wait for Rhino to open, giving time for setup
            make_op("write", "_MaxViewport"),  # Maximize viewport
            make_op("press", ["enter"]),
            make_op("done", "Opened Rhino and maximized viewport"),
            make_op("wait", 10),  # Wait for user to position cursor
            make_op("mouse", mouse_mapper(index=0, x=0.5, y=0.5)),  # Move mouse to center of viewport
            make_op("wait", 5),  # Wait for cursor movement
            make_op("mouse", mouse_mapper(index=0, hold=True, side=0)),  # Hold left click to create points
            make_op("wait", 5),  # Wait for points to be created
            make_op("mouse", mouse_mapper(index=0, x=0.5, y=0.8)),  # Move mouse to select all points
            make_op("wait", 5),  # Wait for cursor movement
            make_op("mouse", mouse_mapper(index=1)),  # Right click to select all points
            make_op("wait", 5),  # Wait for context menu to appear
            make_op("write", "_Spline"),  # Create spline from selected points
            make_op("press", ["enter"]),
            make_op("write", "C"),  # Close the spline
            make_op("press", ["enter"]),
            make_op("done", "Created shoe sole shape and closed spline in Rhino")  # Objective completed
        ],
        "safety_level": 1
    }
]
