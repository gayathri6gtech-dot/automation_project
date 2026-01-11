import pytest
from pages.google_page import GooglePage
@pytest.mark.smoke
def test_google_title(driver):
    google=GooglePage()
    google.open(driver)
    assert "Google" in google.get_title(driver)

