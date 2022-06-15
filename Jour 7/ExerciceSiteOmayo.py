import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
# Ouvrir le lien Omayo.blogspot.com
driver.get("http://omayo.blogspot.com/")
# Récupération la liste des éléments suivantes  VOLOVO,Rapide,Hyndai et Audi
ListeVehicules = driver.find_element(By.ID, "multiselect1")
# Sélectionner la voiture
voiture = Select (ListeVehicules)
voiture.select_by_visible_text("Volvo")
voiture.select_by_value("swiftx")
voiture.select_by_value("audix")
time.sleep(4)
# Localisation de menu déroulant
menu_deroulant = driver.find_element(By.NAME, "SiteMap")
#Choisir le doc 3
listeDocuments = Select(menu_deroulant)
all_options = listeDocuments.options
for doc in all_options :
    if doc.text == "doc 3" :
        doc.click()
        break

time.sleep(4)
voiture.deselect_all()
time.sleep(4)



