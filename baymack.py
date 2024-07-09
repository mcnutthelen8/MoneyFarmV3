import func
import pyautogui
import time
import emojirank
import clipboard
import getcategory
import pygetwindow
import img_captcha_bay
import ocr_captcha

def maximize_focused_window(title):
    windows = pygetwindow.getWindowsWithTitle(title)
    if windows:
        window = windows[0]
        window.activate()  # Activate the window
        window.maximize()  # Maximize the window
    else:
        print(f"No window found with title: {title}")


def check_win_exist(title):
    ggg =pygetwindow.getWindowsWithTitle(title)
    print(ggg)
    if ggg:
        print(title, "does exist")
        return True

    else:
        print(title, "does not exist")
        return False
    
baymack_title = "Baymack - Google Chrome"
def baymack_alive():
    if func.is_window_existent(baymack_title):
        print("Baymack is alive")
        func.windowf(baymack_title, "activate")
        func.windowf(baymack_title, "maximize")
        print("Baymack is Focused..")
    else:
        gg = check_win_exist("YouTube")
        if gg:
            print("Youtube Opened in Baymack")
            try:
                maximize_focused_window("YouTube")
                print("Successfully maximized the focused window.")
                pyautogui.click(470, 15)
            except RuntimeError as e:
                print(e)
            

        else:
            print("No Youtube Opened in Baymack")

        print("Baymack is not alive")


def pinkbar():
    try:
        pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240618101547.png", region=(10, 65, 200, 140), confidence=0.99)
        print("Pinkbar Found Baymack")
        return 1
    except pyautogui.ImageNotFoundException:
        print("No Pinkbar Found Baymack")
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
            print("Inspect Found skylom")
            print("Bar Deleted..")
            pyautogui.click(1904, 82)
            time.sleep(1)
            break
        except pyautogui.ImageNotFoundException:
            print("No Inspect Found Found skylom")
            print("Attempt", countm)
            countm += 1

#check if there's red play button


def blue_button_baymack(): 
    image_path = r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240616034322.png"
    region = (732, 368, 226, 92)
    confidence = 0.8
    try:
        x, y = pyautogui.locateCenterOnScreen(image_path, region=region, confidence=confidence)
        print("Blue button Found Baymack")
        pyautogui.click(942, 468)  
        time.sleep(1)
    except pyautogui.ImageNotFoundException:
        print("No Blue button Found Baymack")
def play_button_baymack():
    image_path = r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240615184949.png"#yt playbutton logo
    region = (916, 376, 67, 47)
    confidence = 0.9
    try:
        x, y = pyautogui.locateCenterOnScreen(image_path, region=region, confidence=confidence)
        print("Play button Found Baymack")
        pyautogui.click(x, y)  
        print("Play button Clicked")
        return 1
    except pyautogui.ImageNotFoundException:
        print("Play button not found on Baymack screen.")
        blue_button_baymack()
        pyautogui.moveTo(1310, 572)
        time.sleep(1)
        try:
            x, y = pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240628131230.png", region=(605, 600, 650, 360), confidence=0.9)
            pyautogui.click(x, y)
            print("Spin Found Baymack")
            return 0
        except pyautogui.ImageNotFoundException:
            print("No Spin Found Baymack")
        try:
            x, y = pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240618211337.png", region=(1256, 556, 113, 56), confidence=0.9)
            pyautogui.click(1300, 578)
            print("Skip Found Baymack")
            return 0
        except pyautogui.ImageNotFoundException:
            print("No Skip  Baymack.")
        
        try:
            x, y = pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240620001605.png", region=(800, 656, 353, 256), confidence=0.9)
            pyautogui.click(x, y )
            pyautogui.press("f5")
            print("Next Found Baymack")
            return 0
        except pyautogui.ImageNotFoundException:
            print("Next Skip  Baymack.")

        try:
            x, y = pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240705183202.png", region=(1027, 624, 146, 121), confidence=confidence)
            print("Recaptcha Found Baymack")
            pyautogui.press('f5')  
            time.sleep(1)
            return 0
        except pyautogui.ImageNotFoundException:
            print("No Recaptcha Found Baymack.")
            return 0
  
