import func
import pyautogui
import time
import img_captcha
import clipboard
import getcategory
import pygetwindow
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
    
#find if skylom tab is still alive and focus
skylom_title = "Skylom - Google Chrome"
def skylom_alive():
    if func.is_window_existent(skylom_title):
        print("Skylom is alive")
        func.windowf(skylom_title, "activate")
        func.windowf(skylom_title, "maximize")
        print("Skylom is Focused..")
    else:
        print("Skylom is not alive")
        gg = check_win_exist("YouTube")
        if gg:
            print("Youtube Opened in Skylom")
            try:
                maximize_focused_window("YouTube")
                print("Successfully maximized the focused window.")
                pyautogui.click(470, 15)
            except RuntimeError as e:
                print(e)
            

        else:
            print("No Youtube Opened in Skylom")

        print("Skylom is not alive")
def pinkbar():
    try:
        pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240616234523.png", region=(10, 65, 200, 140), confidence=0.98)
        print("Pinkbar Found skylom")
        return 1
    except pyautogui.ImageNotFoundException:
        print("No Pinkbar Found skylom")




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
def play_button_skylom():
    image_path = r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240615184949.png"#yt playbutton logo
    region = (926, 401, 67, 47)
    confidence = 0.9
    try:
        x, y = pyautogui.locateCenterOnScreen(image_path, region=region, confidence=confidence)
        print("Play button Found skylom")
        pyautogui.click(x, y)  
        time.sleep(1)
        pyautogui.click(30, 600) 
        print("Play button Clicked")
        return 1
    except pyautogui.ImageNotFoundException:
        print("Play button not found on skylom screen.")
        blue_button_skylom()
        try:
            x, y = pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240620071723.png", region=(861, 65, 170, 68), confidence=confidence)
            print("Prize Found Skylom")
            pyautogui.click(x, y)  
            time.sleep(1)
            return 0
        except pyautogui.ImageNotFoundException:
            print("No Prize Found Skylom.")

        try:
            x, y = pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240705183202.png", region=(1026, 682, 102, 102), confidence=confidence)
            print("Recaptcha Found Skylom")
            pyautogui.press('f5')  
            time.sleep(1)
            return 0
        except pyautogui.ImageNotFoundException:
            print("Recaptcha Found Skylom.")
            return 0

        

#check if there's blue play button
def blue_button_skylom():
    image_path = r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240616204809.png"
    region = (753, 384, 226, 92)
    confidence = 0.8
    try:
        x, y = pyautogui.locateCenterOnScreen(image_path, region=region, confidence=confidence)
        print("Blue button Found skylom")
        pyautogui.click(942, 468)  
        time.sleep(1)
    except pyautogui.ImageNotFoundException:
        print("No Blue button Found skylom")
    

   
#find if any verification popups (Emoji/Img)
def find_verification_skylom():
    #Category Verification
    try:
        pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240616205820.png", region=(773, 678, 340, 67), confidence=0.6)
        print("Category verification Found skylom")
        return 1
    except pyautogui.ImageNotFoundException:
        print("No Category verification  skylom.")
        #Image Verification
        try:
            pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240616214953.png", region=(778, 672, 400, 115), confidence=0.9)
            print("Image verification Found skylom")
            region = (871, 735, 56, 60)
            target_color = (0, 0, 0)  # Hex 0x101010
            tolerance = 5
            found_pixel = func.pixel_search(region, target_color, tolerance)
            if found_pixel:
                print("Matching pixel found at:", found_pixel)
                return 2
            else:
                print("No matching pixel found.")
                return 0
        except pyautogui.ImageNotFoundException:
            print("No Image verification skylom")
            #Calculator Verification
            try:
                pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240616230752.png", region=(684, 163, 606, 249), confidence=0.8)
                print("Calculator verification Found skylom")
                return 3
            except pyautogui.ImageNotFoundException:
                print("No Calculator verification skylom")
                #Oopss Verification
                try:
                    pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240617005350.png", region=(684, 163, 606, 249), confidence=0.8)
                    print("Oopss  Found skylom")
                    pyautogui.click(86,49)
                    return 4
                except pyautogui.ImageNotFoundException:
                    print("No Oopss Calculator verification skylom")
                    try:
                        pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240622011628.png", region=(640, 756, 150, 92), confidence=0.95)
                        print("Video Playing bar  Found skylom")
                        return 5
                    except pyautogui.ImageNotFoundException:
                        print("No Video Playing bar  Found skylom")

                    try:
                        pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240703180416.png", region=(895, 820, 135, 66), confidence=0.9)
                        print("OCR  Found skylom")
                        return 6
                    except pyautogui.ImageNotFoundException:
                        print("No OCR  Found skylom")
                        return 0

