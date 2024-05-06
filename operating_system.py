import math
import subprocess
import sys
import os
import time
import asyncio
import platform
import Xlib
import pyautogui

from misc import convert_percent_to_decimal


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

    def mouse_actions(self, click_detail, with_key_hold=False, press_after_mouse=False):
        # todo make sure both with_key_hold, press_after_mouse never come at once

        try:
            happened = True
            x = convert_percent_to_decimal(click_detail.get("x"))
            y = convert_percent_to_decimal(click_detail.get("y"))
            action = click_detail.get("action")

            is_move = False
            if isinstance(x, float) and isinstance(y, float):
                self.go_to_location(x_percentage=x, y_percentage=y)

            if action == "left_click" or action == "click":
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
                    self.key_hold_release(hold, release=False)
                x_vector, y_vector = click_detail.get("vector")
                pyautogui.mouseDown(button=side)
                pyautogui.moveRel(x_vector, y_vector, duration=0.5)
                pyautogui.mouseUp(button=side)
                if hold:
                    self.key_hold_release(hold)
            else:
                happened = False
            return happened
        except Exception as e:
            print(f"[OperatingSystem][{self.os_name}][mouse] error:", e)
            return False

    def go_to_location(
            self,
            x_percentage,
            y_percentage,
            duration=0.2,
            circle_radius=50,
            circle_duration=0.5,
    ):
        try:
            screen_width, screen_height = pyautogui.size()
            x_pixel = int(screen_width * float(x_percentage))
            y_pixel = int(screen_height * float(y_percentage))

            pyautogui.moveTo(x_pixel, y_pixel, duration=duration)

            start_time = time.time()
            while time.time() - start_time < circle_duration:
                angle = ((time.time() - start_time) / circle_duration) * 2 * math.pi
                x = x_pixel + math.cos(angle) * circle_radius
                y = y_pixel + math.sin(angle) * circle_radius
                pyautogui.moveTo(x, y, duration=0.1)

            pyautogui.moveTo(x_pixel, y_pixel)
            # pyautogui.click(x_pixel, y_pixel)
        except Exception as e:
            print(f"[OperatingSystem][{self.os_name}][mouse] error:", e)
            return False

    def go_to_and_confirm(self):
        pass
