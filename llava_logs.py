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
            make_op("wait", {"message": "waiting for rhino to open and Maximize the window", "time": 50}),
            # wait for rhino to open
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
        "safety_level": 0
    },
    {
        "log_objective": "create two polygons and loft them in rhino",
        "operations": [
            make_op("wait", {"message": "Focus on rhino Window and wait", "time": 30}),
            # wait for rhino to open give time for the user to set up rhino
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
            make_op("wait", {"message": "Focus on rhino Window and wait", "time": 5}),
            # make_op("write", "_MaxViewport"),  # Maximize viewport
            # make_op("press", ["enter"]),
            make_op("write", "InterpCrv"),
            make_op("press", ["enter"]),
            make_op("mouse", mouse_mapper(index=0, x=0.38, y=0.44)),
            make_op("mouse", mouse_mapper(index=0, x=0.44, y=0.6)),
            make_op("mouse", mouse_mapper(index=0, x=0.42, y=0.78)),
            make_op("mouse", mouse_mapper(index=0, x=0.484, y=0.79 + 0.07)),
            make_op("mouse", mouse_mapper(index=0, x=0.484+0.06, y=0.79-0.07)),
            make_op("mouse", mouse_mapper(index=0, x=0.46+0.06, y=0.565)),
            make_op("mouse", mouse_mapper(index=0, x=0.49+0.04, y=0.41)),
            make_op("mouse", mouse_mapper(index=0, x=0.41+0.03, y=0.342-0.07)),
            make_op("write", "P"),  # persistent close
            make_op("press", ["enter"]),
            make_op("press", ["enter"]),
            make_op("write", "InterpCrv"),
            make_op("press", ["enter"]),
            make_op("write", "P"),  # persistent close reset
            make_op("press", ["enter"]),
            make_op("press",["esc"]),
            make_op("done", "Created shoe sole shape and closed spline in Rhino")  # Objective completed
        ],
        "safety_level": 0
    },
    {
        "log_objective": "Make a Surface of the closed curve Rhino",
        "operations": [
            make_op("wait", {"message": "Please Select the Curve You want to Surface", "time": 20}),
            make_op("write", "_PlanarSrf"),  # Use command to extrude curves
            make_op("press", ["enter"]),
            make_op("done", "Made Surface in Rhino")  # Objective completed
        ],
        "safety_level": 0
    },
    {
        "log_objective": "Help me Extrude Surface at 10 units in normal direction",
        "operations": [
            make_op("wait", {"message": "Please Select the Surface You want to Extrude", "time": 20}),
            make_op("write", "_ExtrudeSrf"),  # Use command to extrude curves
            make_op("press", ["enter"]),
            make_op("write", "10"),  # Use command to extrude curves
            make_op("press", ["enter"]),
            make_op("done", "Extruded Surfaces in Rhino")  # Objective completed
        ],
        "safety_level": 0
    },
    {
        "log_objective": "Help me scale down a sole lower curve by 0.7 units",
        "operations": [
            make_op("wait", {"message": "Please Select the Surface You want to Scale Down", "time": 20}),
            make_op("write", "_Scale2D"),  # Use command to extrude curves
            make_op("press", ["enter"]),
            make_op("press", ["0"]),
            make_op("press", ["enter"]),
            make_op("write", "0.8"),  # Use command to extrude curves
            make_op("press", ["enter"]),
            make_op("done", "Scaled in Rhino")  # Objective completed
        ],
        "safety_level": 2
    }
]
