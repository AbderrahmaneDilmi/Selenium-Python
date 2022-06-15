import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.switch_to.frame("packageListFrame")
time.sleep(3)
# Cliquer sur le lien
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()

#Sortir de frame et retourner à la page principale
driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")
driver.find_element(By.XPATH, "/html/body/main/div/section[1]/ul/li[14]/a/span").click()
# Cliquer sur Help
#driver.switch_to.default_content()
#driver.switch_to.frame("classFrame")
#driver.find_element(By.XPATH, "/html/body/main/div/div[2]/iframe").click()

time.sleep(3)
driver.quit()



