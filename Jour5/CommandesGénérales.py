import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# Obtemir url de la page
driver.get("https://demo.nopcommerce.com/")
url_page = driver.current_url
print(url_page)
# Obtenir title de la page
titre_page = driver.title
print(titre_page)
# Obtenir code source
page_source = driver.page_source
print(page_source)




time.sleep(3)
driver.close()