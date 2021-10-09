# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestUpdateASWWUProfile():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_updateASWWUProfile(self):
    self.driver.get("https://aswwu.com/")
    self.driver.set_window_size(550, 691)
    self.driver.find_element(By.CSS_SELECTOR, ".navbar-toggler-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(1) > .d-block").click()
    self.driver.find_element(By.ID, "mask-search-query").click()
    self.driver.find_element(By.ID, "mask-search-query").send_keys("hayden  tinker")
    self.driver.find_element(By.ID, "mask-search-query").send_keys(Keys.ENTER)
    self.driver.find_element(By.ID, "mask-search-query").send_keys("daisy perez")
    self.driver.find_element(By.ID, "mask-search-query").send_keys(Keys.ENTER)
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.ID, "userNameInput").send_keys("hayden.tinker")
    self.driver.find_element(By.ID, "passwordInput").click()
    self.driver.find_element(By.ID, "passwordInput").send_keys("Caseymorgan966401!")
    self.driver.find_element(By.ID, "submitButton").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-circle").click()
    self.driver.find_element(By.LINK_TEXT, "Update Profile").click()
    self.driver.find_element(By.ID, "quote_authorinput").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-circle").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
    self.driver.execute_script("window.scrollTo(0,0)")
  
