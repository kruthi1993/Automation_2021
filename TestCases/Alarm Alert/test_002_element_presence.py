import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from Pages.BasePage import BasePage
from Pages.LoginPage import LoginPage
from Pages.LogoutPage import LogoutPage
from TestCases.test_BaseClass import BaseTest
from Pages.AlarmAlert import AlarmAlert
from selenium.webdriver.common.by import By

import time

class Test_Element_Presence(BaseTest):
    logger= LogGen.loggen()
    mail_id = ReadConfig.sisaManager()
    password = ReadConfig.password()


    def test_export_to_excel_presence(self):
        self.logger.info("*********************Test_002_01_Export to Excel button visibility***********************")
        self.logger.info(
            "****************Verify whether Import button is available and is enabled when clicked on More filters ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id, self.password)
        self.Alarm_obj.alarm_alert_click()
        time.sleep(2)
        self.Alarm_obj.more_filter()
        time.sleep(3)
        ele_export_all_to_excel = self.driver.find_element(By.XPATH, "//button[@id='btnExcel']")
        if ele_export_all_to_excel.is_displayed() and ele_export_all_to_excel.is_enabled():
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "export_to_excel_presence.png")
            assert False

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_002_01_Passed ***********************")



    def test_create_ticket_presence(self):
        self.logger.info("*********************Test_002_02_Create Tickets button visibility***********************")
        self.logger.info(
            "****************Verify whether Create Tickets button is available and is enabled when clicked on More filters ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id, self.password)
        self.Alarm_obj.alarm_alert_click()
        time.sleep(2)
        self.Alarm_obj.more_filter()
        time.sleep(3)
        ele_create_ticket = self.driver.find_element(By.XPATH, "//button[@id='btnTicket']")
        if ele_create_ticket.is_displayed() and ele_create_ticket.is_enabled():
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "create_ticket_presence.png")
            assert False

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_002_02_Passed ***********************")


    def test_import_presence(self):
        self.logger.info("*********************Test_002_03_Import button visibility***********************")
        self.logger.info(
            "****************Verify whether Import button is available and is enabled when clicked on More filters ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id, self.password)
        self.Alarm_obj.alarm_alert_click()
        time.sleep(2)
        self.Alarm_obj.more_filter()
        time.sleep(3)
        ele_import = self.driver.find_element(By.XPATH, "//button[@type='submit' and text()='Import']")
        if ele_import.is_displayed() and ele_import.is_enabled():
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "import_button_presence.png")
            assert False

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_002_03_Passed ***********************")


    def test_delete_presence(self):
        self.logger.info("*********************Test_002_04_Delete button visibility**********************")
        self.logger.info(
            "****************Verify whether delete button is available and is enabled when clicked on More filters ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id, self.password)
        self.Alarm_obj.alarm_alert_click()
        time.sleep(2)
        self.Alarm_obj.more_filter()
        time.sleep(3)
        ele_delete = self.driver.find_element(By.XPATH, "//button[@type='submit' and text()='Delete']")
        if ele_delete.is_displayed() and ele_delete.is_enabled():
            assert False
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Delete_button_presence.png")
            assert True

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_002_04_Passed ***********************")



    def test_save_apply_presence(self):
        self.logger.info("*********************Test_002_05_Save and Apply button visibility***********************")
        self.logger.info(
            "****************Verify whether save and apply button is available and is enabled when clicked on More filters ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id, self.password)
        self.Alarm_obj.alarm_alert_click()
        time.sleep(2)
        self.Alarm_obj.more_filter()
        time.sleep(3)
        ele_save_apply = self.driver.find_element(By.XPATH, "//button[@type='submit' and text()='Save & Apply']")
        if ele_save_apply.is_displayed() and ele_save_apply.is_enabled():
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "save_and_apply_button_presence.png")
            assert False

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_002_05_Passed ***********************")



    def test_apply_presence(self):
        self.logger.info("*********************Test_002_06_Apply button visibility***********************")
        self.logger.info(
            "****************Verify whether Apply button is available and is enabled when clicked on More filters ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id, self.password)
        self.Alarm_obj.alarm_alert_click()
        time.sleep(2)
        self.Alarm_obj.more_filter()
        time.sleep(3)
        ele_apply = self.driver.find_element(By.XPATH, "//button[@type='submit' and text()='Apply']")
        if ele_apply.is_displayed() and ele_apply.is_enabled():
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "apply_button_presence.png")
            assert False

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_002_06_Passed ***********************")


    def test_clear_presence(self):
        self.logger.info("*********************Test_002_07_Clear button visibility***********************")
        self.logger.info(
            "****************Verify whether Clear button is available and is enabled when clicked on More filters ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id, self.password)
        self.Alarm_obj.alarm_alert_click()
        time.sleep(2)
        self.Alarm_obj.more_filter()
        time.sleep(3)
        ele_clear = self.driver.find_element(By.XPATH, "//button[@type='button' and text()='Clear']")
        if ele_clear.is_displayed() and ele_clear.is_enabled():
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "clear_button_presence.png")
            assert False

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_002_07_Passed ***********************")



    def test_close_presence(self):
        self.logger.info("*********************TTest_002_08_Close button visibility***********************")
        self.logger.info(
            "****************Verify whether Close button is available and is enabled when clicked on More filters ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id, self.password)
        self.Alarm_obj.alarm_alert_click()
        time.sleep(2)
        self.Alarm_obj.more_filter()
        time.sleep(3)
        ele_close = self.driver.find_element(By.XPATH, "//button[@type='button' and text()='Close']")
        if ele_close.is_displayed() and ele_close.is_enabled():
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "close_button_presence.png")
            assert False

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_002_08_Passed ***********************")


    @pytest.mark.sanity
    def test_Ticket_close_presence(self):
        self.logger.info("*********************TTest_002_09_Close button visibility***********************")
        self.logger.info(
            "****************Verify whether Close button is available and is enabled when clicked on More filters ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj = LogoutPage(self.driver)
        self.Alarm_obj = AlarmAlert(self.driver)
        self.login_obj.eots_login(self.mail_id, self.password)
        self.Alarm_obj.alarm_alert_click()
        time.sleep(2)
        self.Alarm_obj.checkbox()
        time.sleep(1)
        self.Alarm_obj.create_tickets()
        time.sleep(3)
        target = self.driver.find_element(By.XPATH,"//*[@id='logticketlist']/tr[10]")
        self.driver.execute_script('arguments[0].scrollIntoView(true);',target)
        ele_close = self.driver.find_element(By.XPATH,"/html/body/div[9]/div[3]/div/button[1]")
        if ele_close.is_displayed() and ele_close.is_enabled():
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "close_button_presence.png")
            assert False

        self.logout_obj.eots_logout("yes")
        self.logger.info("********************* Test_002_09_Passed ***********************")