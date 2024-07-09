import pyautogui
import pygetwindow 
import cv2
import numpy as np
import pyautogui
from PIL import Image


def windowf(title, action="activate"):
    try:
        win = pygetwindow.getWindowsWithTitle(title)[0]
        if action == "activate":
            win.activate()
        elif action == "minimize":
            win.minimize()
        elif action == "maximize":
            win.maximize()
    except IndexError:
        raise pygetwindow.PyGetWindowException(f"Window with title '{title}' not found.")
    except pygetwindow.PyGetWindowException as e:
        raise e  # Re-raise any other PyGetWindowException

    return

def is_window_existent(window_title=None):
  try:
    if window_title is None:
      # Check if any window is found (foreground window)
      return bool(pygetwindow.getAllWindows())
    else:
      # Find windows with the specified title (case-sensitive)
      windows_with_title = pygetwindow.getWindowsWithTitle(window_title)
      return len(windows_with_title) > 0  # Check if any match is found

  except Exception as e:
    # Handle potential errors (e.g., library issues)
    print(f"Error checking window existence: {e}")
    return False  # Assume non-existence on error

def mousefunc(x, y, action, button="left", clicks=1, click_type="normal"):
    # Validate action, button, clicks, and click_type arguments
    valid_actions = ["click", "move", "moveandclick", "wheelup", "wheeldown", "draganddrop"]
    valid_buttons = ["left", "right"]
    valid_click_types = ["normal", "hold", "release"]
    if action not in valid_actions:
        raise ValueError(f"Invalid action: '{action}'. Valid actions are: {', '.join(valid_actions)}")
    if button not in valid_buttons:
        raise ValueError(f"Invalid button: '{button}'. Valid buttons are: {', '.join(valid_buttons)}")
    if clicks < 1 or not isinstance(clicks, int):
        raise ValueError("Clicks must be a positive integer.")
    if click_type not in valid_click_types:
        raise ValueError(f"Invalid click type: '{click_type}'. Valid types are: {', '.join(valid_click_types)}")
    # Perform the specified mouse action
    if action == "click":
        if click_type == "normal":
            pyautogui.click(x, y, button=button, clicks=clicks)
            return
        elif click_type == "hold":
            pyautogui.moveTo(x, y)
            pyautogui.mouseDown(button=button)
            return
        elif click_type == "release":
            pyautogui.moveTo(x, y)
            pyautogui.mouseUp(button=button)
            return
        else:
            raise ValueError(f"Invalid click type: '{click_type}'.")
            
    elif action == "move":
        pyautogui.moveTo(x, y)
    elif action == "moveandclick":
        pyautogui.moveTo(x, y)
        pyautogui.click(x, y, button=button)
    elif action == "wheelup":
        pyautogui.scroll(-100)  # Adjust scroll amount as needed
    elif action == "wheeldown":
        pyautogui.scroll(100)  # Adjust scroll amount as needed
    elif action == "draganddrop":
        # Raise an error if start and end coordinates are not provided
        raise NotImplementedError("Drag and drop functionality is not currently implemented. Please provide start and end coordinates.")

def keybfunc(key, action="normal"):
    valid_actions = ["normal", "hold", "release"]
    if action not in valid_actions:
        raise ValueError(f"Invalid action: '{action}'. Valid actions are: {', '.join(valid_actions)}")

    # Perform the keyboard action
    if action == "normal":
        pyautogui.press(key)
    elif action == "hold":
        pyautogui.keyDown(key)
    elif action == "release":
        pyautogui.keyUp(key)

def typetext(text):
    pyautogui.write(text)

def imgclick(img , left, top, width, height, confidence):
    x, y = pyautogui.locateCenterOnScreen(img, region= (left, top, width, height) ,confidence=confidence)
    pyautogui.click(x, y)

def find_image_on_screen(image_path, confidence=0.9, region=None):
    screenshot = pyautogui.screenshot()
    screenshot_array = np.array(screenshot)
    screenshot_rgb = cv2.cvtColor(screenshot_array, cv2.COLOR_BGR2RGB)

    # Load the target image
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Use template matching with similarity check
    result = cv2.matchTemplate(screenshot_rgb, image_rgb, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= confidence:
        # Apply region if provided
        if region is not None:
            x, y, w, h = region
            max_loc = (max_loc[0] + x, max_loc[1] + y)

        # Return bounding box coordinates
        return (max_loc[0], max_loc[1], image.shape[1], image.shape[0])
    else:
        return None





def pixel_search(region, target_color, tolerance=0):

    # Capture the screen region
    screenshot = pyautogui.screenshot(region=region)
    
    # Convert to RGBA
    img = screenshot.convert('RGBA')
    
    # Get the pixels in the defined region
    width, height = img.size
    region_pixels = img.load()
    
    # Iterate over the pixels in the region
    for x in range(width):
        for y in range(height):
            pixel = region_pixels[x, y]
            if all(abs(pixel[i] - target_color[i]) <= tolerance for i in range(3)):  # Compare RGB only
                return (region[0] + x, region[1] + y)
    
    return None
