from  selenium import webdriver
from selenium.webdriver.common.keys import Keys

#open the web browser for testing
kumaran = webdriver.Chrome()
kumaran.get("https://github.com/")

#Types the letter in the selected field
kumaran_engineer = kumaran.find_element_by_xpath("/html/body/div[1]/header/div[3]/div/div/form/label/input[1]")
kumaran_engineer.clear()

#The search word is kumaranusa in github
kumaran_engineer.send_keys("kumaranusa")

#Returns that searched value
kumaran_engineer.send_keys(Keys.RETURN)

