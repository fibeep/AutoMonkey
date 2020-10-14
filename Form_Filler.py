from selenium import webdriver
chromedriver = executable_path=r"/Users/salocohen/Downloads/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.google.com")

