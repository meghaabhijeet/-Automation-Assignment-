import time
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element("id", "cat").click()
time.sleep(2)
driver.find_element("id", "itemc").click()
time.sleep(2)
driver.find_element("xpath",'//a[text()="Samsung galaxy s6"]').click()
time.sleep(2)
driver.find_element("xpath", '//a[text()="Add to cart"]').click()
time.sleep(2)
driver.quit()
