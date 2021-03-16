from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
import time


class LogoutPage(BasePage):

############################## Add the locators of the Logout Page #############################
    Profile= (By.XPATH,"//*[@id='mobile-profile-img']/li/a/img")
    Logout_Button = (By.XPATH,"//*[@id='logoutForm']/a")
    Confirmation_alert_yes = (By.XPATH,"//*[@id='bot2-Msg1']")
    Confirmation_alert_no= (By.XPATH,"//*[@id='bot2-Msg1']")

    """Constructor of the Page Class : To Initialize the Driver"""
    def __init__(self,driver):
       super().__init__(driver)

##########################  Page Actions : Implement Action method for each locators ##########################
    """Page Actions"""
    """This is used to click on Profile"""
    def  profile(self):
        self.do_click(self.Profile)

    """This is used to click on Logout"""
    def logout(self):
        self.do_click(self.Logout_Button)


    """This is used to click on the confirmation Alert"""
    def confirmation(self,confirmation_id):
        if confirmation_id == "yes":
            self.do_click(self.Confirmation_alert_yes)
        elif confirmation_id == "no":
            self.do_click(self.Confirmation_alert_no)


    """This is used to the Logout from the Application"""
    def eots_logout(self,confirmation_value):
        self.profile()
        self.logout()
        self.confirmation(confirmation_value)
