from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Locators.OH_Locators.OH_Profile_Locators import select_authentication


class AuthenticationPage():

    def authentication_module(self):
        personal_setting = OH_personal_setting()
        personal_setting.login_to_OH()
        personal_setting.select_my_profile()
        auth = select_authentication(personal_setting.driver)
        auth.click_authentication()
        time.sleep(2)
        auth.enable_2factor_toggle()
        time.sleep(2)
        auth.enter_password("testing@123")
        time.sleep(2)
        auth.click_submit_button()
        time.sleep(5)
        auth.disable_2factor_toggle()
        time.sleep(3)
        personal_setting.driver.close()


if __name__ == "__main__":
    authenticate = AuthenticationPage()
    authenticate.authentication_module()


        # driver = webdriver.Chrome()
        # driver.set_page_load_timeout(15)
        # driver.maximize_window()
        # driver.get("https://app3.onceplatform.com/")
        # driver.implicitly_wait(35)
        #
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
        #
        # #################################  Authentication page #################################
        # driver.find_element_by_link("/html/body/oh-root/div[2]/sl-sidenav-container/sl-sidenav/div/perfect-scrollbar/div/div[1]/oh-sidebar/div[2]/div[2]/ul/sl-sidenav-category/li/sl-sidenav-category-links/div/perfect-scrollbar/div/div[1]/ul/li[7]/a/div/span").click()
        # time.sleep(2)
        # driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/div/oh-authentication/div/div/form/div[1]/div[1]/div/oui-slide-toggle/label/span").click()
        # time.sleep(2)
        # driver.find_element_by_id("current-password").send_keys("testing@123")
        # time.sleep(2)
        # driver.find_element_by_xpath("//*[@id='oui-dialog-1']/form/div[2]/div[1]/button/span").click()
        # time.sleep(5)
        # driver.find_element_by_xpath("//*[@id='MainDataDiv']/div/div/oh-user-profile/div/oh-authentication/div/div/form/div[2]/button[2]/span").click()
        # time.sleep(3)
        # driver.close()