#find if any verification popups (Emoji/Img)
def find_verification_baymack():
    #Emoji Verification
    try:
        pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240615231953.png", region=(426, 618, 308, 322), confidence=0.9)
        print("Category verification Found Baymack")
        return 2
    except pyautogui.ImageNotFoundException:
        print("No Emoji verification  Baymack.")
        #Category Verification
        try:
            pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240618090739.png", region=(483, 611, 200, 200), confidence=0.95)
            print("Emoji verification Found Baymack")
            return 1
        except pyautogui.ImageNotFoundException:
            #video playing Verification
            try:
                pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240622011000.png", region=(782, 702, 125, 90), confidence=0.95)
                print("Video Playing bar Found Baymack")
                return 3
            except pyautogui.ImageNotFoundException:
                print("No Video Playing bar Found Baymack")
                #Image  Verification
                try:
                    pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240626120459.png", region=(763, 615, 400, 150), confidence=0.8)
                    print("Image Found Baymack")
                    return 4
                except pyautogui.ImageNotFoundException:
                    print("No Image Found Baymack")
                try:
                    pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240703173949.png", region=(875, 745, 121, 66), confidence=0.8)
                    print("OCR Found Baymack")
                    return 5
                except pyautogui.ImageNotFoundException:
                    print("No OCR Found Baymack")
                    return 0
#find_verification_baymack()

#OCR Verification
def ocr_solver():
    try:
        pyautogui.locateCenterOnScreen("captcha.png", region=(843, 621, 337, 267), confidence=0.9)
        print("Same Image Detect")
        clipboard.copy('1000')
        pyautogui.click(873,733)
        pyautogui.click(873,733)
        pyautogui.click(873,733)
        pyautogui.click(873,733)
        time.sleep(0.5)
        pyautogui.press('delete')
        func.keybfunc("ctrl", "hold") 
        func.keybfunc("v", "normal")  
        func.keybfunc("ctrl", "release")
        time.sleep(1)
        pyautogui.click(958,777)
        return 0
    except pyautogui.ImageNotFoundException:
        print("No Same Image Detect")
        screenshot = pyautogui.screenshot(region=(859, 634, 200, 59))
        screenshot.save('captcha.png')
        print('Screen shot saved Baymack')
        ocr = ocr_captcha.ocrcaptcha()
        if ocr == "1000":
            print('Ocr Failed')
        pyautogui.click(873,733)
        pyautogui.click(873,733)
        pyautogui.click(873,733)
        pyautogui.click(873,733)
        time.sleep(0.5)
        pyautogui.press('delete')
        func.keybfunc("ctrl", "hold") 
        func.keybfunc("v", "normal")  
        func.keybfunc("ctrl", "release")
        time.sleep(1)
        pyautogui.click(958,777)


#ocr_solver()

#Image Verification
def solve_image_baymack():
    answer = img_captcha_bay.get_image_answer()
    print(answer, "is less similar image in here")
    if answer == "0.png":
        pyautogui.click(835 ,692)
        print(answer,"Clicked...")
    elif answer == "1.png":
        pyautogui.click(895 ,692)
        print(answer,"Clicked...")
    elif answer == "2.png":
        pyautogui.click(955 ,692)
        print(answer,"Clicked...")
    elif answer == "3.png":
        pyautogui.click(1015 ,692)
        print(answer,"Clicked...")
    elif answer == "4.png":
        pyautogui.click(1075 ,692)
        print(answer,"Clicked...")       
    else:
        print("No image number found..",answer)
        pyautogui.click(835 ,692)

