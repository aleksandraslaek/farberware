import time

from selenium.webdriver.common.by import By


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, credentials):
        self.app.driver.get("https://farberwarecookware.com/")
        self.app.driver.find_element(By.CSS_SELECTOR, ".site-header-right .site-header_account-link-text").click()
        self.app.driver.find_element(By.NAME, "customer[email]").click()
        self.app.driver.find_element(By.NAME, "customer[email]").send_keys(credentials.email)
        self.app.driver.find_element(By.ID, "customer_password").click()
        self.app.driver.find_element(By.ID, "customer_password").send_keys(credentials.password)
        self.app.driver.find_element(By.CSS_SELECTOR, ".form-action--submit").click()
        time.sleep(1)

    def logout(self):
        self.app.driver.find_element(By.XPATH, "//a[@class='site-header__account-link--logout']").click()