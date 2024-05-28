from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Inicializar el navegador
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://marvel-app-challenge.vercel.app/")



# Espera explícita para el elemento inicial
wait = WebDriverWait(driver, 10)
boton_inicial = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='View All Characters']")))
actions = webdriver.ActionChains(driver)
actions.double_click(boton_inicial).perform() # Doble click en el botón inicial que lo hace funcionar (no es necesario hacer scroll)
# driver.execute_script("arguments[0].click();", boton_inicial) # Alternativa usando el click con JS que vimos en la clase



# Cerrar el navegador
driver.quit()
