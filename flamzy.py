import func
import pyautogui
import time
import emojirank
import clipboard
import img_captcha_flamzy
import img_captcha_flamzypinkbar


def autodone():
    try:
        pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240617025622.png", region=(1766, 990, 145, 67), confidence=0.95)
        print("Done Found flamzy")
        pyautogui.click(86,49)
        return 1
    except pyautogui.ImageNotFoundException:
        print("No Done Found flamzy")
        return 0
def pinkbar():
    try:
        pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240617015538.png", region=(10, 65, 200, 140), confidence=0.95)
        print("Pinkbar Found flamzy")
        return 1
    except pyautogui.ImageNotFoundException:
        print("No Pinkbar Found flamzy")
        return 0
    

def remove_pinkbar():
    pyautogui.click(1904, 82)
    time.sleep(1)
    pyautogui.moveTo(40, 78)
    pyautogui.click(button="right")
    time.sleep(1)
    pyautogui.moveTo(93, 408)
    pyautogui.click()
    countm = 0
    while countm < 5:
        time.sleep(1)
        try:
            pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240617000112.png", region=(1805, 68, 60, 37), confidence=0.9)
            time.sleep(1)
            pyautogui.press('delete')
            print("Inspect Found flamzy")
            print("Bar Deleted..")
            pyautogui.click(1904, 82)
            time.sleep(1)
            break
        except pyautogui.ImageNotFoundException:
            print("No Inspect Found Found flamzy")
            print("Attempt", countm)
            countm += 1


#find if flamzy tab is still alive and focus
flamzy_title = "Flamzy - Google Chrome"
def flamzy_alive():
    if func.is_window_existent(flamzy_title):
        print("flamzy is alive")
        func.windowf(flamzy_title, "activate")
        func.windowf(flamzy_title, "maximize")
        print("flamzy is Focused..")
    else:
        print("flamzy is not alive")

#check if there's red play button
def play_button_flamzy():
    
    pink = pinkbar()
    if pink == 1:
        image_path = r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240615184949.png"#yt playbutton logo
        region = (925, 400, 67, 47)
        confidence = 0.9
        try:

            x, y = pyautogui.locateCenterOnScreen(image_path, region=region, confidence=confidence)
            print("Play button Found flamzy(Pinkbar)")
            pyautogui.click(x, y)  
            time.sleep(1)
            pyautogui.click(30, 600) 
            print("Play button Clicked")
        except pyautogui.ImageNotFoundException:
            print("Play button not found on flamzy screen.(Pinkbar)")
            blue_button_flamzy()
    
    else:
        image_path = r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240615184949.png"#yt playbutton logo
        region = (925, 377, 67, 47)
        confidence = 0.9
        try:
            x, y = pyautogui.locateCenterOnScreen(image_path, region=region, confidence=confidence)
            print("Play button Found flamzy")
            pyautogui.click(x, y)  
            time.sleep(1)
            pyautogui.click(30, 600) 
            print("Play button Clicked")
        except pyautogui.ImageNotFoundException:
            print("Play button not found on flamzy screen.")
            blue_button_flamzy()
        

#check if there's blue play button
def blue_button_flamzy():
    image_path = r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240617020413.png"
    region = (964, 361, 226, 92)
    confidence = 0.8
    try:
        x, y = pyautogui.locateCenterOnScreen(image_path, region=region, confidence=confidence)
        print("Blue button Found flamzy")
        pyautogui.click(942, 468)  
        time.sleep(1)
    except pyautogui.ImageNotFoundException:
        print("No Blue button Found flamzy")
    
#find if any verification popups (Emoji/Img)
def find_verification_flamzy():
    #Emoji Verification
    try:
        pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240617020254.png", region=(749, 618, 416, 91), confidence=0.9)
        print("Emoji verification Found flamzy")
        return 1
    except pyautogui.ImageNotFoundException:
        print("No Emoji verification  flamzy.")
        #Image Verification
        try:
            pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240617022955.png", region=(774, 594, 340, 117), confidence=0.9)
            print("Image verification Found flamzy")
            return 2
        except pyautogui.ImageNotFoundException:
            print("No Image verification flamzy")
            return 0


#solve Emoji Verification
def Solve_Emoji_flamzy():
    pyautogui.click(60, 646)
    time.sleep(0.8)
    pyautogui.moveTo(1561, 656)
    pyautogui.mouseDown(button="left")
    time.sleep(0.3)
    pyautogui.moveTo(1561, 686)
    pyautogui.mouseUp(button="left")
    time.sleep(0.3)
    func.keybfunc("ctrl", "hold") 
    func.keybfunc("c", "normal")  
    func.keybfunc("ctrl", "release")
    rank = emojirank.get_emoji_rank()
    if rank == 1:
        pyautogui.click(606, 696)
        print("Emoji 1 Clicked")
        autodone()
    elif rank == 2:
        pyautogui.click(1035, 696)
        print("Emoji 2 Clicked")
        autodone()
    elif rank == 3:
        pyautogui.click(1192 ,696)
        print("Emoji 3 Clicked")
        autodone()
    else:
        pyautogui.click(859, 696)
        print("No Emoji Number Collects")
        autodone()

def Solve_image_flamzy():
    pink = pinkbar()
    if pink == 1:
        answer = img_captcha_flamzypinkbar.get_image_answer()
        print(answer, "is less similar image in here(Pinkbar)")
        if answer == "0.png":
            pyautogui.click(835 ,710)
            print(answer,"Clicked...(Pinkbar)")
        elif answer == "1.png":
            pyautogui.click(895 ,710)
            print(answer,"Clicked...(Pinkbar)")
        elif answer == "2.png":
            pyautogui.click(955 ,710)
            print(answer,"Clicked...(Pinkbar)")
        elif answer == "3.png":
            pyautogui.click(1015 ,710)
            print(answer,"Clicked...(Pinkbar)")
        elif answer == "4.png":
            pyautogui.click(1065 ,710)
            print(answer,"Clicked...(Pinkbar)")       
        else:
            print("No image number found..(Pinkbar)",answer)
            pyautogui.click(835 ,710)
    else:
        answer = img_captcha_flamzy.get_image_answer()
        print(answer, "is less similar image in here")
        if answer == "0.png":
            pyautogui.click(835 ,710)
            print(answer,"Clicked...")
        elif answer == "1.png":
            pyautogui.click(895 ,710)
            print(answer,"Clicked...")
        elif answer == "2.png":
            pyautogui.click(955 ,710)
            print(answer,"Clicked...")
        elif answer == "3.png":
            pyautogui.click(1015 ,710)
            print(answer,"Clicked...")
        elif answer == "4.png":
            pyautogui.click(1065 ,710)
            print(answer,"Clicked...")       
        else:
            print("No image number found..",answer)
            pyautogui.click(835 ,710)