def ocr_solver():
    try:
        pyautogui.locateCenterOnScreen("captcha.png", region=(840, 621, 337, 267), confidence=0.9)
        print("Same Image Detect")
        clipboard.copy('1000')
        pyautogui.click(868,803)
        pyautogui.click(868,803)
        pyautogui.click(868,803)
        pyautogui.click(868,803)
        time.sleep(0.5)
        pyautogui.press('delete')
        func.keybfunc("ctrl", "hold") 
        func.keybfunc("v", "normal")  
        func.keybfunc("ctrl", "release")
        time.sleep(1)
        pyautogui.click(947,844)
        return 0
    except pyautogui.ImageNotFoundException:
        print("No Same Image Detect")
        screenshot = pyautogui.screenshot(region=(853, 702, 200, 59))
        screenshot.save('captcha.png')
        print('Screen shot saved Skylom')
        ocr = ocr_captcha.ocrcaptcha()
        if ocr == "1000":
            print('Ocr Failed')
        pyautogui.click(868,803)
        pyautogui.click(868,803)
        pyautogui.click(868,803)
        pyautogui.click(868,803)
        time.sleep(0.5)
        pyautogui.press('delete')
        func.keybfunc("ctrl", "hold") 
        func.keybfunc("v", "normal")  
        func.keybfunc("ctrl", "release")
        time.sleep(1)
        pyautogui.click(947,844)


#Solve Category Verification
#Get YT Link
def get_ytlinks_skylom():
    countm = 0
    while countm < 3:
        blue_button_skylom()
        print("Getting Yt Link")
        pyautogui.moveTo(1256, 438)
        pyautogui.click(button="right")
        time.sleep(1)
        count = 0
        while count < 3:
            try:
                pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240615235837.png", region=(1054, 378, 100, 114), confidence=0.8)
                pyautogui.moveTo(1256, 438)
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
    video_url = get_ytlinks_skylom()
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
def solve_with_category_skylom(category):
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
    pyautogui.click(470, 745)
    pyautogui.moveTo(470, 745)
    pyautogui.mouseDown(470, 745)
    time.sleep(0.5)
    pyautogui.moveTo(1279, 745)
    pyautogui.mouseUp(1279, 745)
    func.keybfunc("ctrl", "hold") 
    func.keybfunc("c", "normal")  
    func.keybfunc("ctrl", "release")
    user_input = clipboard.paste()
    print(user_input)
    try:
        result = split_user_input_and_find_word(user_input, video_category)
        print(result)
        if result:
            if result.lower() == "word1":
                pyautogui.click(767, 745)
                print("Category1 Solved")
            elif result.lower() == "word2":
                pyautogui.click(900, 745)
                print("Category2 Solved")
            elif result.lower() == "word3":
                pyautogui.click(995, 745)
                print("Category3 Solved")
            elif result.lower() == "word4":
                pyautogui.click(1143, 745)
                print("Category4 Solved")

            elif result.lower() == "word12":
                print("Clicking Music")
                resultg = split_user_input_and_find_word(user_input, "Entertainment")
                if resultg.lower() == "word1":
                    pyautogui.click(767, 745)
                    print("Category1 Solved")
                elif resultg.lower() == "word2":
                    pyautogui.click(900, 745)
                    print("Category2 Solved")
                elif resultg.lower() == "word3":
                    pyautogui.click(995, 745)
                    print("Category3 Solved")
                elif resultg.lower() == "word4":
                    pyautogui.click(1143, 745)
                    print("Category4 Solved")

                elif result.lower() == "word12":
                    print("Clicking people")
                    resultg = split_user_input_and_find_word(user_input, "People")
                    if resultg.lower() == "word1":
                        pyautogui.click(767, 745)
                        print("Category1 Solved")
                    elif resultg.lower() == "word2":
                        pyautogui.click(900, 745)
                        print("Category2 Solved")
                    elif resultg.lower() == "word3":
                        pyautogui.click(995, 745)
                        print("Category3 Solved")
                    elif resultg.lower() == "word4":
                        pyautogui.click(1143, 745)
                        print("Category4 Solved")

                    elif result.lower() == "word12":
                        print("Clicking Entertainment")
                        resultg = split_user_input_and_find_word(user_input, "Music")
                        if resultg.lower() == "word1":
                            pyautogui.click(767, 745)
                            print("Category1 Solved")
                        elif resultg.lower() == "word2":
                            pyautogui.click(900, 745)
                            print("Category2 Solved")
                        elif resultg.lower() == "word3":
                            pyautogui.click(995, 745)
                            print("Category3 Solved")
                        elif resultg.lower() == "word4":
                            pyautogui.click(1143, 745)
                            print("Category4 Solved")
                        
                        elif result.lower() == "word12":
                            print("Clicking None")
                            resultg = split_user_input_and_find_word(user_input, "None")
                            if resultg.lower() == "word1":
                                pyautogui.click(767, 745)
                                print("Category1 Solved")
                            elif resultg.lower() == "word2":
                                pyautogui.click(900, 745)
                                print("Category2 Solved")
                            elif resultg.lower() == "word3":
                                pyautogui.click(995, 745)
                                print("Category3 Solved")
                            elif resultg.lower() == "word4":
                                pyautogui.click(1143, 745)
                                print("Category4 Solved")

                            elif result.lower() == "word12":
                                pyautogui.click(767, 745)
                                print("No Cateogry word found")

        else:
            pyautogui.click(767, 745)
            print("No Cateogry word found")

    except ValueError as e:
        print("Error:", e)

