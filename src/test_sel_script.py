import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin:

    def setup_method(self):
        self.driver = webdriver.Chrome()


    def test_login_positive(self):
        driver = self.driver

        driver.get("http://3.83.24.72:8000/login/?next=/")

        username = driver.find_element(By.ID,"username")
        username.send_keys("admin")

        username = driver.find_element(By.ID,"password")
        username.send_keys("password")

        submit = driver.find_element(By.ID,"submit-button")
        submit.click()

        expected_text = "Login successful"
        actual_text = driver.find_element(By.ID,"result").text

        assert actual_text==expected_text,"Login should be successful but is not"

        time.sleep(5)

    def test_login_negative(self):
        driver = self.driver

        driver.get("http://3.83.24.72:8000/login/?next=/")

        username = driver.find_element(By.ID,"username")
        username.send_keys("admin")

        username = driver.find_element(By.ID,"password")
        username.send_keys("111")

        submit = driver.find_element(By.ID,"submit-button")
        submit.click()

        expected_text = "Login failed"
        actual_text = driver.find_element(By.ID,"result").text

        assert actual_text==expected_text,"Login should fail, but dit not"

        time.sleep(5)

    def teardown_method(self):
        self.driver.quit()