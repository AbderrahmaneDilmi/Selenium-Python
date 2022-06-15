import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[contains(text(),'Alert')]").click()

#  Récupérer l'alerte
alertWindow = driver.switch_to.alert
print(alertWindow.text)

# Cliquer sur le boutton OK de l'alerte (dismiss = cancel)
alertWindow.accept()


time.sleep(5)
driver.quit()
