import skylom
import baymack
import flamzy
import func
import time
import pyautogui
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime
import clipboard


# Full path to your service account key file
cred = credentials.Certificate('firebase.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
#    'databaseURL': 'https://moneyfarm-f6617-default-rtdb.asia-southeast1.firebasedatabase.app'
    'databaseURL': 'https://moneyfarm-95358-default-rtdb.asia-southeast1.firebasedatabase.app/'
})


ref = db.reference('Farm1/MainData')
messages_ref = db.reference('Farm1/Messages')
print('gg')

def push_message(message):
    try:
        messages_ref.push(message)
        print("Message added successfully")
    except Exception as e:
        print(f"Error adding message: {e}")

def has_numbers(input_string):
    # Loop through each character in the string
    for char in input_string:
        # Check if the character is a digit
        if char.isdigit():
            return True
    # If no digits were found
    return False
run_baymack = True
run_flamzy = False
run_skylom = True
webpage = True
Farm_id = " Farm1 "

#ref.update({'Skylom_Coins': 3000})
#print("Skylom_Coins has been set to 2000.")

skylom_category = 0
baymack_category = 0
while True:
    now = datetime.now()
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S ")
    Date = formatted_datetime

    if run_baymack == True:
        baymack.baymack_alive()
        pink = baymack.pinkbar()
        if pink == 1:
            if webpage == True:
                message = Date +"|"+Farm_id+"|"+" Mack |"+" Pink Bar Found "
                push_message(message)
                print(message)
            baymack.remove_pinkbar()
            time.sleep(1)
        baymack.play_button_baymack()
        time.sleep(1)
        #func.windowf("IDLE Shell 3.8.10", "activate")
        verification = baymack.find_verification_baymack()
        if verification == 1:
            clipboard.copy("")
            if webpage == True:
                pyautogui.click(1546, 115)
                pyautogui.moveTo(1546, 115)
                pyautogui.mouseDown(1546, 115)
                time.sleep(0.5)
                pyautogui.moveTo(1387, 115)
                pyautogui.mouseUp(1387, 115)
                func.keybfunc("ctrl", "hold") 
                func.keybfunc("c", "normal")  
                func.keybfunc("ctrl", "release")
                
                baymack_coins = clipboard.paste()
                baymack_coins = baymack_coins.replace(",", "")
                if baymack_coins:
                    if not baymack_coins == "":
                        if has_numbers(baymack_coins) == True:
                            #baymack_coins = baymack_coins.replace("COINS", "")
                            print(baymack_coins,"Coins")
                            message = Date +"|"+Farm_id+"|"+" Mack |"+" Colleted Success Coins="+ baymack_coins
                            push_message(message)
                            print(message)
                            ref.update({'Baymack_Coins': baymack_coins})
            baymack.Solve_Emoji_baymack()


        elif verification == 4:
            print("img verification")
            baymack.solve_image_baymack()
        elif verification == 5:
            print("OCR verification")
            baymack.ocr_solver()
        elif verification == 2:
            print("Category verification found in Baymack...")
            clipboard.copy("")
            if webpage == True:
                pyautogui.click(1546, 115)
                pyautogui.moveTo(1546, 115)
                pyautogui.mouseDown(1546, 115)
                time.sleep(0.5)
                pyautogui.moveTo(1387, 115)
                pyautogui.mouseUp(1387, 115)
                func.keybfunc("ctrl", "hold") 
                func.keybfunc("c", "normal")  
                func.keybfunc("ctrl", "release")
                
                
                baymack_coins = clipboard.paste()
                baymack_coins = baymack_coins.replace(",", "")
                if baymack_coins:
                    if not baymack_coins == "":
                        if has_numbers(baymack_coins) == True:
                            #baymack_coins = baymack_coins.replace("COINS", "")
                            print(baymack_coins,"Coins")
                            message = Date +"|"+Farm_id+"|"+" Mack |"+" Colleted Success Coins="+ baymack_coins
                            push_message(message)
                            print(message)
                            ref.update({'Baymack_Coins': baymack_coins})
            if baymack_category == 0:
                baymack.solve_category_baymack()
            else:
                print("Baymack category =",baymack_category)
                baymack.solve_with_category_baymack(baymack_category)
                baymack_category = 0


        elif verification == 3:
            if baymack_category == 0:
                baymack_category = baymack.get_category1()
                print("Baymack Category =",baymack_category)
        else:
            print("No verification found in Baymack")

    else:
        print("Bymack Off")


    if run_skylom == True:
        skylom.skylom_alive()
        pink = skylom.pinkbar()
        if pink == 1:
            if webpage == True:
                message = Date +"|"+Farm_id+"|"+" Boola |"+" Pink Bar Found "
                push_message(message)
                print(message)
            skylom.remove_pinkbar()
            time.sleep(1)
        skylom.play_button_skylom()
        time.sleep(1)
        #func.windowf("IDLE Shell 3.8.10", "activate")
        verification = skylom.find_verification_skylom()
        if verification == 1:
            print("Category verification found in skylom...")
            if webpage == True:
                pyautogui.click(1524, 115)
                pyautogui.moveTo(1524, 115)
                pyautogui.mouseDown(1524, 115)
                time.sleep(0.5)
                pyautogui.moveTo(1370, 115)
                pyautogui.mouseUp(1370, 115)
                func.keybfunc("ctrl", "hold") 
                func.keybfunc("c", "normal")  
                func.keybfunc("ctrl", "release")
                
                skylom_coins = clipboard.paste()
                skylom_coins = skylom_coins.replace("COINS", "")
                if skylom_coins:
                    if not skylom_coins == "":
                        if has_numbers(skylom_coins) == True:
                            #baymack_coins = baymack_coins.replace("COINS", "")
                            print(skylom_coins,"Coins")
                            message = Date +"|"+Farm_id+"|"+" Boola |"+" Colleted Success Coins="+ skylom_coins
                            push_message(message)
                            print(message)
                            ref.update({'Skylom_Coins': skylom_coins})

            if skylom_category == 0:
                skylom.solve_category_skylom()
            else:
                print("skylom category =",skylom_category)
                skylom.solve_with_category_skylom(skylom_category)
                skylom_category = 0
            #skylom.solve_category_skylom()
            time.sleep(1)
            pyautogui.click(767, 745)
            pyautogui.click(890, 745)
            pyautogui.click(995, 745)
            pyautogui.click(1143, 745)


        elif verification == 2:
            print("IMG verification")
            skylom.solve_image_skylom()

        elif verification == 6:
            print("OCR verification")
            skylom.ocr_solver()
            
        elif verification == 3:
            print("Calc verification found...")
            skylom.solve_calculate()
        elif verification == 5:
            if skylom_category == 0:
                skylom_category = skylom.get_category1()
                print("skylom Category =",skylom_category)
        else:
            print("No verification found")
            
    else:
        print("skylom Off")

    if run_flamzy == True:
        flamzy.flamzy_alive()
        time.sleep(1)

        flamzy.play_button_flamzy()
        time.sleep(1)
        #func.windowf("IDLE Shell 3.8.10", "activate")
        verification = flamzy.find_verification_flamzy()
        if verification == 1:
            flamzy.Solve_Emoji_flamzy()
        elif verification == 2:
            print("image verification found in Flamzy...")
            flamzy.Solve_image_flamzy()
        else:
            print("No verification found in Flamzy")
    else:
        print("Flamzy Off")
