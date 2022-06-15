#Cas de test
# lancer le lien https://www.google.ca
# saisir le mot "Selenium" dans la zone de recherche
# Cliquer sur la suggestion selenium webdriver

import time
from  selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window();
# Ouvrir le lien google.ca
driver.get("https://www.google.ca/")
#Saisir le mot recherché Selenium
recherche=driver.find_element(By.NAME, "q")
recherche.send_keys("Selenium")
time.sleep(4)
#Récupérer la liste des suggestions
suggestions = driver.find_elements(By.XPATH, "//form[@action='/search' and @role='search']//ul[@role='listbox']//li//span")
#parcourir la liste des suggestions
#
#Faire un clique sur l'element de la liste si egale à "selenium webdriver"
for elementList in suggestions:
    print(elementList.text)
    if elementList.text.__eq__('selenium webdriver'):
        elementList.click()
        break
time.sleep(4)