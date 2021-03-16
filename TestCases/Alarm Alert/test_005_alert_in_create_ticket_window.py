import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.LogoutPage import LogoutPage
from TestCases.test_BaseClass import BaseTest
from Pages.AlarmAlert import AlarmAlert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class Test_Alert_In_create_Window(BaseTest):
    logger= LogGen.loggen()
    mail_id = ReadConfig.sisaManager()
    password = ReadConfig.password()


    def test_alert_in_create_ticket_window(self):
        self.logger.info("*********************Test_005_01_Records in Create Ticket Window ***********************")
        self.logger.info("**************** Verify whether all the selected records are shown in create ticket window ,when clicked on Create Ticket by selecting the Records ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id,self.password)
        self.Alarm_obj.alarm_alert_click()
        time.sleep(2)
        self.Alarm_obj.checkbox()
        time.sleep(2)
        self.Alarm_obj.create_tickets()
        time.sleep(2)
        target = self.driver.find_element(By.XPATH,"//*[@id='logticketlist']/tr[10]")
        self.driver.execute_script('arguments[0].scrollIntoView(true);',target)
        table_length =len(self.driver.find_elements(By.XPATH,"//*[@id='logticketlist']/tr"))
        time.sleep(2)
        if table_length <= 10:
             assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "alert_in_create_ticket_window.png")
            assert False
        self.logger.info("********************* Test_005_01_Passed ***********************")