#solve Emoji Verification
def Solve_Emoji_baymack():
    pyautogui.moveTo(252, 690)
    pyautogui.mouseDown(button="left")
    time.sleep(0.3)
    pyautogui.moveTo(1648, 700)
    pyautogui.mouseUp(button="left")
    time.sleep(0.3)
    func.keybfunc("ctrl", "hold") 
    func.keybfunc("c", "normal")  
    func.keybfunc("ctrl", "release")
    rank = emojirank.get_emoji_rank()
    if rank == 1:
        pyautogui.click(606, 690)
        print("Emoji 1 Clicked")
    elif rank == 2:
        pyautogui.click(1035, 690)
        print("Emoji 2 Clicked")
    elif rank == 3:
        pyautogui.click(1192 ,690)
        print("Emoji 3 Clicked")
    else:
        pyautogui.click(1035, 690)
        print("No Emoji Number Collects")

#Solve Category Verification
#Get YT Link
def get_ytlinks_baymack():
    countm = 0
    while countm < 3:
        blue_button_baymack()
        print("Getting Yt Link")
        pyautogui.moveTo(1256, 393)
        pyautogui.click(button="right")
        time.sleep(1)
        count = 0
        while count < 3:
            try:
                pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240615235837.png", region=(1054, 378, 100, 114), confidence=0.8)
                pyautogui.moveTo(1256, 393)
                pyautogui.click(button="left")
                print("Youtube Link is Copied")
                video_url = clipboard.paste()
                print(video_url)
                return video_url
            except pyautogui.ImageNotFoundException:
                print("Waiting Count:", count)
                time.sleep(1)
                count += 1
        countm += 1

#Get Category with Link#1
def get_category1():
    video_url = get_ytlinks_baymack()
    if not video_url:  # Check if video_category is None
        print("Failed to fetch video category.", video_url)
        return 0
    if None == video_url:  # Check if video_category is None
        print("Failed to fetch video category.", video_url)
        return 0
    if "youtu" in video_url:
        category = getcategory.get_video_info(video_url)
        if category:
            print(f"Category: {category}")
            if "Howto" in category:
                return "How-To"
            else:
                return category
        else:
            print("Failed to fetch video info.")
            return 0
    else:
        print("youtu.be not found#2", video_url)
        return 0

#Find Correct Which Category
def replace_family_entertainment(text):
    return text.replace("Family Entertainment", "Family")

def split_user_input_and_find_word(user_input, word_to_find):
    # Replace "Family Entertainment" with "Family" in the input text
    modified_input = replace_family_entertainment(user_input)
    
    # Split the modified input string into lines, removing leading/trailing whitespace
    categories = [line.strip() for line in modified_input.split('\n') if line.strip()]
    
    # Check if there are exactly 4 lines
    if len(categories) != 4:
        print("Input string should contain exactly 4 lines.")
        return  0
    
    # Search for the word in each category (case-insensitive, partial match)
    for category_index, category in enumerate(categories, start=1):
        if isinstance(word_to_find, str) and isinstance(category, str):
            if word_to_find.lower() in category.lower() or category.lower() in word_to_find.lower():
                return f"word{category_index}"
        else:
            print("Both word_to_find and category should be strings")
            return
    
    # If word not found, return a more informative message
    print("Word is not found")
    return "word12"
