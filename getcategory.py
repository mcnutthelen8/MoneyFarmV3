import requests
from bs4 import BeautifulSoup
import clipboard
import time

headers = {
    'User-Agent': 'My User Agent 1.0',
}

def fetch_video_category(video_url, timeout=8):
    try:
        response = requests.get(video_url, headers=headers, timeout=timeout)
        print("Response received")
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            category_tag = soup.find('meta', itemprop='genre')
            category = category_tag['content'] if category_tag else None
            return category
    except requests.Timeout:
        print(f"Request timed out after {timeout} seconds")
    except Exception as e:
        print(f"Error: {e}")
    return None

def get_video_info(video_url, retries=3, timeout=8):
    for attempt in range(retries):
        category = fetch_video_category(video_url, timeout)
        if category:
            return category
        print(f"Retrying... ({attempt + 1}/{retries})")
        time.sleep(1)  # Optional: small delay between retries
    return None
