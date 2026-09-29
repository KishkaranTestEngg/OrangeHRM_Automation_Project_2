import pytest

from pages.login_page import LoginPage
from utils.excel_utils import read_login_test_data


login_test_data = read_login_test_data()


@pytest.mark.parametrize(
    "data",
    login_test_data
)
def test_tc001_login_with_multiple_credentials(driver, data):

    driver.get("https://opensource-demo.orangehrmlive.com/")

    login_page = LoginPage(driver)

    login_page.login(
        data["username"],
        data["password"]
    )

    print(f"Test ID: {data['test_id']}")
    print(f"Username: {data['username']}")
    print(f"Current URL: {driver.current_url}")