#Solve Category 
def solve_category_baymack():
    #Get Video Category
    video_category = get_category1()
    #video_category = category
    if not video_category:  # Check if video_category is None
        print("Failed to fetch video category.", video_category)
        #pyautogui.click(750, 778)
        return
    if None == video_category:  # Check if video_category is None
        print("Failed to fetch video category.", video_category)
        #pyautogui.click(750, 778)
        return
    if 0 == video_category:  # Check if video_category is None
        print("Failed to fetch video category.", video_category)
        #pyautogui.click(750, 778)
        return
    print("Getting 4 Categorys...", video_category)
    #Get 4 Category
    pyautogui.click(470, 690)
    pyautogui.moveTo(470, 690)
    pyautogui.mouseDown(470, 690)
    time.sleep(0.5)
    pyautogui.moveTo(1379, 757)
    func.keybfunc("ctrl", "hold") 
    func.keybfunc("c", "normal")  
    func.keybfunc("ctrl", "release")
    user_input = clipboard.paste()
    print(user_input)
    try:
        result = split_user_input_and_find_word(user_input, video_category)
        if result:
            print(result)
            if result.lower() == "word1":
                pyautogui.click(750, 690)
                print("Category1 Solved")
            elif result.lower() == "word2":
                pyautogui.click(1100, 690)
                print("Category2 Solved")
            elif result.lower() == "word3":
                pyautogui.click(750, 755)
                print("Category3 Solved")
            elif result.lower() == "word4":
                pyautogui.click(750, 755)
                print("Category4 Solved")

            elif result.lower() == "word12":
                print("Clicking Music")
                resultg = split_user_input_and_find_word(user_input, "Entertainment")
                if resultg.lower() == "word1":
                    pyautogui.click(750, 690)
                    print("Category1 Solved")
                elif resultg.lower() == "word2":
                    pyautogui.click(1100, 690)
                    print("Category2 Solved")
                elif resultg.lower() == "word3":
                    pyautogui.click(750, 755)
                    print("Category3 Solved")
                elif resultg.lower() == "word4":
                    pyautogui.click(750, 755)
                    print("Category4 Solved")

                elif result.lower() == "word12":
                    print("Clicking people")
                    resultg = split_user_input_and_find_word(user_input, "People")
                    if resultg.lower() == "word1":
                        pyautogui.click(750, 690)
                        print("Category1 Solved")
                    elif resultg.lower() == "word2":
                        pyautogui.click(1100, 690)
                        print("Category2 Solved")
                    elif resultg.lower() == "word3":
                        pyautogui.click(750, 755)
                        print("Category3 Solved")
                    elif resultg.lower() == "word4":
                        pyautogui.click(750, 755)
                        print("Category4 Solved")

                    elif result.lower() == "word12":
                        print("Clicking Entertainment")
                        resultg = split_user_input_and_find_word(user_input, "Music")
                        if resultg.lower() == "word1":
                            pyautogui.click(750, 690)
                            print("Category1 Solved")
                        elif resultg.lower() == "word2":
                            pyautogui.click(1100, 690)
                            print("Category2 Solved")
                        elif resultg.lower() == "word3":
                            pyautogui.click(750, 755)
                            print("Category3 Solved")
                        elif resultg.lower() == "word4":
                            pyautogui.click(750, 755)
                            print("Category4 Solved")

                        elif result.lower() == "word12":
                            print("Clicking None")
                            resultg = split_user_input_and_find_word(user_input, "None")
                            if resultg.lower() == "word1":
                                pyautogui.click(750, 690)
                                print("Category1 Solved")
                            elif resultg.lower() == "word2":
                                pyautogui.click(1100, 690)
                                print("Category2 Solved")
                            elif resultg.lower() == "word3":
                                pyautogui.click(750, 755)
                                print("Category3 Solved")
                            elif resultg.lower() == "word4":
                                pyautogui.click(750, 755)
                                print("Category4 Solved")
                            
                            elif result.lower() == "word12":
                                pyautogui.click(1100, 690)
                                print("No Cateogry word found")

        else:
                pyautogui.click(1100, 690)
                print("No Cateogry word found")

    except ValueError as e:
        print("Error:", e)
    

