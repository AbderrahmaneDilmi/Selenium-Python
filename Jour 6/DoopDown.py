from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.opencart.com/index.php?route=account/register")
drop_Country = driver.find_element(By.ID,"input-country")
country = Select(drop_Country)
#Select par texte visible
# country.select_by_visible_text("Algeria")
#Select par index
# country.select_by_index(0)
#Select par value (au niveau de select
# country.select_by_value("167")
#Récupérer tout les options dans select
all_options = country.options
total_options = len(all_options)
print("Le nombre d'options : ",total_options)
# Afficher toutes les options (les pays) dans la console
# for opt in all_options:
#      print (opt.text)
for opt in all_options:
    if opt.text == "Canada":
        opt.click()
        break

