import time
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
driver.implicitly_wait(30)
signup_btn=driver.find_element("id", "signin2")
signup_btn.click()
time.sleep(2)

driver.find_element("id", "sign-username").send_keys("megha16")
time.sleep(2)

driver.find_element("id", "sign-password").send_keys("ghatol62")
time.sleep(2)

driver.find_element("xpath", '//button[@onclick="register()"]').click()

driver.quit()