def solve_with_category_baymack(category):
    #Get Video Category
    video_category = category
    #video_category = category
    if not video_category:  # Check if video_category is None
        print("Failed to fetch video category.", video_category)
        #pyautogui.click(750, 778)
        return
    if None == video_category:  # Check if video_category is None
        print("Failed to fetch video category.", video_category)
        #pyautogui.click(750, 778)
        return
    if 0 == video_category:  # Check if video_category is None
        print("Failed to fetch video category.", video_category)
        #pyautogui.click(750, 778)
        return
    print("Getting 4 Categorys...", video_category)
    #Get 4 Category
    pyautogui.click(470, 690)
    pyautogui.moveTo(470, 690)
    pyautogui.mouseDown(470, 690)
    time.sleep(0.5)
    pyautogui.moveTo(1379, 757)
    func.keybfunc("ctrl", "hold") 
    func.keybfunc("c", "normal")  
    func.keybfunc("ctrl", "release")
    user_input = clipboard.paste()
    print(user_input)
    try:
        result = split_user_input_and_find_word(user_input, video_category)
        if result:
            print(result)
            if result.lower() == "word1":
                pyautogui.click(750, 690)
                print("Category1 Solved")
            elif result.lower() == "word2":
                pyautogui.click(1100, 690)
                print("Category2 Solved")
            elif result.lower() == "word3":
                pyautogui.click(750, 755)
                print("Category3 Solved")
            elif result.lower() == "word4":
                pyautogui.click(750, 755)
                print("Category4 Solved")

            elif result.lower() == "word12":
                print("Clicking Music")
                resultg = split_user_input_and_find_word(user_input, "Entertainment")
                if resultg.lower() == "word1":
                    pyautogui.click(750, 690)
                    print("Category1 Solved")
                elif resultg.lower() == "word2":
                    pyautogui.click(1100, 690)
                    print("Category2 Solved")
                elif resultg.lower() == "word3":
                    pyautogui.click(750, 755)
                    print("Category3 Solved")
                elif resultg.lower() == "word4":
                    pyautogui.click(750, 755)
                    print("Category4 Solved")

                elif result.lower() == "word12":
                    print("Clicking people")
                    resultg = split_user_input_and_find_word(user_input, "People")
                    if resultg.lower() == "word1":
                        pyautogui.click(750, 690)
                        print("Category1 Solved")
                    elif resultg.lower() == "word2":
                        pyautogui.click(1100, 690)
                        print("Category2 Solved")
                    elif resultg.lower() == "word3":
                        pyautogui.click(750, 755)
                        print("Category3 Solved")
                    elif resultg.lower() == "word4":
                        pyautogui.click(750, 755)
                        print("Category4 Solved")

                    elif result.lower() == "word12":
                        print("Clicking Entertainment")
                        resultg = split_user_input_and_find_word(user_input, "Music")
                        if resultg.lower() == "word1":
                            pyautogui.click(750, 690)
                            print("Category1 Solved")
                        elif resultg.lower() == "word2":
                            pyautogui.click(1100, 690)
                            print("Category2 Solved")
                        elif resultg.lower() == "word3":
                            pyautogui.click(750, 755)
                            print("Category3 Solved")
                        elif resultg.lower() == "word4":
                            pyautogui.click(750, 755)
                            print("Category4 Solved")

                        elif result.lower() == "word12":
                            print("Clicking None")
                            resultg = split_user_input_and_find_word(user_input, "None")
                            if resultg.lower() == "word1":
                                pyautogui.click(750, 690)
                                print("Category1 Solved")
                            elif resultg.lower() == "word2":
                                pyautogui.click(1100, 690)
                                print("Category2 Solved")
                            elif resultg.lower() == "word3":
                                pyautogui.click(750, 755)
                                print("Category3 Solved")
                            elif resultg.lower() == "word4":
                                pyautogui.click(750, 755)
                                print("Category4 Solved")
                            
                            elif result.lower() == "word12":
                                pyautogui.click(1100, 690)
                                print("No Cateogry word found")

        else:
                pyautogui.click(1100, 690)
                print("No Cateogry word found")

    except ValueError as e:
        print("Error:", e)
    

