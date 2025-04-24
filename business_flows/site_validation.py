import requests
from selenium.webdriver.common.by import By
from configs.config import BASE_URL

def check_all_internal_links(driver):
    driver.get(BASE_URL)
    links = driver.find_elements(By.XPATH, "//a[@href]")
    unique_urls = set()

    for link in links:
        href = link.get_attribute("href")
        if href and href.startswith(BASE_URL):
            unique_urls.add(href)

    assert unique_urls, "No internal links found on homepage!"

    errors = []
    for url in unique_urls:
        try:
            response = requests.get(url)
            if response.status_code >= 400:
                errors.append((url, response.status_code))
        except Exception as e:
            errors.append((url, str(e)))

    assert not errors, f"Broken links found: {errors}"
