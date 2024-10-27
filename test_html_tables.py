from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Data:
    url = "https://tablepress.org/demo/"

class AutomateTables:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start_automation(self):
        self.driver.get(Data().url)
        self.driver.maximize_window()
        sleep(5)

    def fetch_firstname_rowdata(self):
        # empty result list to store the row data
        result = []
        firstname_data = self.driver.find_elements(by=By.XPATH, value='//tbody[@class="row-hover"]/tr/td[1]')
        for data in firstname_data:
            result.append(data.text)
        return result
    
    def row_count(self):
        rows = self.driver.find_elements(by=By.XPATH, value='//tbody[@class="row-hover"]/tr')
        return len(rows)
    
    def column_count(self):
        columns = self.driver.find_elements(by=By.XPATH, value='//tr[@class="row-2 even"]/td')
        return len(columns)

    def shutdown(self):
        self.driver.close()

html_table = AutomateTables()
html_table.start_automation()
print(html_table.fetch_firstname_rowdata())
print(html_table.row_count())
print(html_table.column_count())
html_table.shutdown()



