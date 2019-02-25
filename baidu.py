# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re
import  HTMLTestRunner


class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_baidu(self):
        driver = self.driver
        #请求了一个网页地址
        driver.get(self.base_url + "/")
        # xw= driver.find_element_by_link_text(u"新闻")
        # # 获取输入框
        # srk=driver.find_element_by_id("kw")
        # srk.send_keys("元宵节快乐！")
        # srk.send_keys(Keys.SPACE)
        # print("控件尺寸：",srk.size)
        #
        # print("控件属性：",srk.get_attribute("class"))
        # print("控件是否可见：",srk.is_displayed())
        # print("控件是否可用：",srk.is_enabled())
        #
        #
        # time.sleep(2)
        # print("控件文本：", srk.text)

        #点击了输入框
        # driver.find_element_by_id("kw").click()
        # #清扫输入框
        # driver.find_element_by_id("kw").clear()
        # #在输入框输入文字
        # driver.find_element_by_id("kw").send_keys(u"测试")
        #点击百度一下按钮
        # driver.find_element_by_id("su").click()
        # driver.find_element_by_css_selector("#su").click()
        # driver.find_element_by_xpath(".//*[@id='su']").click()


        # driver.find_element_by_partial_link_text(u"新").click()

        #复数查找

        # input_list=driver.find_elements_by_tag_name("input")
        #输入用户名，密码
        # input_list[0].send_keys("zhangsan")
        # input_list[1].send_keys("123456")
        #登录
        # input_list[2].click()

        # for i  in input_list:
        #     print(i)

        driver.maximize_window()

        #显式等待
        ele_su=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,u"新闻")))
        ele_su.click()
        # time.sleep(3)
        # driver.refresh()
        # hl=driver.window_handles
        # driver.switch_to.window(hl[1])
        time.sleep(3)
        driver.find_element_by_link_text(u"文库").click()

        # time.sleep(3)
        # driver.get_screenshot_as_file("D:/baidu.png")
        # driver.back()
        time.sleep(3)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
