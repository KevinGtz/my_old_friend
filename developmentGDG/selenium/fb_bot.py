from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python"  in driver.tittle
elem = driver.find_element_by_name("q")
elem.send_