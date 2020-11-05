from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")
search = driver.find_element_by_name("q")
search.send_keys("selenium install ubuntu python", Keys.RETURN)
result = driver.find_element_by_partial_link_text("pypi.org")
result.click()
sel_lib = driver.find_element_by_id("search")
sel_lib.send_keys("selenium library", Keys.RETURN)
results = driver.find_elements_by_class_name("package-snippet")
results[1].click()
driver.quit()