def solve_category_skylom():
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
    pyautogui.click(470, 745)
    pyautogui.moveTo(470, 745)
    pyautogui.mouseDown(470, 745)
    time.sleep(0.5)
    pyautogui.moveTo(1279, 745)
    pyautogui.mouseUp(1279, 745)
    func.keybfunc("ctrl", "hold") 
    func.keybfunc("c", "normal")  
    func.keybfunc("ctrl", "release")
    user_input = clipboard.paste()
    print(user_input)
    try:
        result = split_user_input_and_find_word(user_input, video_category)
        print(result)
        if result:
            if result.lower() == "word1":
                pyautogui.click(767, 745)
                print("Category1 Solved")
            elif result.lower() == "word2":
                pyautogui.click(900, 745)
                print("Category2 Solved")
            elif result.lower() == "word3":
                pyautogui.click(995, 745)
                print("Category3 Solved")
            elif result.lower() == "word4":
                pyautogui.click(1143, 745)
                print("Category4 Solved")

            elif result.lower() == "word12":
                print("Clicking Music")
                resultg = split_user_input_and_find_word(user_input, "Entertainment")
                if resultg.lower() == "word1":
                    pyautogui.click(767, 745)
                    print("Category1 Solved")
                elif resultg.lower() == "word2":
                    pyautogui.click(900, 745)
                    print("Category2 Solved")
                elif resultg.lower() == "word3":
                    pyautogui.click(995, 745)
                    print("Category3 Solved")
                elif resultg.lower() == "word4":
                    pyautogui.click(1143, 745)
                    print("Category4 Solved")

                elif result.lower() == "word12":
                    print("Clicking people")
                    resultg = split_user_input_and_find_word(user_input, "People")
                    if resultg.lower() == "word1":
                        pyautogui.click(767, 745)
                        print("Category1 Solved")
                    elif resultg.lower() == "word2":
                        pyautogui.click(900, 745)
                        print("Category2 Solved")
                    elif resultg.lower() == "word3":
                        pyautogui.click(995, 745)
                        print("Category3 Solved")
                    elif resultg.lower() == "word4":
                        pyautogui.click(1143, 745)
                        print("Category4 Solved")

                    elif result.lower() == "word12":
                        print("Clicking Entertainment")
                        resultg = split_user_input_and_find_word(user_input, "Music")
                        if resultg.lower() == "word1":
                            pyautogui.click(767, 745)
                            print("Category1 Solved")
                        elif resultg.lower() == "word2":
                            pyautogui.click(900, 745)
                            print("Category2 Solved")
                        elif resultg.lower() == "word3":
                            pyautogui.click(995, 745)
                            print("Category3 Solved")
                        elif resultg.lower() == "word4":
                            pyautogui.click(1143, 745)
                            print("Category4 Solved")
                        
                        elif result.lower() == "word12":
                            print("Clicking None")
                            resultg = split_user_input_and_find_word(user_input, "None")
                            if resultg.lower() == "word1":
                                pyautogui.click(767, 745)
                                print("Category1 Solved")
                            elif resultg.lower() == "word2":
                                pyautogui.click(900, 745)
                                print("Category2 Solved")
                            elif resultg.lower() == "word3":
                                pyautogui.click(995, 745)
                                print("Category3 Solved")
                            elif resultg.lower() == "word4":
                                pyautogui.click(1143, 745)
                                print("Category4 Solved")

                            elif result.lower() == "word12":
                                pyautogui.click(767, 745)
                                print("No Cateogry word found")

        else:
            pyautogui.click(767, 745)
            print("No Cateogry word found")

    except ValueError as e:
        print("Error:", e)



