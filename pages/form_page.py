from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage
from configs.config import BASE_URL
from configs.config import FORM_PATH
from utils.color_utils import is_red_border


class FormPage(BasePage):
    # --- Locators ---
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By.XPATH, "//label[text()='Male']")
    GENDER_FEMALE = (By.XPATH, "//label[text()='Female']")
    GENDER_OTHER = (By.XPATH, "//label[text()='Other']")
    MOBILE = (By.ID, "userNumber")
    DOB = (By.ID, "dateOfBirthInput")
    SUBJECTS = (By.ID, "subjectsInput")
    HOBBIES_READING = (By.XPATH, "//label[text()='Reading']")
    UPLOAD_PICTURE = (By.ID, "uploadPicture")
    ADDRESS = (By.ID, "currentAddress")
    STATE = (By.ID, "react-select-3-input")
    CITY = (By.ID, "react-select-4-input")
    SUBMIT = (By.ID, "submit")
    CONFIRMATION_HEADER = (By.ID, "example-modal-sizes-title-lg")

    # --- Methods ---
    def load(self):
        self.driver.get(BASE_URL + FORM_PATH)

    def fill_first_name(self, name):
        self.fill(self.FIRST_NAME, name)

    def fill_last_name(self, name):
        self.fill(self.LAST_NAME, name)

    def fill_email(self, email):
        self.fill(self.EMAIL, email)

    def select_gender(self, gender):
        gender = gender.lower()
        if gender == "male":
            self.click(self.GENDER_MALE)
        elif gender == "female":
            self.click(self.GENDER_FEMALE)
        elif gender == "other":
            self.click(self.GENDER_OTHER)

    def fill_mobile(self, mobile):
        self.fill(self.MOBILE, mobile)

    def set_dob(self, dob_str):
        self.scroll_to_element(self.DOB)
        self.click(self.DOB)
        self.fill(self.DOB, dob_str)
        self.driver.find_element(*self.DOB).send_keys(Keys.ENTER)

    def fill_subjects(self, subject):
        self.fill(self.SUBJECTS, subject)
        self.driver.find_element(*self.SUBJECTS).send_keys(Keys.ENTER)

    def select_hobby(self, hobby="Reading"):
        if hobby.lower() == "reading":
            self.click(self.HOBBIES_READING)
        # Add more hobbies if needed

    def upload_file(self, filename):
        path = self.get_asset_path(filename)
        self.driver.find_element(*self.UPLOAD_PICTURE).send_keys(path)

    def fill_address(self, address):
        self.fill(self.ADDRESS, address)

    def select_state_and_city(self, state, city):
        self.fill(self.STATE, state)
        self.driver.find_element(*self.STATE).send_keys(Keys.ENTER)
        self.fill(self.CITY, city)
        self.driver.find_element(*self.CITY).send_keys(Keys.ENTER)

    def submit(self):
        self.scroll_to_element(self.SUBMIT)
        self.click(self.SUBMIT)

    def get_confirmation_text(self):
        return self.get_text(self.CONFIRMATION_HEADER)

    def fill_form_valid_data(self):
        self.fill_first_name("John")
        self.fill_last_name("Doe")
        self.fill_email("john.doe@example.com")
        self.select_gender("Male")
        self.fill_mobile("1234567890")
        self.set_dob("24 Apr 1990")
        self.fill_subjects("Math")
        self.select_hobby("Reading")
        self.upload_file("sample_pic.png")  # Make sure this file exists in /assets
        self.fill_address("123 Automation Lane")
        self.select_state_and_city("NCR", "Delhi")
        self.submit()

    def was_form_submitted_successfully(self):
        try:
            modal = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
            )
            return "Thanks for submitting the form" in modal.text
        except:
            return False

    def fill_form_invalid_email(self):
        self.fill_email("not-an-email")
        self.fill_first_name("John")
        self.scroll_to_element((By.ID, "submit"))
        self.click((By.ID, "submit"))
        self.scroll_to_element((By.ID, "userEmail"))
        self.submit()

    def is_email_field_red_bordered(self):
        email_input = self.driver.find_element(By.ID, "userEmail")
        border_color = email_input.value_of_css_property("border-color")
        return is_red_border(border_color)




