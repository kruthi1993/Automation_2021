from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
import time


class LoginPage(BasePage):

########################## Add the locators of the Login Page #############################
    Email = (By.ID,"Email")
    Password = (By.ID,"Password")
    Login_Button = (By.XPATH,"//button[@type='submit' and @value='Log in']")

    """Constructor of the Page Class : To Initialize the Driver """
    def __init__(self,driver):
       super().__init__(driver)

##########################  Page Actions : Implement Action method for each locators ##########################

    """This is Used to get the Page Title"""
    def get_login_page_title(self,title):
        return self.get_title(title)

    """This is used to the Login"""
    def eots_login(self,username,password):
        self.do_send_keys(self.Email,username)
        self.do_send_keys(self.Password,password)
        time.sleep(2)
        self.do_click(self.Login_Button)
