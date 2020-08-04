from selenium import webdriver
import time
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import datetime
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


# driver = webdriver.Chrome()
# driver.set_page_load_timeout(15)
# driver.maximize_window()
# driver.get("https://app3.onceplatform.com/")
# driver.implicitly_wait(35)

# #################################  Login to OH  #################################
# Ele=driver.find_element_by_name("email")
# driver.find_element_by_name("email").send_keys("death-mad-34@staticso2.com")
# Ele1=driver.find_element_by_name("password")
# driver.find_element_by_name("password").send_keys("testing@123")
# driver.find_element_by_id("signIn").click()
# time.sleep(10)
#
# #################################  Edit Profile settings  #################################
# driver.find_element_by_xpath("//*[@id='rAccountIcon']").click()
# time.sleep(3)
# driver.find_element_by_xpath("//*[@id='Mobileheader']/div/div[2]/div[2]/ul/li[1]/sl-profile-dropdown/div/div[2]/div[2]/ul/li[1]/a/span").click()
# time.sleep(5)

#################################  Date and Time notification #################################
# driver.find_element_by_xpath("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[5]/a/div/span").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='oui-select-5']/div/div[1]/span").click()
# time.sleep(2)
# driver.find_element_by_id("oui-input-0").send_keys("India")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='oui-option-367']/span").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/div/oh-date-and-time/div/div/form/div[2]/button[1]").click()
# time.sleep(5)
# driver.close()


class DateAndtime():

    driver = None

    def __init__(self, driver):
        self.driver = driver


    def server_login(self):
        personal_setting = OH_personal_setting(driver)
        personal_setting.navigate_to_url()
        personal_setting.login_to_OH()
        personal_setting.select_my_profile()

    def datetime(self):
        date1 = datetime(self.driver)
        date1.select_datetime()
        time.sleep(2)
        date1.clickontimezone_tochange()
        time.sleep(2)
        date1.search_timezone("India")
        time.sleep(2)
        date1.select_searchedtimezone()
        time.sleep(2)
        date1.click_save()
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    dateandtime = DateAndtime(driver)
    dateandtime.server_login()
    dateandtime.datetime()