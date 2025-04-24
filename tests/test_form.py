import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from configs.config import BASE_URL, FORM_PATH
import requests
from time import sleep
from utils.color_utils import is_red_border


# ----------------- Positive Test -----------------
def test_valid_form_submission(form_page):
    """Verify that a fully filled valid form is submitted successfully."""
    form_page.driver.get(BASE_URL + FORM_PATH)
    form_page.fill_first_name("John")
    form_page.fill_last_name("Doe")
    form_page.fill_email("john.doe@example.com")
    form_page.select_gender("Male")
    form_page.fill_mobile("1234567890")
    form_page.set_dob("24 Apr 1990")
    form_page.fill_subjects("Math")
    form_page.select_hobby("Reading")
    form_page.upload_file("sample_pic.png")  # Make sure this file exists in /assets
    form_page.fill_address("123 Automation Lane")
    form_page.select_state_and_city("NCR", "Delhi")
    form_page.submit()
    assert form_page.get_confirmation_text() == "Thanks for submitting the form"


def test_invalid_email_shows_error(form_page):
    form_page.driver.get(BASE_URL + FORM_PATH)
    form_page.fill_email("not-an-email")
    form_page.fill_first_name("John")  # enables the submit button

    # Trigger validation by submitting
    form_page.scroll_to_element((By.ID, "submit"))
    form_page.click((By.ID, "submit"))

    # Now check the border
    form_page.scroll_to_element((By.ID, "userEmail"))
    email_input = form_page.driver.find_element(By.ID, "userEmail")
    border_color = email_input.value_of_css_property("border-color")
    sleep(5)
    assert is_red_border(border_color), f"Expected red border, got {border_color}"


# ----------------- Bonus Test: Integrity of all links -----------------
def test_all_site_links_are_working(driver):
    """Bonus: Visit every accessible page from homepage and validate it's not 404/500."""
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
