# Test case
# 1 lancer le navigateur
# # 2 accéder à l'adresse https://demo.nopcommerce.com/# # 3 cliquer sur le lien register
# # 4 remplir le formulaire
# # 5 cliquer sur le bouton Register
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
# 3 cliquer sur le lien register, en utilise le localisateur Link_text
driver.find_element(By.LINK_TEXT, "Register").click()
# 3 cliquer sur le lien register, en utilise le localisateur Partial_linktext
# driver.find_element(By.PARTIAL_LINK_TEXT,"Regi").click()
driver.find_element(By.ID, "FirstName").send_keys("Arwa compte1")
driver.find_element(By.NAME, "LastName").send_keys("Arwa")
driver.find_element(By.ID, "Email").send_keys("arwa@gmail.com")
driver.find_element(By.ID, "Password").send_keys("123456")
driver.find_element(By.ID, "ConfirmPassword").send_keys("123456")
driver.find_element(By.ID, "register-button").submit()
driver.find_element(By.CLASS_NAME, "ico-login").submit()

time.sleep(4)
driver.close()
