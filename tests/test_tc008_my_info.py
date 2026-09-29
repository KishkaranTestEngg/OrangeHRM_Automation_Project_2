from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_tc008_my_info_menu(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    # Login to OrangeHRM
    login_page.login("Admin", "admin123")

    # Verify My Info menu is visible
    assert home_page.is_menu_visible(home_page.MY_INFO_MENU)

    # Click My Info
    home_page.click_my_info()

    # Verify Personal Details is visible and clickable
    assert home_page.is_menu_visible(home_page.PERSONAL_DETAILS_MENU)
    home_page.click_personal_details()

    # Verify Personal Details page is opened
    assert home_page.is_personal_details_page_displayed()

    # Navigate back to My Info
    home_page.click_my_info()

    # Verify Contact Details is visible and clickable
    assert home_page.is_menu_visible(home_page.CONTACT_DETAILS_MENU)
    home_page.click_contact_details()

    # Verify Contact Details page is opened
    assert home_page.is_contact_details_page_displayed()

    # Verify Emergency Contacts is visible and clickable
    assert home_page.is_menu_visible(home_page.EMERGENCY_CONTACTS_MENU)
    home_page.click_emergency_contacts()

    # Verify Emergency Contacts page is opened
    assert home_page.is_emergency_contacts_page_displayed()