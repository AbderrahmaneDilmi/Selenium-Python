import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[contains(text(),'Confirm')]").click()
time.sleep(2)

#  Récupérer l'alerte
alertWindow = driver.switch_to.alert
print(alertWindow.text)

# Permet de cliquer sur (dismiss = cancel)
alertWindow.dismiss()


time.sleep(5)
driver.quit()
