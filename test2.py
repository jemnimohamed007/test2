from selenium import webdriver
import time

url = "https://faucetearner.org/faucet.php"
button_xpath = '//*[@id="body"]/div[1]/div[3]/div[2]/div/div[4]/div[1]/form/button'

# Set up the webdriver (make sure to download the appropriate driver for your browser)
driver = webdriver.Chrome()

# Open the website
driver.get(url)

# Function to click the button every minute
def click_button_every_minute():
    while True:
        # Find the button and click it
        button = driver.find_element_by_xpath(button_xpath)
        button.click()

        # Wait for one minute
        time.sleep(70)

# Call the function
click_button_every_minute()
