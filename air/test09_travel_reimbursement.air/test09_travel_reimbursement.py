# -*- encoding=utf8 -*-
__author__ = "janson"
# 差旅报销申请单审批流程
from airtest.core.api import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
using(r"E:\黄振旭\费用管理系统自动化测试用例\conf\common.air")
from common import common


driver = WebChrome()
driver.implicitly_wait(20)
driver.get("http://14.21.59.70:1000/")
driver.maximize_window()#放大浏览器


# 登录黄振旭账号，提交差旅报销申请单
common.login(driver,"huangzhenxu")
driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")


common.upload_invoice(driver) # 上传一张发票
driver.airtest_touch(Template(r"tpl1597398632931.png", record_pos=(0.36, 7.65), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595237905970.png", record_pos=(9.16, 1.595), resolution=(100, 100)), "打开差旅报销申请单")
driver.airtest_touch(Template(r"tpl1595238021979.png", record_pos=(9.275, 2.43), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595238038956.png", record_pos=(8.545, 2.035), resolution=(100, 100)), "进入新增页面")
driver.airtest_touch(Template(r"tpl1595238520371.png", target_pos=4, record_pos=(7.775, 4.005), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595238613863.png", record_pos=(3.855, 4.43), resolution=(100, 100)), "进入选择出差申请单界面")
driver.airtest_touch(Template(r"tpl1595238654302.png", record_pos=(14.395, 5.615), resolution=(100, 100)))
driver.find_element_by_id("erp_txtMEMO").send_keys("租金")

driver.airtest_touch(Template(r"tpl1595238805466.png", record_pos=(2.18, 2.125), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595238835098.png", record_pos=(13.135, 1.555), resolution=(100, 100)), "提示保存成功")
driver.assert_template(Template(r"tpl1595469277807.png", record_pos=(13.305, 2.33), resolution=(100, 100)), "保存成功")
time.sleep(1)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("审批意见")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1597398883604.png", record_pos=(4.07, 2.675), resolution=(100, 100)), "提交成功，进入直属领导审批")
common.quit(driver)
# 登录何英
common.login(driver,"heying")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1595469628616.png", record_pos=(9.655, 1.54), resolution=(100, 100)), "进入审批界面")
sleep(1)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("审批意见")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1597399235536.png", record_pos=(4.16, 2.695), resolution=(100, 100)), "提交成功，进入部门负责审批")
common.quit(driver)

# 登录谭义
common.login(driver,"tanyi")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1595469628616.png", record_pos=(9.655, 1.54), resolution=(100, 100)), "进入审批界面")
time.sleep(1)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("审批意见")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1597399461148.png", record_pos=(4.095, 2.69), resolution=(100, 100)), "提交成功，进入费用会计核准")
time.sleep(1)
common.quit(driver)
# 登录王岳，进行审批
common.login(driver,"wangyue")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1595469628616.png", record_pos=(9.655, 1.54), resolution=(100, 100)), "进入审批界面")
time.sleep(1)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("审批意见")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595470234039.png", record_pos=(8.66, 2.5), resolution=(100, 100)), "审批成功，进入财务副总监审批")
common.quit(driver)
# 登录李邦特，进入审批
common.login(driver,"libangte")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1595469628616.png", record_pos=(9.655, 1.54), resolution=(100, 100)), "进入审批界面")
time.sleep(1)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("审批意见")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595470903523.png", record_pos=(8.62, 2.495), resolution=(100, 100)), "审批成功，进入财务总监审批")
common.quit(driver)
# 登录陈国媚，进行审批
common.login(driver,"chenguomei")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1595469628616.png", record_pos=(9.655, 1.54), resolution=(100, 100)), "进入审批界面")
time.sleep(1)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[2]/div/div/div/div/input").send_keys("审批意见")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595471773029.png", record_pos=(8.48, 2.485), resolution=(100, 100)), "审批结束")
driver.close()
auto_setup(__file__)