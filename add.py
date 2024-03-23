# import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# os.environ['PATH'] += r"C:\Users\WINDOWS 11\Desktop\Web_Scriping\chrome-win64"
# driver = webdriver.Chrome()
# driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
# driver.implicitly_wait(5)
# # try:
# #     no_button = find_element_by_id('at-cm-no-button')
# #     no_button.click()
# # except:
# #     print('No element with this class name. Skipping...')
# sum1 = driver.find_element_by_id('value1')
# sum2 = driver.find_element_by_id('value2')
#
# sum1.send_keys_to_element("12")
# sum2.send_keys_to_element("12")
#
# btn = driver.find_element_by_css_selector('button[onclick="return total()"]')
# btn.click_to();