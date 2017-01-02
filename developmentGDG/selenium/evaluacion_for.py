#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
import unittest 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from my_key import key

class SeleniumTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		
	def tearDown(self):
		pass
		#self.driver.close()

#para correr el servidor se usa el comando *nosetests "programa"
	
	def test_open_aragon_login(self):

		keys = key
		self.driver.get(u'http://www.aragon.unam.mx/evaluacion1.1/Login.php')

		search = self.driver.find_element_by_name('nombre_usuario')
		search_2 = self.driver.find_element_by_name('contrasenia')
		button = self.driver.find_element_by_class_name('button')

		search.send_keys('106004731')
		search_2.send_keys(keys)
		button.click()
		
		evaluar =  self.driver.find_element_by_link_text('Evaluar Cursos').click()
		
		button_2 = self.driver.find_element_by_class_name('button')
		button_2.click()

		always = self.driver.find_element_by_name('P1')
		always.click()

		for i in range(2, 25):
			always = self.driver.find_element_by_name('P{}'.format(i))
			always.click()

		button_3 = self.driver.find_element_by_class_name('button')
		button_3.click()



	
"""
	search.send_keys(Keys.RETURN)
	driver.implicity_wait(100)
		always_2 = self.driver.find_element_by_name('P2')
		always_2.click()

		always_3 = self.driver.find_element_by_name('P3')
		always_3.click()

		always_4 = self.driver.find_element_by_name('P4')
		always_4.click()

		always_5 = self.driver.find_element_by_name('P5')
		always_5.click()

		always_6 = self.driver.find_element_by_name('P6')
		always_6.click()

		always_7 = self.driver.find_element_by_name('P7')
		always_7.click()

		always_8 = self.driver.find_element_by_name('P8')
		always_8.click()

		always_9 = self.driver.find_element_by_name('P9')
		always_9.click()

		always_10 = self.driver.find_element_by_name('P10')
		always_10.click()

		always_11 = self.driver.find_element_by_name('P11')
		always_11.click()

		always_12 = self.driver.find_element_by_name('P12')
		always_12.click()

		always_13 = self.driver.find_element_by_name('P13')
		always_13.click()

		always_14 = self.driver.find_element_by_name('P14')
		always_14.click()

		always_15 = self.driver.find_element_by_name('P15')
		always_15.click()

		always_16 = self.driver.find_element_by_name('P16')
		always_16.click()

		always_17 = self.driver.find_element_by_name('P17')
		always_17.click()

		always_18 = self.driver.find_element_by_name('P18')
		always_18.click()

		always_19 = self.driver.find_element_by_name('P19')
		always_19.click()

		always_20 = self.driver.find_element_by_name('P20')
		always_20.click()

		always_21 = self.driver.find_element_by_name('P21')
		always_21.click()

		always_22 = self.driver.find_element_by_name('P22')
		always_22.click()

		always_23 = self.driver.find_element_by_name('P23')
		always_23.click()

		always_24 = self.driver.find_element_by_name('P24')
		always_24.click() """



		#Evaluar_Cursos.click()

		#email.send_keys('k1e@live.com.mx')
		#search = self.driver.find_element_by_id('searchInput')

		#search.send_keys('Eapaña')

