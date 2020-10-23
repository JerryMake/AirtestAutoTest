# -*- encoding=utf8 -*-
__author__ = "Administrator"
# 预付款申请单（部门，未签订合同）
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
#登录黄振旭账号，填写预付款申请单↓
common.login(driver,"huangzhenxu")
driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")
driver.airtest_touch(Template(r"tpl1597394167142.png", record_pos=(0.07, 6.645), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595215637171.png", record_pos=(6.735, 1.575), resolution=(100, 100)), "进入预付款申请单页面")
driver.airtest_touch(Template(r"tpl1595215662545.png", record_pos=(7.125, 1.975), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595215694789.png", record_pos=(6.4, 1.76), resolution=(100, 100)), "进入新增界面")
driver.find_element_by_xpath("//*[@id=\"erp_cmbEXPECTED_INVOICE_TYPE\"]/div/div/input").send_keys("")
driver.airtest_touch(Template(r"tpl1595215753390.png", record_pos=(7.805, 5.555), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595215764639.png", record_pos=(7.065, 4.355), resolution=(100, 100)), "选择预计发票类型")
driver.find_element_by_id("erp_txtEXPECTED_INVOICE_RATE").clear()
driver.find_element_by_id("erp_txtEXPECTED_INVOICE_RATE").send_keys("10")
driver.find_element_by_id("erp_txtADVANCES_AMOUNT").clear()
driver.find_element_by_id("erp_txtADVANCES_AMOUNT").send_keys("1000")
driver.find_element_by_id("erp_txtPAYEE_BANK_ACCOUNT").send_keys("123456")
driver.find_element_by_id("erp_txtPAYEE_BANK").send_keys("654321")
driver.find_element_by_id("erp_txtPAYEE_FULL_NAME").send_keys("银河装备")
driver.find_element_by_id("erp_txtADVANCES_REASON").send_keys("租金")
driver.find_element_by_id("erp_txtMEMO").send_keys("租金")
driver.find_element_by_id("erp_cmbADVANCES_ATTR_TYPE").click()
driver.airtest_touch(Template(r"tpl1597394517213.png", record_pos=(3.355, 4.395), resolution=(100, 100)))
driver.airtest_touch(Template(r"tpl1595216371565.png", record_pos=(7.775, 2.75), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595216415181.png", record_pos=(11.535, 3.105), resolution=(100, 100)), "保存成功")
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.assert_template(Template(r"tpl1595216500600.png", record_pos=(10.69, 8.12), resolution=(100, 100)), "显示下一步审批人员")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1597394909944.png", record_pos=(4.08, 2.685), resolution=(100, 100)), "提交成功，进入直属领导审批")
time.sleep(1)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
common.quit(driver)
#提交成功，注销
# 登录何英
common.login(driver,"heying")
driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()

driver.assert_template(Template(r"tpl1594979205529.png", record_pos=(7.03, 1.05), resolution=(100, 100)), "进入待审批的借款申请单")
time.sleep(3) 
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1594979338707.png", record_pos=(11.45, 2.245), resolution=(100, 100)), "提交成功")
time.sleep(3) 
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部

common.quit(driver)
#登录谭义账号进行审批预付款申请单
common.login(driver,"tanyi")
driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()

driver.assert_template(Template(r"tpl1594979205529.png", record_pos=(7.03, 1.05), resolution=(100, 100)), "进入待审批的借款申请单")
time.sleep(3) 
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.assert_template(Template(r"tpl1594979286766.png", record_pos=(8.04, 7.955), resolution=(100, 100)), "下滑到底部")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1594979338707.png", record_pos=(11.45, 2.245), resolution=(100, 100)), "提交成功")
time.sleep(3) 
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部

common.quit(driver)
#登录王岳账号
common.login(driver,"wangyue")
driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()

driver.assert_template(Template(r"tpl1594979205529.png", record_pos=(7.03, 1.05), resolution=(100, 100)), "进入待审批的借款申请单")
time.sleep(3) 
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.assert_template(Template(r"tpl1594979780545.png", record_pos=(8.165, 7.965), resolution=(100, 100)), "滑动至底部")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1594979828900.png", record_pos=(11.525, 2.23), resolution=(100, 100)), "提交成功")
common.quit(driver)
#登录李邦特账号
common.login(driver,"libangte")
driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1594979205529.png", record_pos=(7.03, 1.05), resolution=(100, 100)), "进入待审批的借款申请单")
time.sleep(3) 
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.assert_template(Template(r"tpl1594980270366.png", record_pos=(8.075, 7.96), resolution=(100, 100)), "滑动至底部")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1594980311042.png", record_pos=(11.465, 2.26), resolution=(100, 100)), "提交成功")
common.quit(driver)
#登录陈国媚账号
common.login(driver,"chenguomei")
driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1594979205529.png", record_pos=(7.03, 1.05), resolution=(100, 100)), "进入待审批的借款申请单")
time.sleep(3) 
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
common.quit(driver)
#登录陈伟强账号
common.login(driver,"chenweiqiang")
driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1594979205529.png", record_pos=(7.03, 1.05), resolution=(100, 100)), "进入待审批的借款申请单")
time.sleep(3) 
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595214426769.png", record_pos=(13.285, 2.68), resolution=(100, 100)), "审批结束")
driver.close()
auto_setup(__file__)