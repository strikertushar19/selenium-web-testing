import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
class PinpointTestCase(unittest.TestCase):

    def setUp(self):
        service = Service('/snap/bin/geckodriver') # this path if you install geckodriver from snap command in ubuntu
        self.browser = webdriver.Firefox(service=service)
        self.addCleanup(self.browser.quit)  

    def test_login(self):
        try:
            login_url = "Put_your_desired_website_url"
            self.browser.get(login_url)


            #  XPath  is defined for login buttton
            login_button = self.browser.find_element(By.XPATH, "//body/div[@id='root']/div[1]/nav[1]/div[1]/div[1]/ul[1]/li[4]/a[1]")
            login_button.click()

            #xpath defined for the input fields on login page
            username_field = self.browser.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")  # Update if necessary
            password_field = self.browser.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/div[2]/div[1]/input[1]")  # Update if necessary
           
            # Invalid input credentials defined
            username_field.send_keys("your_email@example.com")
            password_field.send_keys("ajhgkahgahka")

            login_submit_button = self.browser.find_element(By.XPATH, "//button[contains(text(),'Sign In')]")
            login_submit_button.click()
            time.sleep(4)  # this is to make sure that you can see the error invalid credentails


        except Exception as e:
            self.fail(f"Test encountered an exception: {e}")

    def tearDown(self):
        # Ensure the browser quits after the test freeing up resources.
        if hasattr(self, 'browser'):
            self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
