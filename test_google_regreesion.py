import pytest
from pages.google_page import GooglePage
@pytest.mark.regression
def test_google_regression(driver):
    google=GooglePage()
    google.open(driver)
    title=google.get_title(driver)
    assert title == "Google"
    assert len(title) > 3


