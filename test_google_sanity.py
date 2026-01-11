import pytest
from pages.google_page import GooglePage
@pytest.mark.sanity
def test_google_title(driver):
    google=GooglePage()
    google.open(driver)
    title=google.get_title(driver)
    assert title == "Google"

