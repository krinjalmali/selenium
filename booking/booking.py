import os
import self
import booking.constants as const
from selenium import webdriver

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Users\WINDOWS 11\Desktop\Web_Scriping\chrome-win64", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get("https://www.booking.com")

    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[header-currency-picker-trigger]'
        )
        currency_element.click_to()

    # selected_currency_element = self.find_element_by_css_selector(
    #     f"a[data-modal-header-async-url-param*=\"selected_currency={currency}\"]"
    # )
    # selected_currency_element.click()

