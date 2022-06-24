import pytest
from selenium import webdriver
from PageObject.testlogin import LoginPage
from utilities.customlogger import LogGen
from utilities.readProperties import ConfigReader


class TestLogin():
    baseurl=ConfigReader.GetApplicationURL()
    username=ConfigReader.GetUsername()
    password =ConfigReader.GetPassword()
    # baseurl="https://opensource-demo.orangehrmlive.com/"
    # username="Admin"
    # password = "admin123"
    logger=LogGen.loggen()

    @pytest.mark.smoke
    def test_001_loginPage(self,setup):
        self.logger.info("*******TEst001************")

        self.driver = setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        if act_title=="OrangeHRM":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"Test_001_LoginPage.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_002_homepage(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.LP=LoginPage(self.driver)
        self.driver.LP.SetUsername(self.username)
        self.driver.LP.SetPassword(self.password)
        self.driver.LP.ClickLogin()
        homepae_title=self.driver.title
        if homepae_title=="OrangeHRM":
            self.driver.save_screenshot(".\\Screenshots\\" + "pass_Test_002_homepage.png")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"Failed_Test_002_homepage.png")
            self.driver.close()
            assert False





