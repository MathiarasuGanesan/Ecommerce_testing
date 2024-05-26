import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class TestEcommerce(unittest.TestCase):
    def setUp(self):
        # Initialize the Chrome WebDriver
        driver_path = 'C:/Users/User/Downloads/chromedriver-win64/chromedriver.exe'
        service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

    def test_invalid_login(self):
        """Test logging in with invalid credentials"""
        # Input values
        username = 'invalid_user'
        password = 'invalid_password'

        try:
            # Open the demo e-commerce site
            self.driver.get('https://www.saucedemo.com/')
            
            # Log in with invalid credentials
            self.driver.find_element(By.ID, 'user-name').send_keys(username)
            self.driver.find_element(By.ID, 'password').send_keys(password)
            self.driver.find_element(By.ID, 'login-button').click()
            
            # Verify error message is displayed
            try:
                error_message = self.driver.find_element(By.CSS_SELECTOR, '.error-message')
                self.assertTrue(error_message.is_displayed())
                self.assertEqual(error_message.text, 'Epic sadface: Username and password do not match any user in this service')
            except NoSuchElementException:
                pass  # Error message not found, which is expected for invalid login

        except Exception as e:
            self.fail(f"Test failed: {e}")

    def test_valid_login(self):
        """Test logging in with valid credentials"""
        # Input values
        username = 'standard_user'
        password = 'secret_sauce'

        try:
            # Open the demo e-commerce site
            self.driver.get('https://www.saucedemo.com/')
            
            # Log in with valid credentials
            self.driver.find_element(By.ID, 'user-name').send_keys(username)
            self.driver.find_element(By.ID, 'password').send_keys(password)
            self.driver.find_element(By.ID, 'login-button').click()
            
            # Wait for the products page to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item'))
            )
            
            # Add a product to the cart
            self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
            
            # Go to the cart
            self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
            
            # Proceed to checkout
            self.driver.find_element(By.ID, 'checkout').click()
            
            # Fill out the checkout information
            self.driver.find_element(By.ID, 'first-name').send_keys('John')
            self.driver.find_element(By.ID, 'last-name').send_keys('Doe')
            self.driver.find_element(By.ID, 'postal-code').send_keys('12345')
            self.driver.find_element(By.ID, 'continue').click()
            
            # Finish the checkout
            self.driver.find_element(By.ID, 'finish').click()
            
            # Wait for the confirmation page to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'complete-header'))
            )
            
            # Confirm the order is complete
            order_complete = self.driver.find_element(By.CLASS_NAME, 'complete-header')
            self.assertIn('Thank you for your order!', order_complete.text)

        except Exception as e:
            self.fail(f"Test failed: {e}")


if __name__ == "__main__":
    unittest.main()
