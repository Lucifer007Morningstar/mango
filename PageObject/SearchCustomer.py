from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SearchCustomers:
    link_admin_xpath="//b[normalize-space()='Admin']"
    textfield_username_xpath="//input[@id='searchSystemUser_userName']"
    dropdown_user_role_xpath="//select[@id='searchSystemUser_userType']"
    textfield_employeename_xpath="//input[@id='searchSystemUser_employeeName_empName']"
    dropdown_status_xpath="//select[@id='searchSystemUser_status']"
    button_search_xpath="//input[@id='searchBtn']"

    tablesearch_xpath="//table[@id='resultTable']"
    tablerow_xpath="//table[@id='resultTable']//tr"
    tablecolumn_xpath="//table[@id='resultTable']//tr/td"



    def __init__(self,driver):
        self.driver = driver

    def ClickAdmin(self):
        self.driver.find_element(By.XPATH,self.link_admin_xpath).click()

    def Searchusername(self,Username):
        self.driver.find_element(By.XPATH,self.textfield_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textfield_username_xpath).send_keys(Username)

    def SelectUserRole(self,text):
        dropdown=Select(self.driver.find_element(By.XPATH,self.dropdown_user_role_xpath))
        dropdown.select_by_visible_text(text)

    def SelectEmployeeName(self,employeename):
        self.driver.find_element(By.XPATH,self.textfield_employeename_xpath).clear()
        self.driver.find_element(By.XPATH,self.textfield_employeename_xpath).send_keys(employeename)

    def SelectStatues(self,text):
        dropdown2=Select(self.driver.find_element(By.XPATH,self.dropdown_status_xpath))
        dropdown2.select_by_visible_text(text)

    def ClickSearch(self):
        self.driver.find_element(By.XPATH, self.button_search_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tablerow_xpath))

    def NoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tablecolumn_xpath))

    def SearchByUsername(self,Username):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.tablesearch_xpath)
            Usernameid=table.find_element(By.XPATH,"//table[@id='resultTable']//tr["+str(r)+"]/td[2]").text
            if Usernameid==Username:
                flag=True
                break
        return flag

