import pytest
from selenium import webdriver
from Pages.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from TestCases.test_BaseClass import BaseTest
from Pages.LogoutPage import LogoutPage
from utilities.customLogger import LogGen


import time

class Test_overview_dashboard(BaseTest):
    logger=LogGen.loggen()
    """test_case 1"""
    """Verify the headers present in the Overview Dashboard"""
    mail_id = ReadConfig.sisaManager()
    password =ReadConfig.password()

    @pytest.mark.sanity

    def test_home_page_title(self):
        self.logger.info("*********************Test_001_Overview Dashboard***********************")
        self.logger.info("****************Verify the headers present in the Overview Dashboard ******************")
        self.login_obj = LoginPage(self.driver)
        self.login_obj.eots_login(self.mail_id,self.password)
        if "SISA EOT" == "SISA EOT":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "test_home_page_title.png")
            assert False
        self.logger.info("********************* Test_001_Passed ***********************")




    @pytest.mark.regression
    def test_home_page_module(self):
        self.login_obj=LoginPage(self.driver)
        #self.login_obj.eots_login(self.mail_id,self.password)
        self.driver.find_element_by_id("Rawfilter").click()
        time.sleep(3)

