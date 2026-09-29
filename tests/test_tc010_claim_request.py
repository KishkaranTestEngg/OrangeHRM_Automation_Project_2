from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_tc010_claim_request(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    # Login as Admin
    login_page.login("Admin", "admin123")

    # Navigate to Claim
    home_page.click_claim()

    # Open Assign Claim
    home_page.click_assign_claim()

    # Enter and select employee
    home_page.enter_employee_name("Qwerty")
    home_page.select_employee()

    # Select Event
    home_page.select_event()

    # Select Currency
    home_page.select_currency()

    # Enter Remarks
    home_page.enter_remarks("Test Claim Request")