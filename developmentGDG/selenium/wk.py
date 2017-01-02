#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
import unittest 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SeleniumTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def tearDown(self):
		pass 
		#self.driver.close()


	def test_open_wikipedia(self):
		self.driver.get(u'https://es.wikipedia.org/wiki/Wikipedia:Portada')

		#button = self.driver.find_element_by_id('Español')
		search = self.driver.find_element_by_id('searchInput')

		search.send_keys('Linux')
		#button.click()
		#email.send_keys('k1e@live.com.mx')
		#search = self.driver.find_element_by_id('searchInput')

		#search.send_keys('Eapaña')


		search.send_keys(Keys.RETURN)
		driver.implicity_wait(10)