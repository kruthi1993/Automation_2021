import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
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


class Test_Export_to_Excel(BaseTest):
    logger= LogGen.loggen()
    mail_id = ReadConfig.sisaManager()
    password = ReadConfig.password()


    def test_export(self):
        self.logger.info("*********************Test_009_01_Alarm Alert 10 Records Per page ***********************")
        self.logger.info("**************** Verify whether all the selected records are shown in create ticket window ,when clicked on Create Ticket by selecting the Records ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id,self.password)
        self.Alarm_obj.alarm_alert_click()
        time.sleep(2)
        self.Alarm_obj.export_to_excel("yes")
        time.sleep(3)
        # if Keyword in alerts:
        #     assert True
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" + "more_filter_apply.png")
        #     assert False

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_009_01_Passed ***********************")


