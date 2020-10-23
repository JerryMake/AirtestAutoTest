# -*- encoding=utf8 -*-
__author__ = "janson"
#新增出差申请单
from airtest.core.api import using
using(r"E:\黄振旭\费用管理系统自动化测试用例\conf\common.air")
from common import common
from airtest.core.api import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome

# 加载驱动
driver = WebChrome()
driver.implicitly_wait(20)
driver.get("http://14.21.59.70:1000/")
driver.maximize_window()#放大浏览器

# 登录黄振旭
common.login(driver,"huangzhenxu")
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/ul/div[2]/li/ul/div/a/li/span").click()
driver.assert_template(Template(r"tpl1594806824724.png", record_pos=(10.395, 1.93), resolution=(100, 100)), "进入出差申请单")
driver.airtest_touch(Template(r"tpl1594806856010.png", record_pos=(10.62, 2.76), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1594806903770.png", record_pos=(11.045, 2.605), resolution=(100, 100)), "进入新增出差申请单界面")
driver.find_element_by_xpath("//*[@id=\"erp_cmbTRAVEL_FROM_PLACE\"]/div/div/input").click()
driver.airtest_touch(Template(r"tpl1594807757859.png", record_pos=(10.455, 4.745), resolution=(100, 100)))

driver.airtest_touch(Template(r"tpl1594807773681.png", record_pos=(12.275, 4.745), resolution=(100, 100)))

driver.find_element_by_xpath("//*[@id=\"erp_cmbTRAVEL_TO_PLACE\"]/div/div/input").click()
driver.assert_template(Template(r"tpl1594806994034.png", record_pos=(11.92, 4.2), resolution=(100, 100)), "选择出发地")
driver.find_element_by_xpath("//*[@id=\"erp_cmbTRAVEL_TO_PLACE\"]/div/div/input").click()
driver.airtest_touch(Template(r"tpl1594807757859.png", record_pos=(10.455, 4.745), resolution=(100, 100)))

driver.airtest_touch(Template(r"tpl1594807773681.png", record_pos=(12.275, 4.745), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1594807036893.png", record_pos=(15.575, 4.205), resolution=(100, 100)), "选择目的地")
driver.find_element_by_id("erp_cmbTRAVEL_WAY").click()
driver.airtest_touch(Template(r"tpl1594807956116.png", record_pos=(7.25, 4.575), resolution=(100, 100)))

driver.assert_template(Template(r"tpl1594807104688.png", record_pos=(15.22, 4.085), resolution=(100, 100)), "选择出行方式")
driver.find_element_by_xpath("//input[@placeholder='选择出差开始日期']").click()
driver.airtest_touch(Template(r"tpl1594807219148.png", target_pos=4, record_pos=(10.94, 6.49), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1594807242155.png", record_pos=(8.975, 4.26), resolution=(100, 100)), "选择出差开始日期")
driver.find_element_by_xpath("//input[@placeholder='选择出差结束日期']").click()
driver.airtest_touch(Template(r"tpl1594807219148.png", target_pos=4, record_pos=(10.94, 6.49), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1594807290793.png", record_pos=(12.67, 4.265), resolution=(100, 100)), "选择出差结束日期")
driver.assert_template(Template(r"tpl1594807319932.png", record_pos=(15.78, 4.26), resolution=(100, 100)), "出差天数为1")
driver.find_element_by_id("erp_txtTRAVEL_ESTIMATED_COST").clear()
driver.find_element_by_id("erp_txtTRAVEL_ESTIMATED_COST").send_keys("100")
driver.airtest_touch(Template(r"tpl1594864100831.png", target_pos=2, record_pos=(9.135, 5.39), resolution=(100, 100)))
driver.airtest_touch(Template(r"tpl1594864142480.png", record_pos=(9.11, 6.145), resolution=(100, 100)))

driver.airtest_touch(Template(r"tpl1594863790721.png", target_pos=6, record_pos=(8.58, 5.785), resolution=(100, 100)))
driver.find_element_by_xpath("//label[@for='TRAVEL_USRS']").click()

driver.assert_template(Template(r"tpl1594864176887.png", record_pos=(8.59, 5.295), resolution=(100, 100)), "选择出差人员")


driver.find_element_by_id("erp_txtTRAVEL_REASON").send_keys("出差")
driver.find_element_by_id("erp_txtMEMO").send_keys("出差备注")
driver.assert_template(Template(r"tpl1594807471705.png", record_pos=(8.62, 6.205), resolution=(100, 100)), "验证是否填写")
driver.find_element_by_xpath("//*[@id=\"pane-detail\"]/div/div/div/div/button/span").click()
driver.assert_template(Template(r"tpl1594807510525.png", record_pos=(15.215, 1.39), resolution=(100, 100)), "提示保存成功")
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("意见")
driver.assert_template(Template(r"tpl1594807589090.png", record_pos=(8.98, 8.11), resolution=(100, 100)), "填写意见")

driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[5]/div/div/div/button/span").click()
sleep(2)
driver.assert_template(Template(r"tpl1597391483131.png", record_pos=(4.075, 2.675), resolution=(100, 100)), "进入直属领导审批")


common.quit(driver)
# 登录何英进行审批
common.login(driver,"heying")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1595401467730.png", record_pos=(2.77, 0.875), resolution=(100, 100)), "进入审批界面")
time.sleep(1)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.assert_template(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)),"显示提交按钮")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1597391749323.png", record_pos=(4.15, 2.705), resolution=(100, 100)), "进入部门负责人审批")
common.quit(driver)
# 登录谭义进行审批
common.login(driver,"tanyi")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1595401467730.png", record_pos=(2.77, 0.875), resolution=(100, 100)), "进入审批界面")
time.sleep(1)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595214426769.png", record_pos=(13.285, 2.68), resolution=(100, 100)), "审批结束")
common.quit(driver)
driver.close()


auto_setup(__file__)