from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:

    ADD_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Add']"
    )

    USER_ROLE_DROPDOWN = (
        By.XPATH,
        "//label[normalize-space()='User Role']/following::div[contains(@class,'oxd-select-text')][1]"
    )

    EMPLOYEE_NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='Type for hints...']"
    )

    USERNAME_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Username']/following::input[1]"
    )

    STATUS_DROPDOWN = (
        By.XPATH,
        "//label[normalize-space()='Status']/following::div[contains(@class,'oxd-select-text')][1]"
    )

    PASSWORD_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Password']/following::input[1]"
    )

    CONFIRM_PASSWORD_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Confirm Password']/following::input[1]"
    )

    SAVE_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Save']"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//div[contains(@class,'oxd-toast-content')]"
    )

    # TC006 - User List
    USERNAME_SEARCH_INPUT = (
        By.XPATH,
        "//label[normalize-space()='Username']/following::input[1]"
    )

    SEARCH_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Search']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def click_add(self):
        add_button = self.wait.until(
            EC.element_to_be_clickable(self.ADD_BUTTON)
        )
        add_button.click()

    def select_user_role(self, role):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.USER_ROLE_DROPDOWN)
        )
        dropdown.click()

        option = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[@role='option']//span[normalize-space()='{role}']"
                )
            )
        )
        option.click()

    def enter_employee_name(self, employee_name):
        employee_input = self.wait.until(
            EC.visibility_of_element_located(self.EMPLOYEE_NAME_INPUT)
        )
        employee_input.clear()
        employee_input.send_keys(employee_name)

    def enter_username(self, username):
        username_input = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )
        username_input.clear()
        username_input.send_keys(username)

    def select_status(self, status):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.STATUS_DROPDOWN)
        )
        dropdown.click()

        option = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[@role='option']//span[normalize-space()='{status}']"
                )
            )
        )
        option.click()

    def enter_password(self, password):
        password_input = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )
        password_input.clear()
        password_input.send_keys(password)

    def enter_confirm_password(self, password):
        confirm_password_input = self.wait.until(
            EC.visibility_of_element_located(self.CONFIRM_PASSWORD_INPUT)
        )
        confirm_password_input.clear()
        confirm_password_input.send_keys(password)

    def click_save(self):
        save_button = self.wait.until(
            EC.element_to_be_clickable(self.SAVE_BUTTON)
        )
        save_button.click()

    def select_employee(self):
        employee_input = self.wait.until(
            EC.visibility_of_element_located(self.EMPLOYEE_NAME_INPUT)
        )

        employee_input.clear()
        employee_input.send_keys("a")

        # Wait until searching is completed
        self.wait.until(
            lambda driver: "Searching...." not in driver.find_element(
                By.XPATH,
                "//div[contains(@class,'oxd-autocomplete-dropdown')]"
            ).text
        )

        # Get available employee options
        options = self.driver.find_elements(
            By.XPATH,
            "//div[contains(@class,'oxd-autocomplete-option')]"
        )

        print("\nEmployee suggestions:")

        for option in options:
            print(" -", option.text)

        # Select the first real employee result
        for option in options:
            if option.text.strip() and option.text.strip() != "No Records Found":
                print("Selected employee:", option.text)
                option.click()
                return

        raise AssertionError("No employee was available for selection.")

    def is_user_created_successfully(self):
        success_message = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )
        print("\nSuccess message:", success_message.text)
        return success_message.is_displayed()

    # TC006 - Search newly created user

    def search_user(self, username):
        username_input = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_SEARCH_INPUT)
        )

        username_input.clear()
        username_input.send_keys(username)

        search_button = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )

        search_button.click()

    def is_user_present_in_list(self, username):
        user = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//div[contains(@class,'oxd-table-body')]"
                    f"//div[contains(@class,'oxd-table-row')]"
                    f"//*[normalize-space()='{username}']"
                )
            )
        )

        return user.is_displayed()