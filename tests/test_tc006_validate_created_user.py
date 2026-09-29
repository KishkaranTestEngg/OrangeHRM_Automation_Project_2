import pytest
import time
from selenium import webdriver

from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.admin_page import AdminPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


def test_tc006_validate_created_user(driver):

    # Open OrangeHRM
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Login as Admin
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    # Navigate to Admin
    home_page = HomePage(driver)
    home_page.click_admin()

    # Create a new user
    admin_page = AdminPage(driver)
    admin_page.click_add()

    # Select User Role
    admin_page.select_user_role("ESS")

    # Select Employee
    admin_page.select_employee()

    # Generate unique username
    username = f"tc006user{int(time.time())}"
    password = "Test@12345"

    # Enter username
    admin_page.enter_username(username)

    # Select status
    admin_page.select_status("Enabled")

    # Enter password
    admin_page.enter_password(password)

    # Confirm password
    admin_page.enter_confirm_password(password)

    # Save user
    admin_page.click_save()

    # Verify user was created
    assert admin_page.is_user_created_successfully()

    # Navigate back to User List
    home_page.click_admin()

    # Search for the newly created user
    admin_page.search_user(username)

    # Verify newly created user is present in User List
    assert admin_page.is_user_present_in_list(username)

    print(f"\nTC006 Passed - User '{username}' is present in Admin User List.")