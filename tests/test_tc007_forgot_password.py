import pytest
from pages.login_page import LoginPage


def test_tc007_forgot_password_navigation(driver):
    login_page = LoginPage(driver)

    # Click Forgot your password?
    login_page.click_forgot_password()

    # Verify Reset Password page is displayed
    assert login_page.is_reset_password_page_displayed()

    # Enter registered username
    login_page.enter_reset_username("Admin")

    # Click Reset Password
    login_page.click_reset_password()