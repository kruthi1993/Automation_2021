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


class Test_Alert_In_create_Window(BaseTest):
    logger= LogGen.loggen()
    mail_id = ReadConfig.sisaManager()
    password = ReadConfig.password()


    def test_more_filter_save_apply(self):
        self.logger.info("*********************Test_013_Alarm Alert 10 Records Per page ***********************")
        self.logger.info("**************** Verify whether More filter window is closed when clicked on close button present in More Filters ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id,self.password)
        self.Alarm_obj.alarm_alert_click()
        time.sleep(2)
        self.Alarm_obj.more_filter()
        self.driver.find_element(By.XPATH,"//select[@id='ddl_alarm']").click()
        field_droplist=self.driver.find_elements(By.XPATH,"//select[@id='ddl_alarm']/option")
        self.driver.find_element(By.XPATH,"//select[@id='ddl_alarm_operators']").click()
        operator_droplist=self.driver.find_elements(By.XPATH,"//select[@id='ddl_alarm_operators']/option")
        ECS_field = "Source IP"
        operator = "Should"
        Keyword = "10.100.7.22"
        col = str(5)
        self.Alarm_obj.filter_search(field_droplist,operator_droplist,ECS_field,operator,Keyword)
        self.Alarm_obj.apply()
        alerts = []
        length = len(self.driver.find_elements_by_xpath("//*[@id='loglist']/tr"))  # Checking the number of records exist in the table
        for i in range(1, length + 1):
            rows = self.driver.find_element_by_xpath("//*[@id='loglist']/tr[" + str(i) + "]/td["+col+"]").text
            alerts.append(rows)

        def chkList(alerts):
            return len(set(alerts)) == 1
        if Keyword in alerts:
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "more_filter_apply.png")
            assert False

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_009_Passed ***********************")


