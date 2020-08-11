import time

from selenium.webdriver.common.keys import Keys

from AutomationScript.Locators.OH_Locators.OH_schedule_share_publiclink_locator import share_without_personalised_link, \
    share_with_perosnalised_link, schedule_Publish, new_tab, Booking_form
from AutomationScript.OnceHub.OH_Profile.OH_personal_details import OH_personal_setting
from AutomationScript.Webdrivers.Chrome_driver import get_chrome_driver


class share_public_link():
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def server_login(self):
        personal_setting = OH_personal_setting(driver)
        personal_setting.navigate_to_url()
        time.sleep(5)
        personal_setting.login_to_OH()

    def Schedule_without_personalised_link(self):
        without = share_without_personalised_link(self.driver)
        without.click_schedule_option_from_top_menu()
        time.sleep(3)
    ############# Copy Booking link #####################3
        without.from_so_click_share_booking_link()
        time.sleep(5)
        without.select_dropdown_option()
        time.sleep(3)
        without.select_booking_page()
        time.sleep(3)
        without.copy_public_link()
        time.sleep(3)
        without.click_copy_close_button()
        time.sleep(5)
    ############# Open new tab and paste the booking url #####################
        opentab = new_tab(self.driver)
        opentab.open_new_window_and_paste_copied_url()
        time.sleep(10)
        opentab.select_15minute_event_type()
        time.sleep(5)
        opentab.change_time_zone()
        time.sleep(5)
        opentab.click_on_dropdown()
        time.sleep(2)
        opentab.search_India("India")
        time.sleep(5)
        opentab.select_searched_country()
        time.sleep(5)
        opentab.click_continue()
        time.sleep(5)
        opentab.select_time_slot()
        time.sleep(5)
        opentab.clickcontinue()
        time.sleep(7)
    ########### Fill booking form ##################
        form = Booking_form(self.driver)
        form.enter_name("Test")
        time.sleep(3)
        form.enter_email("testinginviteoncetesting@gmail.com")
        time.sleep(3)
        form.click_done()
        time.sleep(20)
        form.copy_bookingID()



    # def Schedule_with_personalised_link(self):
    #     without = share_without_personalised_link(self.driver)
    #     without.click_schedule_option_from_top_menu()
    #     time.sleep(5)
    #     without.from_so_click_share_booking_link()
    #     time.sleep(3)
    #     without.select_dropdown_option()
    #     time.sleep(3)
    #     without.select_booking_page()
    #     time.sleep(3)
    #     include = share_with_perosnalised_link(self.driver)
    #     include.turn_on_personalised_toggle()
    #     time.sleep(3)
    #     include.enter_customer_name("Test1")
    #     time.sleep(3)
    #     include.enter_customer_email("testinginviteoncetesting@gmail.com")
    #     time.sleep(3)
    #     without = share_without_personalised_link(self.driver)
    #     without.click_copy_close_button()
    #     time.sleep(5)
    #
    # def Publish_your_website(self):
    #     without = share_without_personalised_link(self.driver)
    #     without.click_schedule_option_from_top_menu()
    #     time.sleep(3)
    #     publish = schedule_Publish(self.driver)
    #     publish.select_share_and_publish_option()
    #     time.sleep(10)
    #     self.driver.back()
    #     time.sleep(10)


if __name__ == "__main__":
    driver = get_chrome_driver().launch_chrome()
    public_link = share_public_link(driver)
    public_link.server_login()
    public_link.Schedule_without_personalised_link()
    # public_link.Schedule_with_personalised_link()
    # public_link.Publish_your_website()