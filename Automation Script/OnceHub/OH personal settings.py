from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.set_page_load_timeout(15)
driver.maximize_window()
driver.get("https://app3.onceplatform.com/")
driver.implicitly_wait(35)

#################################  Login to OH  #################################
Ele=driver.find_element_by_name("email")
driver.find_element_by_name("email").send_keys("death-mad-34@staticso2.com")
Ele1=driver.find_element_by_name("password")
driver.find_element_by_name("password").send_keys("testing@123")
driver.find_element_by_id("signIn").click()
time.sleep(10)

#################################  Edit Profile settings  #################################
driver.find_element_by_xpath("//*[@id='rAccountIcon']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='Mobileheader']/div/div[2]/div[2]/ul/li[1]/sl-profile-dropdown/div/div[2]/div[2]/ul/li[1]/a/span").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/oh-page-header/div[1]/div[3]/div/button/span/oui-icon").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='cdk-overlay-0']/div/div/button/span").click()
time.sleep(2)
driver.find_element_by_name("lastName").clear()
driver.find_element_by_name("lastName").send_keys("Admin")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='oui-dialog-0']/form/div[2]/div[1]/button").click()
time.sleep(5)
driver.close()