# -*- encoding=utf8 -*-
__author__ = "janson"
# 填写费用报销申请单
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
# 登录黄振旭账号，填写费用报销申请单
common.login(driver,"huangzhenxu")
common.upload_invoice(driver) #上传一张发票
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[1]/div[2]/div[1]/div/ul/div[4]/li/ul/div[2]/a/li/span").click()
driver.assert_template(Template(r"tpl1595228936982.png", record_pos=(2.895, 0.88), resolution=(100, 100)), "进入费用报销申请单")
driver.airtest_touch(Template(r"tpl1595228967476.png", record_pos=(2.99, 1.69), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595228980833.png", record_pos=(2.275, 1.495), resolution=(100, 100)), "进入新增页面")
driver.find_element_by_id("erp_txtMEMO").send_keys("租金")
driver.airtest_touch(Template(r"tpl1595229065206.png", record_pos=(2.195, 1.705), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595229087417.png", record_pos=(8.795, 2.07), resolution=(100, 100)), "保存成功")
driver.execute_script('window.scrollTo(0,400)')   #滑到400的位置
driver.airtest_touch(Template(r"tpl1595229365733.png", record_pos=(2.165, 1.915), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595229377593.png", record_pos=(3.475, 2.005), resolution=(100, 100)), "进入创建界面")
driver.find_element_by_id("erp_txtCOST_USE").send_keys("租金")
driver.find_element_by_xpath("//input[@placeholder='选择费用发生日期']").click()
driver.airtest_touch(Template(r"tpl1595229619678.png", record_pos=(11.95, 5.84), resolution=(100, 100)))
driver.find_element_by_id("erp_txtPAYEE_BANK_ACCOUNT").send_keys("123456")
driver.find_element_by_id("erp_txtPAYEE_BANK").send_keys("654321")
driver.find_element_by_id("erp_txtPAYEE_FULL_NAME").send_keys("银河装备")
driver.airtest_touch(Template(r"tpl1595229764986.png", record_pos=(7.785, 6.725), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595229777006.png", record_pos=(7.525, 2.225), resolution=(100, 100)), "进入选择发票页面")
driver.airtest_touch(Template(r"tpl1597396242568.png", record_pos=(3.67, 4.43), resolution=(100, 100)))
driver.airtest_touch(Template(r"tpl1595229917858.png", record_pos=(17.34, 8.525), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595229959071.png", record_pos=(12.14, 7.1), resolution=(100, 100)), "成功选择发票")
driver.airtest_touch(Template(r"tpl1595230039783.png", record_pos=(17.775, 8.485), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595230046647.png", record_pos=(15.02, 1.065), resolution=(100, 100)), "提示保存成功")
driver.assert_exist("//*[@id=\"erp_tableContactsList\"]/div/div[3]/table/tbody/tr/td/div/span", "xpath", "添加成功.")
driver.execute_script('window.scrollTo(0,0)')    #滑到顶部
driver.airtest_touch(Template(r"tpl1595229065206.png", record_pos=(2.195, 1.705), resolution=(100, 100)))
time.sleep(1)
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("意见")
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1597396399487.png", record_pos=(4.095, 2.695), resolution=(100, 100)), "提交成功，进入直属领导审批")
common.quit(driver)
# 登录何英
common.login(driver,"heying")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1597396986141.png", record_pos=(0.97, 1.495), resolution=(100, 100)), "进入费用报销申请单")
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("意见")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
time.sleep(1)
driver.assert_template(Template(r"tpl1595230422776.png", record_pos=(8.675, 2.48), resolution=(100, 100)), "提交成功")
common.quit(driver)
#登录谭义账号，审批申请单
common.login(driver,"tanyi")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div[1]/div/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1597396986141.png", record_pos=(0.97, 1.495), resolution=(100, 100)), "进入费用报销申请单")
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("意见")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595231560328.png", record_pos=(7.525, 2.435), resolution=(100, 100)), "审批成功2")
common.quit(driver)
#登录王岳账号，审批
common.login(driver,"wangyue")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div[1]/div/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1595231363381.png", record_pos=(4.99, 1.93), resolution=(100, 100)), "进入审批界面")
time.sleep(1)
driver.execute_script('window.scrollTo(0,400)')   #滑到400的位置
driver.airtest_touch(Template(r"tpl1595231823112.png", record_pos=(2.29, 4.65), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1597397648545.png", record_pos=(3.375, 5.28), resolution=(100, 100)), "核验成功")

driver.execute_script('window.scrollTo(0,0)')    #滑到顶部
driver.airtest_touch(Template(r"tpl1595229065206.png", record_pos=(2.195, 1.705), resolution=(100, 100)))
time.sleep(1)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("意见")
driver.assert_template(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)),"显示提交按钮")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
common.quit(driver)
#登录李邦特账号，审批
common.login(driver,"libangte")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1597396986141.png", record_pos=(0.97, 1.495), resolution=(100, 100)), "进入费用报销申请单")
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("意见")
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595234585754.png", record_pos=(8.6, 2.495), resolution=(100, 100)), "审批成功，进入下一节点")
common.quit(driver)
# 登录陈国媚账号，审批
common.login(driver,"chenguomei")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1597396986141.png", record_pos=(0.97, 1.495), resolution=(100, 100)), "进入费用报销申请单")
time.sleep(1)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.airtest_touch(Template(r"tpl1595213823428.png", target_pos=4, record_pos=(12.16, 8.805), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595236089746.png", record_pos=(5.53, 8.41), resolution=(100, 100)), "勾选成功")

driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("意见")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595235508777.png", record_pos=(7.55, 2.5), resolution=(100, 100)), "提交成功")

common.quit(driver)
#登录陈伟强账号
common.login(driver,"chenweiqiang")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1597396986141.png", record_pos=(0.97, 1.495), resolution=(100, 100)), "进入费用报销申请单")
time.sleep(3) 
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595214218910.png", record_pos=(8.665, 2.51), resolution=(100, 100)), "提交成功")
common.quit(driver)
#登录吴希文账号
common.login(driver,"wuxiwen")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1597396986141.png", record_pos=(0.97, 1.495), resolution=(100, 100)), "进入费用报销申请单")
time.sleep(1)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595214426769.png", record_pos=(13.285, 2.68), resolution=(100, 100)), "审批结束")

driver.close()

auto_setup(__file__)