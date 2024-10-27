from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Data:
    url = "https://www.saucedemo.com/v1/index.html"
    username = "standard_user"
    password = "secret_sauce"

class SwagAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start_automation(self):
        self.driver.get(Data().url)
        self.driver.maximize_window()
        sleep(5)

    def shutdown(self):
        self.driver.close()

    def validate_login(self):
        # enter the username
        self.driver.find_element(by=By.XPATH, value='//input[@id="user-name"]').send_keys(Data().username)

        # enter the password
        self.driver.find_element(by=By.XPATH, value='//input[@id="password"]').send_keys(Data().password)

        # click the login button
        self.driver.find_element(by=By.XPATH, value='//input[@id="login-button"]').click()
        sleep(5)

        # validate the products text in the homepage
        product_text = self.driver.find_element(by=By.XPATH, value='//div[contains(text(), "Products")]').text

        # asserting to validate the text
        assert product_text == "Products"

        print("SUCCESS : Test Passed")


automationSwag = SwagAutomation()
automationSwag.start_automation()
automationSwag.validate_login()
automationSwag.shutdown()
    