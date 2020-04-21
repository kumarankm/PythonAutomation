from  selenium import webdriver
from selenium.webdriver.common.keys import Keys

#open the web browser for testing
kumaran = webdriver.Chrome()
kumaran.get("https://www.instagram.com/u.s.a.dreamer/")

#Types the letter in the selected field
kumaran_engineer = kumaran.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
kumaran_engineer.clear()

#The search word is kumaranusa in github
kumaran_engineer.send_keys("thisisbillgates")

#Returns that searched value
kumaran_engineer.send_keys(Keys.RETURN)

