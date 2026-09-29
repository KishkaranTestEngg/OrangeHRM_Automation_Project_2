def test_tc002_home_url(driver):

    driver.get("https://opensource-demo.orangehrmlive.com")

    assert "orangehrm" in driver.current_url.lower()