#Image Verification
def solve_image_skylom():
    answer = img_captcha.get_image_answer()
    print(answer, "is less similar image in here")
    if answer == "0.png":
        pyautogui.click(835 ,770)
        print(answer,"Clicked...")
    elif answer == "1.png":
        pyautogui.click(895 ,770)
        print(answer,"Clicked...")
    elif answer == "2.png":
        pyautogui.click(955 ,770)
        print(answer,"Clicked...")
    elif answer == "3.png":
        pyautogui.click(1015 ,770)
        print(answer,"Clicked...")
    elif answer == "4.png":
        pyautogui.click(1075 ,770)
        print(answer,"Clicked...")       
    else:
        print("No image number found..",answer)
        pyautogui.click(835 ,770)

def find_lowest(num1, num2, num3, num4):
    # Convert string inputs to integers
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    num4 = int(num4)
    
    answer = 1
    lowest = num1
    print(lowest, "is num1", num1)
    
    if num2 < lowest:
        print(num2, "is lower than", lowest)
        lowest = num2
        answer = 2
    
    if num3 < lowest:
        print(num3, "is lower than", lowest)
        lowest = num3
        answer = 3
    
    if num4 < lowest:
        print(num4, "is lower than", lowest)
        lowest = num4
        answer = 4

    print(num1, num2, num3, num4)
    print(answer, "is lowest in func")
    return answer


def solve_calculate():
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    try:
        x,y = pyautogui.locateCenterOnScreen(r"C:\Users\Coder\Desktop\MoneyFarmV3\images\Screen_20240616231231.png", region=(942, 440, 155, 80), confidence=0.8)
        print("True False Found")
        pyautogui.click(x, y)  
        print("False Clicked...")
        return 
    except pyautogui.ImageNotFoundException:
        print("Trying to Get Numbers")
        pyautogui.moveTo(603, 473)
        pyautogui.mouseDown(603, 473)
        time.sleep(0.3)
        pyautogui.moveTo(849, 473)
        time.sleep(0.5)
        func.keybfunc("ctrl", "hold") 
        func.keybfunc("c", "normal")  
        func.keybfunc("ctrl", "release")
        time.sleep(0.5)
        num1 = clipboard.paste()
        #num1 = int(num1)
        if num1 == 0 or num1 =="":
            print(num1, "Num1 is broke")
            return
        print(num1)

        pyautogui.moveTo(950, 473)
        time.sleep(0.5)
        func.keybfunc("ctrl", "hold") 
        func.keybfunc("c", "normal")  
        func.keybfunc("ctrl", "release")
        time.sleep(0.5)

        num2 = clipboard.paste()
        num2 = num2.replace(num1, "")
        #num2 = int(num2)
        if num2 == 0 or num2 =="":
            print(num2, "num2 is broke")
            return
        print(num2)

        pyautogui.moveTo(1050, 473)
        time.sleep(0.5)
        func.keybfunc("ctrl", "hold") 
        func.keybfunc("c", "normal")  
        func.keybfunc("ctrl", "release")
        num3 = clipboard.paste()
        print(num3,"without repplace")
        num3 = num3.replace(num1, "")
        num3 = num3.replace(num2, "")
        #num3 = int(num3)
        if num3 == 0 or num3 =="":
            print(num3, "num3 is broke")
            return
        print(num3)

        pyautogui.moveTo(1150, 473)
        pyautogui.mouseUp(1150, 473)
        time.sleep(0.5)
        func.keybfunc("ctrl", "hold") 
        func.keybfunc("c", "normal")  
        func.keybfunc("ctrl", "release")
        num4 = clipboard.paste()
        num4 = num4.replace(num1, "")
        num4 = num4.replace(num2, "")
        num4 = num4.replace(num3, "")
        num4 = int(num4)
        if num4 == 0 or num4 =="":
            print(num4, "num4 is broke")
            return
        print(num4)
        time.sleep(0.5)
        #num5 = "999"
        print(num1,  num2, num3, num4, "is full numbers")
        lowest_value = find_lowest(num1,  num2, num3, num4)
        print(lowest_value, "is lowest")
        time.sleep(1)
        if lowest_value == 1:
            pyautogui.click(805, 477)
            print("1 Number Clicked...")
        elif lowest_value == 2:
            pyautogui.click(905, 477)
            print("2 Number Clicked...")
        elif lowest_value == 3:
            pyautogui.click(1005, 477)
            print("3 Number Clicked...")
        elif lowest_value == 4:
            pyautogui.click(1105, 477)
            print("4 Number Clicked...")
        else:
            pyautogui.click(1105, 477)
            print("No valid number Found")


