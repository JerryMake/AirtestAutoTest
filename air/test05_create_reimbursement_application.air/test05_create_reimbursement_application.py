# -*- encoding=utf8 -*-
__author__ = "janson"
# 新增招待申请单
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
# 登录黄振旭，提交招待申请单
common.login(driver,"huangzhenxu")
driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/ul/div[2]/li/ul/div[2]/a/li/span").click()
driver.assert_template(Template(r"tpl1594866810340.png", record_pos=(8.64, 1.08), resolution=(100, 100)), "打开【招待申请单】")
driver.airtest_touch(Template(r"tpl1594866859370.png", record_pos=(8.87, 1.925), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1594867550086.png", record_pos=(9.55, 2.37), resolution=(100, 100)), "进入新增页面")
driver.airtest_touch(Template(r"tpl1594867580071.png", target_pos=4, record_pos=(12.415, 3.975), resolution=(100, 100)))

driver.assert_template(Template(r"tpl1594866964820.png", record_pos=(8.41, 1.275), resolution=(100, 100)), "选择人员")
driver.airtest_touch(Template(r"tpl1594866998339.png", record_pos=(17.14, 4.035), resolution=(100, 100)))

driver.find_element_by_xpath("//input[@placeholder='选择招待日期']").click()
driver.airtest_touch(Template(r"tpl1594867092167.png", target_pos=6, record_pos=(17.3, 5.43), resolution=(100, 100)))
driver.find_element_by_id("erp_txtSERVE_ESTIMATED_COST").clear()
driver.find_element_by_id("erp_txtSERVE_ESTIMATED_COST").send_keys("500")
driver.airtest_touch(Template(r"tpl1594867171110.png", record_pos=(9.37, 4.33), resolution=(100, 100)))
driver.airtest_touch(Template(r"tpl1594867195573.png", record_pos=(9.365, 5.445), resolution=(100, 100)))
driver.airtest_touch(Template(r"tpl1594868096187.png", record_pos=(10.215, 4.73), resolution=(100, 100)))
driver.find_element_by_xpath("//*[@id=\"erp_txtSERVE_GUESTS\"]").send_keys("招待对象")
driver.find_element_by_id("erp_txtSERVE_REASON").send_keys("招待事由是项目需要")
driver.find_element_by_id("erp_txtMEMO").send_keys("备注是项目需求")
driver.airtest_touch(Template(r"tpl1594867292758.png", record_pos=(8.125, 1.83), resolution=(100, 100)))
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("填写意见后点击提交")
time.sleep(3) 
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1597393154148.png", record_pos=(4.1, 2.685), resolution=(100, 100)), "进入直属领导审批")

common.quit(driver)
# 登录何英账号进行审批
common.login(driver,"heying")
driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1595317631518.png", record_pos=(11.405, 0.985), resolution=(100, 100)), "进入审批界面")
time.sleep(1)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1597393362838.png", record_pos=(4.14, 2.695), resolution=(100, 100)), "进入部门负责人审批")

common.quit(driver)
# 登录谭义进行审批
common.login(driver,"tanyi")
driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1595317631518.png", record_pos=(11.405, 0.985), resolution=(100, 100)), "进入审批界面")
time.sleep(1)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595214426769.png", record_pos=(13.285, 2.68), resolution=(100, 100)), "审批结束")
driver.close()
auto_setup(__file__)