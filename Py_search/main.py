import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def search_google():
    try:
        # Specify the path to the chromedriver executable
        driver = webdriver.Chrome(executable_path='C:/Users/User/Downloads/chromedriver-win64/chromedriver.exe') 
        
        # Open Google
        driver.get('https://www.google.com')

        # Find the search box using its name attribute value
        search_box = driver.find_element('name', 'q')

        # Send the search query to the search box
        search_box.send_keys('abc')

        # Simulate pressing the Enter key
        search_box.send_keys(Keys.RETURN)

        # Wait for a few seconds to see the results
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()

# Run the function
search_google()
