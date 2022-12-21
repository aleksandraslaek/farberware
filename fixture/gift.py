from selenium.webdriver.common.by import By


class GiftCard:
    def __init__(self, app):
        self.app = app
    def add_gift_card(self):
        self.app.driver.get('https://farberwarecookware.com/products/farberware-gift-card')
        self.app.driver.find_element(By.XPATH,
                                     "//button[@class='product-form--atc-button mdc-ripple-surface mdc-ripple-upgraded']").click()
        self.app.driver.find_element(By.XPATH, "//a[@class='cart-item--remove-link']").click()