from selenium import webdriver
from time import sleep
import pytest
import subprocess
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    # Start Streamlit in the background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])
    options = Options()
    options.headless = True  # Run in headless mode (it won't show the ui to the user)
    driver = webdriver.Chrome(options=options)
    # Start the WebDriver using GeckoDriver
    driver.set_page_load_timeout(5)
    yield driver

    # Close the WebDriver and Streamlit after test
    driver.quit()
    process.kill()

def test_app_opens(driver):
    # Check if the page is open
    driver.get("http://localhost:8501")
    sleep(5)

def test_check_title_is(driver):
    # Check if the page is open
    driver.get("http://localhost:8501")
    # Check if the page title is
    sleep(2)
    # Catch the page title
    page_title = driver.title

    # Check if the page title is like below
    expected_title = "Excel schema validator"
    assert page_title == expected_title

def test_check_streamlit_h1(driver):
    # Open the streamlit page
    driver.get("http://localhost:8501")
    # Wait before to execute the next step
    sleep(2)

    # Catch the fisrt element <h1> of page
    h1_element = driver.find_element(By.TAG_NAME, "h1")

    # Check if the element text is like below
    expected_text = "Upload your Excel file here"
    assert h1_element.text == expected_text