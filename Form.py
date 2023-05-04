from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

URL = 'https://forms.gle/mwzYeRpMTuy9mQNKA'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


class Form:

    def __init__(self):
        service = Service(r"C:\Users\Paki\Downloads\chromedriver_win32\chromedriver")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def fill_form(self, selo, cena, povrsina, link, dist_ljub, dist_mar):
        self.driver.get(URL)
        sleep(2)
        selo_ = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        selo_.click()
        selo_.send_keys(selo)
        cena_ = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        cena_.click()
        cena_.send_keys(cena)
        povrsina_ = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        povrsina_.click()
        povrsina_.send_keys(povrsina)
        link_ = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_.click()
        link_.send_keys(link)
        ljub = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
        ljub.click()
        ljub.send_keys(dist_ljub)
        mar = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
        mar.click()
        mar.send_keys(dist_mar)
        self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()