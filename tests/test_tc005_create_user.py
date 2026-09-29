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


def test_tc005_create_user(driver):

    # Open OrangeHRM
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Login as Admin
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    # Navigate to Admin
    home_page = HomePage(driver)
    home_page.click_admin()

    # Click Add
    admin_page = AdminPage(driver)
    admin_page.click_add()

    # Select User Role
    admin_page.select_user_role("ESS")

    #select the employee
    admin_page.select_employee()


    # Generate a unique username
    username = f"test user{int(time.time())}"
    password = "Test@12345"

    # Enter username
    admin_page.enter_username(username)

    # Select status
    admin_page.select_status("Enabled")

    # Enter password
    admin_page.enter_password(password)

    # Confirm password
    admin_page.enter_confirm_password(password)

    # Save the new user
    admin_page.click_save()

    # Verify user creation
    assert admin_page.is_user_created_successfully()

    # Logout from Admin account
    home_page.logout()

    # Verify that user is redirected to the login page
    assert "login" in driver.current_url.lower()

    # Login with newly created user
    login_page.login(username, password)

    # Verify successful login
    assert home_page.is_menu_visible(home_page.DASHBOARD_MENU)