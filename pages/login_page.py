from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//p[contains(normalize-space(), 'Forgot your password?')]")
    RESET_PASSWORD_BUTTON = (By.XPATH, "//button[normalize-space()='Reset Password']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def enter_username(self, username):
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_username_visible(self):
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )
        return username_field.is_displayed()

    def is_username_enabled(self):
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )
        return username_field.is_enabled()

    def is_password_visible(self):
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        return password_field.is_displayed()

    def is_password_enabled(self):
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        return password_field.is_enabled()

    def click_forgot_password(self):
        forgot_password_link = self.wait.until(
            EC.element_to_be_clickable(self.FORGOT_PASSWORD_LINK)
        )
        forgot_password_link.click()

    def click_reset_password(self):
        self.wait.until(
            EC.element_to_be_clickable(self.RESET_PASSWORD_BUTTON)
        ).click()

    def is_reset_password_page_displayed(self):
        return "requestPasswordResetCode" in self.driver.current_url

    def enter_reset_username(self, username):
        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        ).clear()

        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)