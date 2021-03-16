from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""This class is  the parent of all pages"""
"""It contains all generic methods and utilities for all the pages"""

class BasePage:


    """Constructor of the Page Class : To Initialize the Driver """
    def __init__(self,driver):
        self.driver = driver        #Initailizing to the local driver : self.driver---class variable

    """ Generic Method to click on any web element  """
    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    """ Generic Method to send the data to any web element  """
    def do_send_keys(self,by_locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    """ Generic Method to fetch the text from any web element  """
    def get_element_text(self,by_locator):
        element= WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """ Generic Method to check the visibility of web element  """
    def is_visible(self,by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    """ Generic Method to fetch the title of the Web Page  """
    def get_title(self,title):
        WebDriverWait(self.driver,10).until(EC.title_is(title))
        return self.driver.title

    """ Generic Method to Navigate to Modules : Mouse Over """
    def mouse_over(self,by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    # """ Generic Method for Selecting the dropdown values """
    # def select_values(self,drop_list,values):
    #     for ele in drop_list:
    #         for k in range(len(values)):
    #             if ele == values[k]:
    #                 ele.click()
    #                 break


    def select_values(self, dropdown, values):
        for ele in dropdown:
            print(ele.text)
            if ele.text == values:
                ele.click()
                break

