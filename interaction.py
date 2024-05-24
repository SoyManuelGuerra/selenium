from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options = chrome_options)
url_path = "https://marvel-app-challenge.vercel.app/"
driver.get(url_path)
driver.maximize_window()
time.sleep(5)

# Función para hacer scroll down
def doScroll(scrollY):
  driver.execute_script(f'window.scrollTo(0, {scrollY})')
  
doScroll(500)
time.sleep(1)

driver.find_element(By.LINK_TEXT, "View All Characters").click()
time.sleep(1)

input = driver.find_element(By.CSS_SELECTOR, '#root > main > div:nth-child(2) > div > input')
input.send_keys('hulk')
doScroll(600)
time.sleep(5)

select_first_card = driver.find_element(By.XPATH, '//*[@id="root"]/main/div[3]/div/div[1]/div/button')
select_first_card.click()
time.sleep(5)

go_back = driver.find_element(By.LINK_TEXT, 'Go back')
go_back.click()
time.sleep(3)

clear_input = driver.find_element(By.XPATH, '//*[@id="root"]/main/div[2]/div/img[2]')
clear_input.click()
doScroll(300)
time.sleep(3)

driver.quit()