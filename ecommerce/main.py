import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your ChromeDriver
driver_path = 'C:/Users/User/Downloads/chromedriver-win64/chromedriver.exe'
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Open the demo e-commerce site
    driver.get('https://www.saucedemo.com/')
    
    # Log in to the site
    username = driver.find_element(By.ID, 'user-name')
    password = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.ID, 'login-button')
    
    username.send_keys('standard_user')
    password.send_keys('secret_sauce')
    login_button.click()
    
    # Wait for the products page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item'))
    )
    
    # Add a product to the cart
    add_to_cart_button = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    add_to_cart_button.click()
    
    # Go to the cart
    cart_icon = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_icon.click()
    
    # Wait for the cart page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'cart_item'))
    )
    
    # Proceed to checkout
    checkout_button = driver.find_element(By.ID, 'checkout')
    checkout_button.click()
    
    # Fill out the checkout information
    first_name = driver.find_element(By.ID, 'first-name')
    last_name = driver.find_element(By.ID, 'last-name')
    postal_code = driver.find_element(By.ID, 'postal-code')
    continue_button = driver.find_element(By.ID, 'continue')
    
    first_name.send_keys('John')
    last_name.send_keys('Doe')
    postal_code.send_keys('12345')
    continue_button.click()
    
    # Finish the checkout
    finish_button = driver.find_element(By.ID, 'finish')
    finish_button.click()
    
    # Wait for the confirmation page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'complete-header'))
    )
    
    # Confirm the order is complete
    order_complete = driver.find_element(By.CLASS_NAME, 'complete-header')
    assert 'THANK YOU FOR YOUR ORDER' in order_complete.text

    print("Test Passed: Order was completed successfully.")
      
except AssertionError as e:
    print(f"Test Failed: {e}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()

