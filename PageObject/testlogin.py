from selenium.webdriver.common.by import By


class LoginPage():
    textfiled_username_xpath="//input[@id='txtUsername']"
    textfield_password_xpath="//input[@id='txtPassword']"
    button_login_xpath="//input[@id='btnLogin']"
    link_welcome_xpath="//a[@id='welcome']"
    link_logout_xpath="//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    def SetUsername(self,username):
        self.driver.find_element(By.XPATH,self.textfiled_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textfiled_username_xpath).send_keys(username)

    def SetPassword(self,password):
        self.driver.find_element(By.XPATH,self.textfield_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.textfield_password_xpath).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def ClickWelcome(self):
        self.driver.find_element(By.XPATH,self.link_welcome_xpath).click()

    def ClickLogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_xpath).click()
