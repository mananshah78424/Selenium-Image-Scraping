import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_image_urls(search_term, num_pages):
    # Start a new Chrome browser session
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode (without opening a browser window)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    image_urls = []
    
    for page in range(1, num_pages + 1):
        search_url = f"https://www.gettyimages.com/photos/{search_term}?page={page}"
        driver.get(search_url)
        
        # Give the page time to load images (adjust time if needed)
        time.sleep(3)
        
        # Find all image elements by their tag name
        images = driver.find_elements(By.TAG_NAME, "img")
        
        for img in images:
            img_url = img.get_attribute("src")
            if img_url and "https" in img_url:
                image_urls.append(img_url)
        
        print(f"Fetched {len(images)} images from page {page}")
    
    # Close the browser session
    driver.quit()
    
    return image_urls

# Example usage
search_term = "nature"
num_pages = 3
image_urls = get_image_urls(search_term, num_pages)

# Print fetched URLs
for url in image_urls:
    print(url)
