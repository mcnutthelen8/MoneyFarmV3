import os
import pyautogui
import cv2
import os
import numpy as np
import clipboard


def get_image_answer():
    # Define a list of coordinates and sizes for the regions
    regions = [
        (809, 735, 56, 60),
        (871, 735, 56, 60),
        (929, 735, 56, 60),
        (989, 735, 56, 60),
        (1049, 735, 56, 60)
    ]

    def capture_screenshots(regions):
        # Create a subfolder named "cropped" if it doesn't exist
        if not os.path.exists("cropped"):
            os.makedirs("cropped")
        
        for i, region in enumerate(regions):
            x, y, width, height = region
            # Take a screenshot of the specified region
            screenshot = pyautogui.screenshot(region=(x, y, width, height))
            screenshot.save(f'C:/Users/Coder/Desktop/MoneyFarmV2/python/cropped/{i}.png')

    # Capture 5 screenshots of the specified areas
    capture_screenshots(regions)

    pyautogui.sleep(1)



    # Path to directory containing images
    image_dir = r'C:/Users/Coder/Desktop/MoneyFarmV2/python/cropped/'

    # Threshold value for filtering similar images
    threshold = 0.9

    # Dictionary to store image similarities
    similarities = {}

    # Iterate over all image pairs and calculate their structural similarity
    for i, img_file in enumerate(os.listdir(image_dir)):
        img_path = os.path.join(image_dir, img_file)
        if not os.path.isfile(img_path):
            continue
        img1 = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        for j in range(i+1, len(os.listdir(image_dir))):
            other_img_file = os.listdir(image_dir)[j]
            other_img_path = os.path.join(image_dir, other_img_file)
            if not os.path.isfile(other_img_path):
                continue
            img2 = cv2.imread(other_img_path, cv2.IMREAD_GRAYSCALE)
            similarity = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)[0][0]
            similarities[(img_path, other_img_path)] = similarity
            similarities[(other_img_path, img_path)] = similarity

    # Calculate the average similarity score for each image
    image_scores = {}
    for img_path in os.listdir(image_dir):
        img_path = os.path.join(image_dir, img_path)
        if not os.path.isfile(img_path):
            continue
        similar_scores = [v for k, v in similarities.items() if k[0] == img_path]
        avg_score = np.mean(similar_scores)
        image_scores[img_path] = avg_score

    # Find the image with the least similarity to other images
    min_score = min(image_scores.values())
    min_images = [k for k, v in image_scores.items() if v == min_score]
    if len(min_images) == 1:
        min_image_name = os.path.basename(min_images[0])
        print(f"Image {min_image_name} has the least similarity with an average score of {min_score}")
        clipboard.copy(min_image_name)
        return min_image_name
    else:
        # If there are multiple images with the same minimum similarity score,
        # choose the image with the smallest file size as the least similar image
        min_size = float('inf')
        min_image = None
        for image in min_images:
            size = os.path.getsize(image)
            if size < min_size:
                min_size = size
                min_image = image
        min_image_name = os.path.basename(min_image)
        print(f"Image {min_image_name} has the least similarity with an average score of {min_score}")
        clipboard.copy(min_image_name)
        return min_image_name


