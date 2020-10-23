# -*- encoding=utf8 -*-
__author__ = "janson"
# 还款申请单

from airtest.core.api import *
using(r"E:\黄振旭\费用管理系统自动化测试用例\conf\common.air")
from common import common
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)
driver.get("http://14.21.59.70:1000/")
driver.maximize_window()#放大浏览器
# 登录夏子霞支付借款单
common.login(driver,"xiazixia")
common.pay_loan(driver)
common.quit(driver)
# 登录huangzhenxu账号,提交还款申请单
common.login(driver,"huangzhenxu")
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/ul/div[3]/li/ul/div[3]/a/li/span").click()

driver.assert_template(Template(r"tpl1595316700201.png", record_pos=(11.41, 1.0), resolution=(100, 100)), "进入还款申请单")
driver.airtest_touch(Template(r"tpl1595316722041.png", record_pos=(11.645, 1.825), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595316735573.png", record_pos=(10.88, 1.59), resolution=(100, 100)), "进入新增页面")
driver.airtest_touch(Template(r"tpl1595319105650.png", target_pos=6, record_pos=(15.725, 2.05), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595319156050.png", record_pos=(3.73, 3.635), resolution=(100, 100)), "进入选择借款单界面")
driver.airtest_touch(Template(r"tpl1595319182296.png", record_pos=(14.42, 5.43), resolution=(100, 100)))
driver.find_element_by_xpath("//*[@id=\"erp_cmbREPAY_MODE_ID\"]/div/div/input").click()
driver.airtest_touch(Template(r"tpl1595319230179.png", record_pos=(3.325, 4.44), resolution=(100, 100)))
driver.find_element_by_id("erp_txtMEMO").send_keys("123")
driver.find_element_by_id("erp_txtREPAY_AMOUNT").clear()
driver.find_element_by_id("erp_txtREPAY_AMOUNT").send_keys("1000")

driver.airtest_touch(Template(r"tpl1595319316699.png", record_pos=(2.16, 1.735), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595319464979.png", record_pos=(13.595, 2.665), resolution=(100, 100)), "保存")
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595319540507.png", record_pos=(13.675, 2.655), resolution=(100, 100)), "提交成功")
# 登录夏子霞确认还款
common.login(driver,"xiazixia")
common.confirm_repayment(driver) # 确认还款
common.quit(driver)
# 登录黄振旭查看是否已确认还款
common.login(driver,"huangzhenxu")
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/ul/div[3]/li/ul/div[3]/a/li/span").click()
driver.assert_template(Template(r"tpl1595316700201.png", record_pos=(11.41, 1.0), resolution=(100, 100)), "进入还款申请单")
driver.refresh() # 刷新方法 refresh
driver.assert_template(Template(r"tpl1595320236760.png", record_pos=(15.155, 4.69), resolution=(100, 100)), "显示已收款")



auto_setup(__file__)

