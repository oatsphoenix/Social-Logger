from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Firefox()
driver.maximize_window()

# LOG INTO FACEBOOK 

driver.get("http://www.facebook.com")
driver.implicitly_wait(30)
username = driver.find_element_by_name("email")
password = driver.find_element_by_name("pass")
login    = driver.find_element_by_name("login")
username.send_keys("youremailhere")
password.send_keys("yourpasswordhere")
login.click()

# LOG INTO INSTAGRAM

driver.execute_script("window.open('about:blank', 'secondtab');") # opens a new, blank tab
driver.switch_to.window("secondtab")                              # switches over to new tab
driver.get("http://www.instagram.com")
driver.implicitly_wait(30) 
switchUser = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div/div[3]/span/button')
switchUser.click()
username = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
password = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
login    = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
username.send_keys("yourusernamehere")
password.send_keys("yourpasswordhere")
login.click()

# LOG INTO TWITTER

driver.execute_script("window.open('about:blank', 'secondtab');") # opens a new, blank tab
driver.switch_to.window("secondtab")                              # switches over to new tab
driver.get("http://www.twitter.com/login")
username = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
password = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
login    = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span")
username.send_keys("yourusernamehere")
password.send_keys("yourpasswordhere")
login.click()