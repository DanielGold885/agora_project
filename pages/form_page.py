# pages/form_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

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
