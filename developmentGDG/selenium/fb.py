import unittest 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SeleniumTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def tearDown(self):
		pass 
		#self.driver.close()


	def test_open_facebook(self):
		self.driver.get('https:www.facebook.com')
		email = self.driver.find_element_by_id('email')
		password = self.driver.find_element_by_id('pass')
		button = self.driver.find_element_by_id('loginbutton')

		#message = self.driver.find_element_by_id('u_0_z')
		#submit= self.driver.find_element_by_id('#u_0_v')

		email.send_keys('kevin0911@live.com.mx')
		password.send_keys('gksl106004731')
		button.click()
		
		#message.send_keys('hola a todos soy un bot')
		message = self.driver.find_element_by_id('u_0_18')
		message_2 = self.driver.find_element_by_class_name('mf7 _4jy0 _4jy3 _4jy1 _51sy selected _42ft')

		message.send_keys('Hola soy un bot')
		message_2.click()

		email.send_keys(Keys.RETURN)
		driver.implicity_wait(10)