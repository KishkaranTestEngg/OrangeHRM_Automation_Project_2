from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class HomePage:

    ADMIN_MENU = (By.XPATH, "//span[text()='Admin']")
    PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    LEAVE_MENU = (By.XPATH, "//span[text()='Leave']")
    CLAIM_MENU = (By.XPATH, "//span[normalize-space()='Claim']")
    ASSIGN_CLAIM = (By.XPATH, "//a[normalize-space()='Assign Claim']")
    ASSIGN_LEAVE_MENU = (By.XPATH, "//a[normalize-space()='Assign Leave']")
    EMPLOYEE_NAME_INPUT = (By.XPATH,"//label[normalize-space()='Employee Name']/following::input[1]")
    EMPLOYEE_SUGGESTION = (By.XPATH, "//div[@role='option' and contains(., 'Qwerty Qwerty LName')]")
    LEAVE_TYPE_DROPDOWN = (By.XPATH,"//label[normalize-space()='Leave Type']/following::div[contains(@class,'oxd-select-text')][1]")
    LEAVE_TYPE_OPTION = (By.XPATH, "//div[@role='option'][normalize-space()='CAN - Vacation']")
    FROM_DATE_INPUT = (By.XPATH,"//label[normalize-space()='From Date']/following::input[1]")
    TO_DATE_INPUT = ( By.XPATH,"//label[normalize-space()='To Date']/following::input[1]")
    ASSIGN_BUTTON = (By.XPATH,"//button[normalize-space()='Assign']")
    CURRENCY_DROPDOWN = (By.XPATH, "//label[normalize-space()='Currency']/following::div[contains(@class,'oxd-select-text')][1]")
    CURRENCY_OPTION = (By.XPATH, "//div[@role='option'][normalize-space()='Indian Rupee']")
    EVENT_DROPDOWN = (By.XPATH,"//label[normalize-space()='Event']/following::div[contains(@class,'oxd-select-text')][1]")
    EVENT_OPTION = (By.XPATH, "//div[@role='option'][normalize-space()='Travel Allowance']")
    REMARKS_INPUT = (By.XPATH, "//label[normalize-space()='Remarks']/following::textarea[1]")
    CREATE_BUTTON = (By.XPATH, "//button[normalize-space()='Create']")
    STATUS_INITIATED = (By.XPATH, "//*[normalize-space()='Initiated']")
    CONFIRM_LEAVE_MESSAGE = (By.XPATH, '//*[contains(normalize-space(), "Employee doesn\'t have the sufficient leave balance")]')
    CONFIRM_OK_BUTTON = (By.XPATH, "//button[normalize-space()='Ok']")
    TIME_MENU = (By.XPATH, "//span[text()='Time']")
    RECRUITMENT_MENU = (By.XPATH, "//span[text()='Recruitment']")
    MY_INFO_MENU = (By.XPATH, "//span[text()='My Info']")
    PERSONAL_DETAILS_MENU = (By.XPATH, "//a[normalize-space()='Personal Details']")
    PERSONAL_DETAILS_HEADING = (By.XPATH, "//h6[normalize-space()='Personal Details']")
    CONTACT_DETAILS_MENU = (By.XPATH, "//a[normalize-space()='Contact Details']")
    CONTACT_DETAILS_HEADING = (By.XPATH, "//h6[normalize-space()='Contact Details']")
    EMERGENCY_CONTACTS_MENU = (By.XPATH, "//a[normalize-space()='Emergency Contacts']")
    EMERGENCY_CONTACTS_HEADING = (By.XPATH,"//h6[normalize-space()='Assigned Emergency Contacts']")
    DASHBOARD_MENU = (By.XPATH, "//span[text()='Dashboard']")
    LOGOUT_MENU = (
        By.XPATH,
        "//a[normalize-space()='Logout']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def is_menu_visible(self, menu_locator):
        menu = self.wait.until(
            EC.visibility_of_element_located(menu_locator)
        )
        return menu.is_displayed()

    def click_menu(self, menu_locator):
        menu = self.wait.until(
            EC.element_to_be_clickable(menu_locator)
        )
        menu.click()

    def click_admin(self):
        admin_menu = self.wait.until(
            EC.element_to_be_clickable(self.ADMIN_MENU)
        )
        admin_menu.click()

    def click_claim(self):
        claim_menu = self.wait.until(
            EC.element_to_be_clickable(self.CLAIM_MENU)
        )
        claim_menu.click()

    def click_assign_claim(self):
        assign_claim = self.wait.until(
            EC.element_to_be_clickable(self.ASSIGN_CLAIM)
        )
        assign_claim.click()

    def click_leave(self):
        leave_menu = self.wait.until(
            EC.element_to_be_clickable(self.LEAVE_MENU)
        )
        leave_menu.click()

    def click_assign_leave(self):
        assign_leave = self.wait.until(
            EC.element_to_be_clickable(self.ASSIGN_LEAVE_MENU)
        )
        assign_leave.click()

    def select_currency(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.CURRENCY_DROPDOWN)
        )
        dropdown.click()

        currency = self.wait.until(
            EC.element_to_be_clickable(self.CURRENCY_OPTION)
        )
        currency.click()

    def select_event(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.EVENT_DROPDOWN)
        )
        dropdown.click()

        event = self.wait.until(
            EC.element_to_be_clickable(self.EVENT_OPTION)
        )
        event.click()

    def enter_remarks(self, remarks):
        remarks_input = self.wait.until(
            EC.visibility_of_element_located(self.REMARKS_INPUT)
        )
        remarks_input.clear()
        remarks_input.send_keys(remarks)

    def click_create(self):
        create_button = self.wait.until(
            EC.element_to_be_clickable(self.CREATE_BUTTON)
        )
        create_button.click()

    def verify_initiated_status(self):
        status = self.wait.until(
            EC.visibility_of_element_located(self.STATUS_INITIATED)
        )
        assert status.is_displayed()
        assert status.text.strip() == "Initiated"

    def enter_employee_name(self, employee_name):
        employee_input = self.wait.until(
            EC.visibility_of_element_located(self.EMPLOYEE_NAME_INPUT)
        )
        employee_input.clear()
        employee_input.send_keys(employee_name)

    def select_employee(self):
        employee = self.wait.until(
            EC.element_to_be_clickable(self.EMPLOYEE_SUGGESTION)
        )
        employee.click()

    def select_leave_type(self):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.LEAVE_TYPE_DROPDOWN)
        )
        dropdown.click()

        leave_type = self.wait.until(
            EC.element_to_be_clickable(self.LEAVE_TYPE_OPTION)
        )
        leave_type.click()

    def enter_from_date(self, from_date):
        from_date_input = self.wait.until(
            EC.visibility_of_element_located(self.FROM_DATE_INPUT)
        )
        from_date_input.clear()
        from_date_input.send_keys(from_date)

    def enter_to_date(self, to_date):
        to_date_input = self.wait.until(
            EC.visibility_of_element_located(self.TO_DATE_INPUT)
        )
        to_date_input.click()
        to_date_input.send_keys(Keys.CONTROL, "a")
        to_date_input.send_keys(Keys.BACKSPACE)
        to_date_input.send_keys(to_date)

    def verify_confirm_leave_message(self):
        self.wait.until(
            EC.visibility_of_element_located(self.CONFIRM_OK_BUTTON)
        )

        body_text = self.driver.find_element(By.TAG_NAME, "body").text

        assert "sufficient leave balance" in body_text

    def click_assign(self):
        assign_button = self.wait.until(
            EC.element_to_be_clickable(self.ASSIGN_BUTTON)
        )
        assign_button.click()


    def click_confirm_ok(self):
        ok_button = self.wait.until(
            EC.element_to_be_clickable(self.CONFIRM_OK_BUTTON)
        )
        ok_button.click()



    def logout(self):
        # Open the user profile menu
        profile_menu = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(@class,'oxd-userdropdown-tab')]")
            )
        )
        profile_menu.click()

        # Click Logout
        logout_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT_MENU)
        )
        logout_button.click()

    def click_my_info(self):
        my_info_menu = self.wait.until(
            EC.element_to_be_clickable(self.MY_INFO_MENU)
        )
        my_info_menu.click()

    def click_personal_details(self):
        personal_details = self.wait.until(
            EC.element_to_be_clickable(self.PERSONAL_DETAILS_MENU)
        )
        personal_details.click()

    def click_contact_details(self):
        contact_details = self.wait.until(
            EC.element_to_be_clickable(self.CONTACT_DETAILS_MENU)
        )
        contact_details.click()

    def click_emergency_contacts(self):
        emergency_contacts = self.wait.until(
            EC.element_to_be_clickable(self.EMERGENCY_CONTACTS_MENU)
        )
        emergency_contacts.click()

    def is_personal_details_page_displayed(self):
        heading = self.wait.until(
            EC.visibility_of_element_located(self.PERSONAL_DETAILS_HEADING)
        )
        return heading.is_displayed()

    def is_contact_details_page_displayed(self):
        heading = self.wait.until(
            EC.visibility_of_element_located(self.CONTACT_DETAILS_HEADING)
        )
        return heading.is_displayed()

    def is_emergency_contacts_page_displayed(self):
        heading = self.wait.until(
            EC.visibility_of_element_located(self.EMERGENCY_CONTACTS_HEADING)
        )
        return heading.is_displayed()



