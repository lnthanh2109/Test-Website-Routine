import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# [alt="Áo sơ mi tay ngắn, có thêu. LOOSE form - 10S21SHS010"]
str = input("nhâp alt quần áo cần tìm")
driver = webdriver.Chrome()
driver.get('https://routine.vn/thoi-trang-nam.html')
time.sleep(1)
driver.execute_script('window.scroll(0,500)')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,str).click()
