from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class MySeleniumTests(StaticLiveServerTestCase):
    # fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        self.selenium.implicitly_wait(15)
        username_input = self.selenium.find_element_by_id("loginFormInputEmail")
        username_input.send_keys('admin@gmail.com')
        self.selenium.implicitly_wait(15)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('secret')
        self.selenium.implicitly_wait(30)
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
