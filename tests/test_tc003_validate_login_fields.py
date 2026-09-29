from pages.login_page import LoginPage


def test_tc003_validate_login_fields(driver):

    login_page = LoginPage(driver)

    assert login_page.is_username_visible()
    assert login_page.is_username_enabled()

    assert login_page.is_password_visible()
    assert login_page.is_password_enabled()