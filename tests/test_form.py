import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from configs.config import BASE_URL, FORM_PATH
import requests
from time import sleep
from utils.color_utils import is_red_border
from business_flows.site_validation import check_all_internal_links


# ----------------- Positive Test -----------------
def test_valid_form_submission(form_page):
    form_page.fill_form_valid_data()
    assert form_page.was_form_submitted_successfully()

# ----------------- Negative Test -----------------
def test_invalid_email_red_border(form_page):
    form_page.fill_form_invalid_email()
    assert form_page.is_email_field_red_bordered()

# ----------------- Bonus Test: Integrity of all links -----------------
def test_all_site_links_are_working(driver):
    check_all_internal_links(driver)
