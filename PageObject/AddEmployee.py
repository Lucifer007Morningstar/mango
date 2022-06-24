from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class NewEmployee():
    link_PIM_xpath="//b[normalize-space()='PIM']"
    link_add_employment_xpath="//a[@id='menu_pim_addEmployee']"
    upload_photograph_xpath="//input[@id='photofile']"
    textfield_firtname_xpath="//input[@id='firstName']"
    textfield_lastname_xpath="//input[@id='lastName']"
    textfield_middlename_xpath="//input[@id='middleName']"
    textfield_employeeid_xpath="//input[@id='employeeId']"
    checkbox_loginDetails_xpath="//input[@id='chkLogin']"
    button_save_xpath="//input[@id='btnSave']"


    def __init__(self,driver):

        self.driver = driver
    def ClickPIM(self):
        chains=ActionChains(self.driver)
        PIMelement=self.driver.find_element(By.XPATH,self.link_PIM_xpath)
        chains.move_to_element(PIMelement).perform()

    def ClickAddEmployee(self):
        self.driver.find_element(By.XPATH, self.link_add_employment_xpath).click()

    def UploadPhotograph(self):
        self.driver.find_element(By.XPATH, self.upload_photograph_xpath).send_keys("C://Users/Anshu/Desktop/icon//ins.png")

    def SetFirstName(self,fname):
        self.driver.find_element(By.XPATH, self.textfield_firtname_xpath).clear()
        self.driver.find_element(By.XPATH, self.textfield_firtname_xpath).send_keys(fname)


    def SetMiddleName(self,mname):
        self.driver.find_element(By.XPATH, self.textfield_middlename_xpath).clear()
        self.driver.find_element(By.XPATH, self.textfield_middlename_xpath).send_keys(mname)

    def SetLastName(self,lname):
        self.driver.find_element(By.XPATH, self.textfield_lastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.textfield_lastname_xpath).send_keys(lname)

    def ClickSave(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()
