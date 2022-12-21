import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from fixture.gift import GiftCard
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension",
                                        False)  # Adding Argument to Not Use Automation Extension
        options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Excluding enable-automation Switch
        options.add_argument("disable-popup-blocking")
        options.add_argument("disable-notifications")
        options.add_argument("disable-gpu")  ##renderer timeout
        self.driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride',
                                    {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                  'Chrome/85.0.4183.102 Safari/537.36'})
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.session = SessionHelper(self)
        self.gift = GiftCard(self)



    def destroy(self):
        self.driver.quit()