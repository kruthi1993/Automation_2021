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

class Test_Alarm_Alert_records_per_page(BaseTest):
    logger= LogGen.loggen()
    mail_id = ReadConfig.sisaManager()
    password = ReadConfig.password()


    def test_alarm_alert_10_records_per_page(self):
        self.logger.info("*********************Test_004_01_Alarm Alert 10 Records Per page ***********************")
        self.logger.info("**************** Verify whether only 10 records are shown in the table when records per page is selected as 10 ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id,self.password)
        self.Alarm_obj.alarm_alert_click()
        time.sleep(2)

        el =self.driver.find_element(By.XPATH,"//select[@name='dt_basic_length']")
        for option in el.find_elements_by_tag_name('option'):
            if option.text=='10':
                option.click()
                break
        table_length =len(self.driver.find_elements(By.XPATH,"//*[@id='loglist']/tr"))
        print(table_length)
        if table_length <=10:
             assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "alarm_alert_10_records_per_page.png")
            assert False

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_004_01_Passed ***********************")


    def test_alarm_alert_20_records_per_page(self):
        self.logger.info("*********************Test_004_02_Alarm Alert 20 Records Per page ***********************")
        self.logger.info("**************** Verify whether only 20 records are shown in the table when records per page is selected as 10 ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id,self.password)
        self.Alarm_obj.alarm_alert_click()
        time.sleep(2)

        el =self.driver.find_element(By.XPATH,"//select[@name='dt_basic_length']")
        for option in el.find_elements_by_tag_name('option'):
            if option.text=='20':
                option.click()
                break
        table_length =len(self.driver.find_elements(By.XPATH,"//*[@id='loglist']/tr"))
        print(table_length)
        if table_length <=20:
             assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "alarm_alert_20_records_per_page.png")
            assert False

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_004_02_Passed ***********************")


    def test_alarm_alert_30_records_per_page(self):
        self.logger.info("*********************Test_004_03_Alarm Alert 30 Records Per page ***********************")
        self.logger.info("**************** Verify whether only 30 records are shown in the table when records per page is selected as 10 ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id,self.password)
        self.Alarm_obj.alarm_alert_click()
        time.sleep(2)

        el =self.driver.find_element(By.XPATH,"//select[@name='dt_basic_length']")
        for option in el.find_elements_by_tag_name('option'):
            if option.text=='30':
                option.click()
                break
        table_length =len(self.driver.find_elements(By.XPATH,"//*[@id='loglist']/tr"))
        print(table_length)
        if table_length <=30:
             assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "alarm_alert_30_records_per_page.png")
            assert False

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_004_03_Passed ***********************")

    def test_alarm_alert_40_records_per_page(self):
        self.logger.info("*********************Test_004_04_Alarm Alert 40 Records Per page ***********************")
        self.logger.info("**************** Verify whether only 40 records are shown in the table when records per page is selected as 10 ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id,self.password)
        self.Alarm_obj.alarm_alert_click()
        time.sleep(2)
        Drop_down_value =[10]
        self.driver.find_element(By.XPATH,"//select[@name='dt_basic_length']").click()
        droplist=self.driver.find_elements(By.XPATH,"//select[@name='dt_basic_length']/option")
        self.Alarm_obj.records_per_page(droplist,40)
        table_length =len(self.driver.find_elements(By.XPATH,"//*[@id='loglist']/tr"))
        print(table_length)
        if table_length ==40:
             assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "alarm_alert_40_records_per_page.png")
            assert False

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_004_04_Passed ***********************")



