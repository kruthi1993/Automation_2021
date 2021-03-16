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

class Test_Alarm_Alert_Page_Titles(BaseTest):
    logger= LogGen.loggen()
    mail_id = ReadConfig.sisaManager()
    password = ReadConfig.password()


    def test_alarm_alert_page_title(self):
        self.logger.info("*********************Test_001_Alarm Alert Page Title***********************")
        self.logger.info("****************Verify whether Alarm Alert list page is opened when clicked on Alarm Alert Menu ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id,self.password)
        self.Alarm_obj.alarm_alert_click()
        exp_res = "Alarm Alerts List"
        act_res = self.driver.find_element(By.XPATH,"//h3[@class='panel-title inline-block']").text
        if exp_res == act_res:
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "alarm_alert_page_title.png")
            assert False

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_001_Passed ***********************")

    def test_alarm_alert_create_ticket(self):
        self.logger.info("*********************Test_002_Alarm Alert_Create_Tickets_Page Title***********************")
        self.logger.info("****************Verify whether Ticket creation page is opened when clicked on Create Ticket ******************")
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
        exp_res = "Create Ticket for Alarms"
        act_res = self.driver.find_element(By.XPATH,"//span[@id='ui-id-2' and text()='Create Ticket for Alarms']").text
        self.Alarm_obj.create_ticket_close()
        if exp_res == act_res:
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "alarm_alert_create_ticket.png")
            assert False

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_002_Passed ***********************")


    def test_alarm_alert_view_message_title(self):
        self.logger.info("*********************Test_003_Alarm Alert View Message Page Title***********************")
        self.logger.info("****************Verify whether View Message is window is opened when clicked on View Message ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id,self.password)
        self.Alarm_obj.alarm_alert_click()
        time.sleep(2)
        self.Alarm_obj.view_message()
        exp_res = "Message"
        act_res = self.driver.find_element(By.XPATH,"//span[@id='ui-id-1' and text()='Message']").text
        self.Alarm_obj.view_close()
        if exp_res == act_res:
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "alarm_alert_view_message_title.png")
            assert False

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_003_Passed ***********************")