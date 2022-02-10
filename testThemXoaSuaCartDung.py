import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# https://routine.vn/ao-khoac-chan-bong-co-v-regular-10f21jac012.html
str = input("nhâp link sản phẩm cần thêm vào giỏ hàng")
driver = webdriver.Chrome()
driver.get(str)
time.sleep(1)
driver.find_element(By.ID,'option-label-color-93-item-239').click()
time.sleep(1)
driver.find_element(By.ID,'option-label-size-192-item-32').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'.field.qty>.control span.edit-qty.plus').click()
time.sleep(2)
driver.find_element(By.ID,'product-addtocart-button').click()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR,'.block.block-minicart .block-content .minicart-items .product-item .details-qty.qty .edit-qty.plus').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'.block.block-minicart .block-content .minicart-items .product-item .details-qty.qty .update-cart-item').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'.block.block-minicart .block-content .minicart-items .product-item .details-qty.qty .edit-qty.minus').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'.block.block-minicart .block-content .minicart-items .product-item .details-qty.qty .update-cart-item').click()
time.sleep(2)


driver.find_element(By.CSS_SELECTOR,'.block.block-minicart .block-content .minicart-items .product-item .product.actions .action').click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'.modal-popup.confirm .modal-footer .action-primary').click()
time.sleep(2)