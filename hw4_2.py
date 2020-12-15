from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.globallogic.com/ua/careers/")
search = driver.find_element_by_id("by_keyword")
search.send_keys("QA", Keys.RETURN)

result = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "mb-0"))
)
print(result.text)
driver.quit()

