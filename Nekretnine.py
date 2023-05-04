from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

URL = 'https://www.nepremicnine.net/oglasi-prodaja/posest/kmetija/2/?s=3'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


class Nekretnine:

    def __init__(self):
        service = Service(r"C:\Users\Paki\Downloads\chromedriver_win32\chromedriver")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyButtonAccept"]').click()
        self.sva_sela = []
        self.sve_povrsine = []
        self.sve_cene = []
        self.svi_linkovi = []
        self.get_selo_names()
        self.get_povrsine()
        self.get_cene()
        self.get_linkovi()

    def get_selo_names(self):
        all_names = self.driver.find_elements(By.CLASS_NAME, "title")
        [self.sva_sela.append(name.text) for name in all_names if name.text.strip()]

    def get_povrsine(self):
        all_sizes = self.driver.find_elements(By.CLASS_NAME, "velikost")
        for size in all_sizes:
            size_list = size.text.strip().split(" ")[0].split(",")[0].split(".")
            try:
                real_size = int(size_list[0] + size_list[1]) / 10000
                self.sve_povrsine.append(real_size)
            except IndexError:
                real_size = int(size_list[0]) / 10000
                self.sve_povrsine.append(real_size)

    def get_cene(self):
        all_prices = self.driver.find_elements(By.CLASS_NAME, "cena")
        [self.sve_cene.append(cena.text) for cena in all_prices if cena.text.strip()]

    def get_linkovi(self):
        links = self.driver.find_elements(By.CLASS_NAME, 'slika')
        [self.svi_linkovi.append(link.get_attribute("href")) for link in links]


