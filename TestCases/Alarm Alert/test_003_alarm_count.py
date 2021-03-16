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

import time

class Test_Alarm_Alert_Count(BaseTest):
    logger= LogGen.loggen()
    mail_id = ReadConfig.sisaManager()
    password = ReadConfig.password()


    def test_alarm_alert_count(self):
        self.logger.info("*********************Test_003_01_Alarm Alert Count***********************")
        self.logger.info("**************** Verify whether Alarm Count in the alarm alert page is showing same data as in Main company profile ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id,self.password)
        self.Alarm_obj.alarm_alert_click()
        time.sleep(2)
        alarm_count_company = self.driver.find_element(By.XPATH,"//span[@id='AlarmCount']").text
        alarm_count_alert_page = self.driver.find_element(By.XPATH,"//label[@id='lblcount']").text

        if alarm_count_company in alarm_count_alert_page :
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "alarm_alert_count.png")
            assert False

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_003_01_Passed ***********************")

