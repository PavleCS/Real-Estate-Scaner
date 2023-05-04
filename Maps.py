from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException


MAPS = "https://www.google.com/maps/"
CAPITALS = ["Ljubljana", "Maribor"]

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

class Maps:

    def __init__(self):
        service = Service(r"C:\Users\Paki\Downloads\chromedriver_win32\chromedriver")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.results = dict()


    def get_map_info(self, city):
        self.driver.get(MAPS)
        if city not in self.results:
            self.results[city] = []
        self.driver.find_element(By.XPATH, '//*[@id="searchboxinput"]').send_keys(f"{city} slovenija")
        self.driver.find_element(By.XPATH, '//*[@id="searchboxinput"]').send_keys(Keys.ENTER)
        sleep(7)
        try:
            self.driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button/span/img').click()
            sleep(7)
            for capital in CAPITALS:
                self.driver.find_element(By.XPATH, '//*[@id="sb_ifc51"]/input').clear()
                self.driver.find_element(By.XPATH, '//*[@id="sb_ifc51"]/input').send_keys(capital)
                self.driver.find_element(By.XPATH, '//*[@id="sb_ifc51"]/input').send_keys(Keys.ENTER)
                sleep(7)
                total_time = self.driver.find_element(By.XPATH,
                                                      '//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[1]/span[1]')
                self.results[city].append({capital: total_time.text})
                sleep(7)
        except NoSuchElementException:
            print(f"Nema lokacije za {city}")

