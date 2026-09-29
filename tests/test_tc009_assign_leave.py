from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_tc009_assign_leave(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    # Login as Admin
    login_page.login("Admin", "admin123")

    # Navigate to Leave
    home_page.click_leave()

    # Open Assign Leave
    home_page.click_assign_leave()

    # Enter and select employee
    home_page.enter_employee_name("Qwerty Qwerty LName")
    home_page.select_employee()

    # Select Leave Type
    home_page.select_leave_type()

    # Enter Leave Dates
    home_page.enter_from_date("2026-28-09")
    home_page.enter_to_date("2026-29-09")

    # Click Assign
    home_page.click_assign()

    # Verify confirmation message
    home_page.verify_confirm_leave_message()

    # Confirm leave assignment
    home_page.click_confirm_ok()