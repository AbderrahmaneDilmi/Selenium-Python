# test case
# lancer le lien https://www.saucedemo.com/# saisir le username et le password
# cliquer sur le bouton LOGIN
# cliquer sur le bouton ADD TO CART
# cliquer sur le panier
# cliquer sur le bouton checkout
# remplir le formulaire
# cliquer sur le bouton CONTINUE
# cliquer sur le bouton annuler
# cliquer sur le bouton REMOVE
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
#Saisir le username et le password
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
#cliquer sur le bouton login
driver.find_element(By.ID,"login-button").click()
#cliquer sur le bouton ADD TO CART
driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
#cliquer sur le panier
driver.find_element(By.CLASS_NAME,"shopping_cart_badge").click()
#cliquer sur le bouton checkout
driver.find_element(By.ID,"checkout").click()
#remplir les champs nom, prenom et code postal
driver.find_element(By.ID,"first-name").send_keys("Boudjedri")
driver.find_element(By.ID,"last-name").send_keys("Hamza")
driver.find_element(By.ID,"postal-code").send_keys("J4G")
#cliquer sur le bouton continuer
driver.find_element(By.ID,"continue").click()
#cliquer sur le botuon annuler
time.sleep(45)
driver.close()