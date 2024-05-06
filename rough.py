import os

import pyautogui
import time

from makePrompt import make_ss_dir

t = os.path.join(make_ss_dir(), "screenshot.png")
screenshot = pyautogui.screenshot()
screenshot.save(t)