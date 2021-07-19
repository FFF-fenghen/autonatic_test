class Mail:

    def __init__(self, driver):
        self.driver = driver

    def login(self,username,password):
        '''login'''
        login_frame = self.driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
        self.driver.switch_to.frame(login_frame)
        user = self.driver.find_element_by_name('email')
        user.send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_id("dologin").click()

    def logout(self):
        '''log out'''
        self.driver.find_element_by_id('_mail_component_5_5').click()
        self.driver.find_element_by_id('_mail_component_72_72').click()
