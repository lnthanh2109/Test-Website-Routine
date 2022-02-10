import time

from selenium import webdriver
from selenium.webdriver.common.by import By
str = input("nhâp từ khóa cần tìm")
driver = webdriver.Chrome()
driver.get('https://routine.vn/')
inp = driver.find_element(By.ID,'search')
inp.send_keys(str)
inp.submit()

# áo




