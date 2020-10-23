# -*- encoding=utf8 -*-
__author__ = "Administrator"
#撤回并作废借款申请单
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
# 登录何英，提交借款单
common.login(driver,"heying")
driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/ul/div[3]/li/ul/div[2]/a/li/span").click()
driver.assert_template(Template(r"tpl1595381252824.png", record_pos=(9.86, 1.125), resolution=(100, 100)), "进入借款单页面")
driver.airtest_touch(Template(r"tpl1595381273465.png", record_pos=(10.055, 1.96), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595381296421.png", record_pos=(9.375, 1.75), resolution=(100, 100)), "进入新增借款单界面")
driver.find_element_by_xpath("//*[@id=\"erp_cmbLOAN_TYPE_ID\"]/div/div/input").click()
driver.airtest_touch(Template(r"tpl1597391204520.png", record_pos=(3.49, 6.075), resolution=(100, 100)))
driver.find_element_by_id("erp_txtLOAN_AMOUNT").clear()
driver.find_element_by_id("erp_txtLOAN_AMOUNT").send_keys("1000")
driver.find_element_by_xpath("//input[@placeholder='选择预计还款日期']").click()
driver.airtest_touch(Template(r"tpl1595381535711.png", record_pos=(17.185, 6.565), resolution=(100, 100)))
driver.find_element_by_id("erp_txtLOAN_REASON").send_keys("事由租金")
driver.find_element_by_id("erp_txtMEMO").send_keys("备注租金")
driver.airtest_touch(Template(r"tpl1595383208112.png", record_pos=(9.25, 1.96), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595383320737.png", record_pos=(13.19, 2.94), resolution=(100, 100)), "保存成功")
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595383928011.png", record_pos=(13.515, 2.775), resolution=(100, 100)), "提交成功")
driver.airtest_touch(Template(r"tpl1595383949879.png", record_pos=(9.37, 1.58), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595383969091.png", record_pos=(9.445, 1.575), resolution=(100, 100)), "返回主页")
driver.airtest_touch(Template(r"tpl1595383989903.png", record_pos=(16.725, 6.495), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595384003651.png", record_pos=(12.85, 5.16), resolution=(100, 100)), "弹出提示")
driver.airtest_touch(Template(r"tpl1595384019505.png", record_pos=(15.35, 5.77), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595384038643.png", record_pos=(17.18, 3.105), resolution=(100, 100)), "撤销成功")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1595381252824.png", record_pos=(9.86, 1.125), resolution=(100, 100)), "进入借款单页面")
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("作废")
driver.airtest_touch(Template(r"tpl1595384306362.png", record_pos=(11.535, 9.315), resolution=(100, 100)))

driver.assert_template(Template(r"tpl1595384171338.png", record_pos=(13.005, 2.33), resolution=(100, 100)), "作废成功")

driver.close()



auto_setup(__file__)