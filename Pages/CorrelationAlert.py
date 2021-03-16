from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
import time

class CorrelationAlert(BasePage):
    Alerts_Module =(By.XPATH,"//span[text()='Alerts']")
    Correlation_Alert = (By.XPATH,"//a[text()='Correlation Alerts']")
    Export_All_To_Excel = (By.XPATH,"//button[@id='btnExcel']")
    Export_confirmation_alert = (By.XPATH,"")
    Create_Ticket = (By.ID,"btnTicket")
    Ticket_close = (By.XPATH,"/html/body/div[9]/div[3]/div/button[2]")
    Checkbox = (By.ID,"checkBoxAll")
    View_message = (By.XPATH,"//*[@id='loglist']/tr[1]/td[9]/center")
    View_close=(By.XPATH,"/html/body/div[6]/div[3]/div/button")
    More_Filter = (By.XPATH,"//a[@id='acctop']")
    Filter_Name=(By.ID,"txtfiltername")
    Records_Per_Page = (By.XPATH,"//select[@name='dt_basic_length']")
    keyword =(By.XPATH,"//*[@id='collapseOne-1']/div[3]/div[4]/div/input")
    Apply = (By.XPATH,"//button[@type='submit' and text()='Apply']")
    Close = (By.XPATH,"//button[@type='button' and text()='Close']")
    Import = (By.XPATH, "//button[@type='submit' and text()='Import']")
    Delete =(By.XPATH, "//button[@type='submit' and text()='Delete']")
    Save_Apply =(By.XPATH, "//button[@type='submit' and text()='Save & Apply']")
    Clear = (By.XPATH, "//button[@type='button' and text()='Clear']")
    Export_confirm = (By.XPATH,"//button[@id='bot2-Msg1']")
    Export_not_confirm = (By.XPATH,"//button[@id='bot1-Msg1']")
    Saved_filter_select = (By.XPATH,"//button[@type='button' and @title='Select Filter(s)']")





    """Constructor of the Page Class """
    def __init__(self,driver):
       super().__init__(driver)

    """Page Actions"""
    """This is used to the Navigate to Correlation Alert Module"""
    def Correlation_alert_click(self):
        self.mouse_over(self.Alerts_Module)
        self.do_click(self.Correlation_Alert)

    """This is used to the Export the Correlation Alerts"""
    def export_all_alerts(self):
        self.do_click(self.Export_All_To_Excel)

    """This is used to the enter the filter name"""
    def filter_name(self,name):
        self.do_send_keys(self.Filter_Name,name)


    """This is used to click on the confirmation Alert"""
    def confirmation(self,confirmation_id):
        if confirmation_id == "yes":
            self.do_click(self.Export_confirm)
        elif confirmation_id == "no":
            self.do_click(self.Export_not_confirm)

    """This is used to the Export the Correlation Alerts to Excel"""
    def export_to_excel(self,confirmation):
        self.export_all_alerts()
        self.confirmation(confirmation)


    """This is used to the Create the Correlation Tickets"""
    def create_tickets(self):
        self.do_click(self.Create_Ticket)

    """This is used to click on main checkbox"""
    def checkbox(self):
        self.do_click(self.Checkbox)

    """This is used to the view the message"""
    def view_message(self):
        self.do_click(self.View_message)

    """This is used to close the view window"""
    def view_close(self):
        self.do_click(self.View_close)

    """This is used to close the create Ticket window"""
    def create_ticket_close(self):
        self.do_click(self.Ticket_close)

    """This is used to select the number of records to be displayed in Page"""
    def records_per_page(self,value):
        self.select_values(self.Records_Per_Page,value)

    """This is used to click on More Filters"""
    def more_filter(self):
        self.do_click(self.More_Filter)


    """This is used to enter the filter condition"""

    def filter_search(self, field_list,operator_list, ECS_field,operator,search_keyword):
        self.select_values(field_list, ECS_field)
        self.select_values(operator_list,operator)
        self.do_click(self.keyword)
        time.sleep(2)
        self.do_send_keys(self.keyword, search_keyword)
        self.do_send_keys(self.keyword, Keys.ENTER)
        self.do_send_keys(self.keyword, Keys.RETURN)


    """This is used to click on  Apply button"""
    def apply(self):
        self.do_click(self.Apply)


    """This is used to click on main Apply button"""
    def filter_condition(self,dropdown,search_field,keyword_value):

        self.filter_search(dropdown,search_field,keyword_value)
        self.apply()

    """This is used to click on close button"""
    def close(self):
        self.do_click(self.Close)

    """This is used to click on Import button"""
    def import1(self):
        self.do_click(self.Import)

    """This is used to click on Delete button"""
    def delete(self):
        self.do_click(self.Delete)

    """This is used to click on Save_Apply button"""
    def save_apply(self):
        self.do_click(self.Save_Apply)

    """This is used to click on Clear button"""
    def clear(self):
        self.do_click(self.Clear)

    """This is used to select the saved filter condition"""
    def saved_filter(self,dropdown,list):
        self.select_values(dropdown,list)










