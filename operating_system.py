import subprocess
import sys
import os
import time
import asyncio
import platform
import Xlib
import pyautogui


class OperatingSystem:
    def __init__(self):
        self.os_name = platform.system()

    def screenshot(self, path):
        if self.os_name == 'Windows':
            screenshot = pyautogui.screenshot()
            screenshot.save(path)
        # if self.os_name == 'Linux':
        #     screen = Xlib.display.Display().screen()
        #     size = screen.width_in_pixels, screen.height_in_pixels
        #     screenshot = pyautogui.screenshot()
        if self.os_name == 'Darwin':
            subprocess.run(['screencapture', "-C", path])

    def write(self, content: str):
        try:
            content = content.replace("\\n", "\n")
            for char in content:
                pyautogui.write(char)
            return True
        except Exception as e:
            print(f"[Class OperatingSystem][{self.os_name}]Exception while writing to file", e)
            return False

    def press_keys(self, keys):
        try:
            for key in keys:
                pyautogui.keyDown(key)
            time.sleep(0.1)
            for key in reversed(keys):
                pyautogui.keyUp(key)
        except Exception as e:
            print(f"[Class OperatingSystem][{self.os_name}]Exception while pressing keys", e)

    # todo make key hold and up a wrapper would be better
    def key_hold_release(self, key, release=True):
        try:
            if release:
                pyautogui.keyUp(key)
            else:
                pyautogui.keyDown(key)
            time.sleep(0.1)
        except Exception as e:
            print(f"[Class OperatingSystem][{self.os_name}]Exception while pressing keys", e)

    def mouse_actions(self, click_detail, with_key_hold, press_after_mouse):
        # todo make sure both with_key_hold, press_after_mouse never come at once
        try:
            happened = True
            action = click_detail.get("action")
            if action == "left_click":
                pyautogui.click()
            elif action == "right_click":
                pyautogui.rightClick()
            elif action == "double_click":
                pyautogui.doubleClick()
            elif action == "scroll":
                pyautogui.scroll(click_detail.get("amount"))
            elif action == "mouse_drag":
                side = click_detail.get("side")
                hold = with_key_hold
                if hold:
                    with_key_hold(hold, release=False)
                x_vector, y_vector = click_detail.get("vector")
                pyautogui.mouseDown(button=side)
                pyautogui.moveRel(x_vector, y_vector, duration=0.5)
                pyautogui.mouseUp(button=side)
                if hold:
                    with_key_hold(hold)
            else:
                happened = False
            return happened
        except Exception as e:
            print(f"[OperatingSystem][{self.os_name}][mouse] error:", e)
            return False

    def go_to_and_confirm(self):
        pass
