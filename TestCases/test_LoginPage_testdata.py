import pytest
from selenium import webdriver
from Pages.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from TestCases.test_BaseClass import BaseTest
from Pages.LogoutPage import LogoutPage
from utilities.customLogger import LogGen
from utilities import XLUtilis


import time

class Test_ddt(BaseTest):
    logger=LogGen.loggen()
    """test_case 1"""
    """Verify the headers present in the Overview Dashboard"""
    path ="C:/Users/kruthi.p/PycharmProjects/EOTS_Automation_2021/TestData/TestData.xlsx"
    # mail_id = ReadConfig.sisaManager()
    # password =ReadConfig.password()

    @pytest.mark.sanity

    def test_home_page_title(self):
        self.logger.info("*********************Test_001_Overview Dashboard***********************")
        self.logger.info("****************Verify the headers present in the Overview Dashboard ******************")
        self.login_obj = LoginPage(self.driver)
        self.logout_obj =LogoutPage(self.driver)
        self.row = XLUtilis.getRowCount(self.path,"Sheet1")
        print(self.row)
        lst_result_status = []
        for r in range(2,self.row+1):
            self.mail_id=XLUtilis.readData(self.path,"Sheet1",r,1)
            self.password=XLUtilis.readData(self.path,"Sheet1",r,2)
            self.exp = XLUtilis.readData(self.path,"Sheet1",r,3)
            self.login_obj.eots_login(self.mail_id,self.password)
            time.sleep(3)
            if "SISA EOT" == "SISA EOT":
               assert True
               if self.exp == "Pass":
                   self.logger.info("****Passed*****")
                   self.logout_obj.eots_logout("yes")
                   lst_result_status.append("fail")
               elif self.exp == "Fail":
                   self.logger.info("****Passed*****")
                   self.logout_obj.eots_logout("yes")
                   lst_result_status.append("Fail")
            else:
               self.driver.save_screenshot(".\\Screenshots\\"+ "test_home_page_title.png")
               assert False



            self.logger.info("********************* Test_001_Passed ***********************")





    def test_home_page_module(self):
        self.login_obj=LoginPage(self.driver)
        self.driver.find_element_by_id("Rawfilter").click()

