from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = driver = webdriver.Remote(
   command_executor='http://chromedriver:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)
driver.get("172.18.0.2:5000")
print 'I got source!'
print driver.page_source
driver.close()
