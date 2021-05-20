from AutomationScript.Calendar_connection.O365_via_oAuth_Calendar import O365_OAuth_calendar_connection_setting
from AutomationScript.Locators.OH_Locators.SignupAndSO_Onboarding_Locators import inbox_email, Product_selection, \
    Timezone_selection, Calendar_connection, video_conferencing, test_booking, Signup, skip_tour, logout, chatonce, \
    calendar_connection
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver
import time
from selenium.webdriver.common.keys import Keys
import pyperclip as pc



class Signup_SO_Onboarding():
    #################################  launch Chrome server  #################################

    driver = None
    # test

    def __init__(self, driver):
        self.driver = driver

    def Inbox_email(self):
        inbox = inbox_email(self.driver)
        self.driver.maximize_window()
        inbox.launch_inbox_email()
        inbox.copy_inbox_email()
        text = pc.paste()
        print(text)
        # print(Keys.CONTROL + "v")

    def Signup_with_new_user(self):
        onboard = Signup(self.driver)
        onboard.Navigate_to_URL()
        onboard.Enter_1stName("Test User")
        onboard.Enter_email(Keys.CONTROL + "v")
        onboard.Enter_password("testing@123")
        onboard.ReEnter_password("testing@123")
        onboard.click_signup_button()

    def select_product(self):
        product = Product_selection(self.driver)
        product.select_so_product()

    def select_timezone(self):
        timezone = Timezone_selection(self.driver)
        timezone.select_sunday()
        timezone.select_saturday()
        timezone.click_on_change_timezone()
        timezone.click_on_dropdown()
        timezone.search_India("India")
        timezone.select_timezone()
        timezone.click_save()
        timezone.click_continue()

    def skip_calendar_connection(self):
        skip = calendar_connection(self.driver)
        skip.click_skip_for_calendar_connection()

    def connect_Exchange_calendar(self):
        connect = Calendar_connection(self.driver)
        connect.click_calendar_expand_button()
        connect.click_exchange_connect_button()
        connect.enter_username("gilad@staticso.com")
        connect.enter_password("schEdu1e")
        connect.expand_advanced_setting()
        connect.enter_ews_url("https://mex09.emailsrvr.com/owa")
        connect.click_connect_button()
        connect.click_continue()

    def Conferencing_option(self):
        video = video_conferencing(self.driver)
        video.click_skip_for_video_conferencing()

    def Booking_test(self):
        test = test_booking(self.driver)
        test.click_skip_for_test_booking()

    def SO_tour_skip(self):
        tour = skip_tour(self.driver)
        tour.click_skip_for_test_booking()

    def ChatOnce_started(self):
        co_start = chatonce(self.driver)
        co_start.click_on_setup()
        co_start.select_ChatOnce()
        co_start.click_Get_started_button_on_popup()

    def Application_logout(self):
        log_out = logout(self.driver)
        log_out.click_profile_icon()
        log_out.click_signout()


if __name__ == "__main__":
    for x in range(1):
        driver = get_chrome_driver().launch_chrome()
        Onboard_SO = Signup_SO_Onboarding(driver)
        Onboard_SO.Inbox_email()
        Onboard_SO.Signup_with_new_user()
        Onboard_SO.select_product()
        Onboard_SO.select_timezone()
        Onboard_SO.skip_calendar_connection()
        # Onboard_SO.connect_Exchange_calendar()
        Onboard_SO.Conferencing_option()
        Onboard_SO.Booking_test()
        Onboard_SO.SO_tour_skip()
        calendar = O365_OAuth_calendar_connection_setting(driver)
        calendar.Calendarconnection_from_profilemenu()
        calendar.calendarconnection_from_menu()
        # calendar.Oh_O365_oAuth_calendar_connect()
        driver.close()

    # Onboard_SO.ChatOnce_started()
    # Onboard_SO.Application_logout()
    # driver.close()
