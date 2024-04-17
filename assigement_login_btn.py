import time
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
driver.implicitly_wait(30)
login_btn=driver.find_element("id","login2")
login_btn.click()
time.sleep(2)

driver.find_element("id","loginusername").send_keys("gita11")
time.sleep(2)

driver.find_element("id","loginpassword").send_keys("sharma123")
time.sleep(2)

driver.find_element("xpath", '//button[@onclick="logIn()"]').click()

driver.quit()