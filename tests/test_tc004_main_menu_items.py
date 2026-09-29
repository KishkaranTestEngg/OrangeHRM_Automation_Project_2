import pytest

from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.fixture
def driver():
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


def test_tc004_main_menu_items(driver):

    # Open OrangeHRM login page
    driver.get("https://opensource-demo.orangehrmlive.com/")

    # Login with valid credentials
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    # Create HomePage object
    home_page = HomePage(driver)

    # Verify Admin menu visibility and clickability
    assert home_page.is_menu_visible(home_page.ADMIN_MENU)
    home_page.click_menu(home_page.ADMIN_MENU)

    # Navigate back to Dashboard
    driver.back()

    # Verify PIM menu visibility and clickability
    assert home_page.is_menu_visible(home_page.PIM_MENU)
    home_page.click_menu(home_page.PIM_MENU)

    # Navigate back to Dashboard
    driver.back()

    # Verify Leave menu visibility and clickability
    assert home_page.is_menu_visible(home_page.LEAVE_MENU)
    home_page.click_menu(home_page.LEAVE_MENU)

    # Navigate back to Dashboard
    driver.back()

    # Verify Time menu visibility and clickability
    assert home_page.is_menu_visible(home_page.TIME_MENU)
    home_page.click_menu(home_page.TIME_MENU)

    # Navigate back to Dashboard
    driver.back()

    # Verify Recruitment menu visibility and clickability
    assert home_page.is_menu_visible(home_page.RECRUITMENT_MENU)
    home_page.click_menu(home_page.RECRUITMENT_MENU)

    # Navigate back to Dashboard
    driver.back()

    # Verify My Info menu visibility and clickability
    assert home_page.is_menu_visible(home_page.MY_INFO_MENU)
    home_page.click_menu(home_page.MY_INFO_MENU)

    # Navigate back to Dashboard
    driver.back()

    # Verify Performance menu visibility and clickability
    assert home_page.is_menu_visible(home_page.PERFORMANCE_MENU)
    home_page.click_menu(home_page.PERFORMANCE_MENU)

    # Navigate back to Dashboard
    driver.back()

    # Verify Dashboard menu visibility and clickability
    assert home_page.is_menu_visible(home_page.DASHBOARD_MENU)
    home_page.click_menu(home_page.DASHBOARD_MENU)
