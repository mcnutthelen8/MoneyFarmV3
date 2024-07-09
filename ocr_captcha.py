import easyocr
import clipboard
import re

def ocrcaptcha():
    # Initialize the EasyOCR reader without GPU
    reader = easyocr.Reader(['en'], gpu=False)  # Disable GPU usage
    # Read the image
    image_path = 'captcha.png'
    try:
        result = reader.readtext(image_path)
        # Display the results
        for detection in result:
            text = detection[1]  # Extract the text from the detection tuple
            print(text)
            # Remove leading and trailing spaces and newlines
            cleaned_text = text.strip()
            
            # Check if cleaned text contains only 0-9 and A-Z characters
            if not re.match(r'^[0-9A-Za-z]+$', cleaned_text):
                cleaned_text = "1000"
                print('gg')
            else:
                print(f"Detected text: {cleaned_text}")
            
            clipboard.copy(cleaned_text)
            return cleaned_text
    except Exception as e:
        print(f"Error reading text: {e}")
        clipboard.copy("1000")
        return "1000"
