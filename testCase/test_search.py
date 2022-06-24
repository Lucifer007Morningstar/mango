import pytest

from PageObject.SearchCustomer import SearchCustomers
from PageObject.testlogin import LoginPage
from utilities.readProperties import ConfigReader
import time


class TestSearch():
    baseurl=ConfigReader.GetApplicationURL()
    username=ConfigReader.GetUsername()
    password =ConfigReader.GetPassword()

    @pytest.mark.sanity
    def test_003_Search(self,setup):
        self.driver=setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.driver.LP=LoginPage(self.driver)
        self.driver.LP.SetUsername(self.username)
        self.driver.LP.SetPassword(self.password)
        self.driver.LP.ClickLogin()
        SCUST=SearchCustomers(self.driver)
        SCUST.ClickAdmin()
        SCUST.Searchusername("Admin")
        SCUST.ClickSearch()
        time.sleep(2)
        status=SCUST.SearchByUsername("Admin")
        self.driver.close()
        assert True==status