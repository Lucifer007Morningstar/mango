import pytest

from PageObject.AddEmployee import NewEmployee
from PageObject.testlogin import LoginPage
from utilities.readProperties import ConfigReader
from selenium import webdriver


class TestPotoUpload():
    baseurl=ConfigReader.GetApplicationURL()
    username=ConfigReader.GetUsername()
    password =ConfigReader.GetPassword()


    @pytest.mark.regression
    def test_04_photo(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.driver.LP = LoginPage(self.driver)
        self.driver.LP.SetUsername(self.username)
        self.driver.LP.SetPassword(self.password)
        self.driver.LP.ClickLogin()
        self.driver.AD=NewEmployee(self.driver)
        self.driver.AD.ClickPIM()
        self.driver.AD.ClickAddEmployee()
        self.driver.AD.SetFirstName("Some")
        self.driver.AD.SetMiddleName("Thing")
        self.driver.AD.SetLastName("Good")
        self.driver.AD.UploadPhotograph()
        self.driver.AD.ClickSave()
        tt=self.driver.title
        if tt=="OrangeHRM":
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False



