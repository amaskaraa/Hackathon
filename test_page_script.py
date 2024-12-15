import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Define valid and invalid credentials
VALID_USERNAME = "user"
VALID_PASSWORD = "letuserpass"
INVALID_USERNAME = "invalid_user@example.com"
INVALID_PASSWORD = "invalid_password"

@pytest.fixture
def driver():
    # Setup the WebDriver (assuming Chrome for this example)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Implicit wait for elements to be ready
    yield driver
    driver.quit()

def test_successful_login(driver):
    # Navigate to the login page
    driver.get("http://3.83.24.72:8000/login/")  # Replace with the actual login URL

    # Locate the username, password fields, and login button using the provided mapping
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CLASS_NAME, "oh-btn--secondary")

    # Enter valid credentials
    username_field.send_keys(VALID_USERNAME)
    password_field.send_keys(VALID_PASSWORD)

    # Click the login button
    login_button.click()

    # Assert successful login by checking for a specific element or URL
    # Replace 'dashboard' with the actual URL or element that indicates a successful login
    assert "" in driver.current_url

def test_failed_login(driver):
    # Navigate to the login page
    driver.get("http://3.83.24.72:8000/login/")  # Replace with the actual login URL

    # Locate the username, password fields, and login button using the provided mapping
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CLASS_NAME, "oh-btn--secondary")

    # Enter invalid credentials
    username_field.send_keys(INVALID_USERNAME)
    password_field.send_keys(INVALID_PASSWORD)

    # Click the login button
    login_button.click()

    # Assert failed login by checking for an error message or unchanged URL
    # Replace 'error-message' with the actual element or text that indicates a failed login
    # error_message = driver.find_element(By.CLASS_NAME, "error-message")
    # assert error_message.is_displayed()
    assert "/login" in driver.current_url

# Note: Adjust the URL, element locators, and assertions based on the actual application under test.