import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
#Mettre le driver 1éré fenetre ds une variable
parentWindow = driver.current_window_handle
# L'identifiant de la 1 ere fenetre : CDwindow-707B4373443B42A0B301F3FABD251852
print(parentWindow)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

#Récup la liste des ID's de fenetre ouvertes
windowsHandles = driver.window_handles
# Premiere fenetre
parentWindowId = windowsHandles[0]
# Deuxieme fenetre
childWindowId = windowsHandles[1]
# Les générés sont dynamiques
print("parentWindowId", parentWindowId)
print("childWindowId", childWindowId)
# Basculer vers la 2eme fenetre, récup url et titre de 2eme fenetre
driver.switch_to.window(childWindowId)
url1 = driver.current_url
title1 = driver.title
# Switch à la fenetre parent
driver.switch_to.window(parentWindowId)
print("#################################################################")
url2 = driver.current_url
title2 = driver.title
print(url2)
print(title2)
# 2 eme approche : parcourrir la liste de windowsHandleIds et vrf le titre
# for winId in windowsHandelsIds:
for winId in windowsHandles:
    driver.switch_to.window(winId)
    if driver.title == title1:
        driver.close()



time.sleep(3)
driver.quit()