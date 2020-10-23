# -*- encoding=utf8 -*-
__author__ = "Administrator"
# 新增费用报销申请单（冲账），进入审批流程，有影响，需要上传一张发票，需要已付款的借款申请单，使用heying
from airtest.core.api import *
import unittest
using(r"E:\黄振旭\费用管理系统自动化测试用例\conf\common.air")
from common import common
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome


driver = WebChrome()
driver.implicitly_wait(20)
driver.get("http://14.21.59.70:1000")
driver.maximize_window()#放大浏览器
        
print("登录黄振旭账号")
common.login(driver,"huangzhenxu")
common.create_loan(driver)
print("登录夏子霞")
common.login(driver,"xiazixia")
common.pay_loan(driver)
sleep(2)
common.quit(driver)
print("登录何英账号")
common.login(driver,"huangzhenxu")
print("上传一张发票")
common.upload_invoice(driver)
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/ul/div[4]/li/ul/div/a/li/span").click()
driver.assert_template(Template(r"tpl1595484957475.png", record_pos=(11.275, 0.975), resolution=(100, 100)), "进入费用报销申请单界面")
driver.airtest_touch(Template(r"tpl1595484997538.png", record_pos=(10.46, 1.81), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595485017525.png", record_pos=(9.765, 1.565), resolution=(100, 100)), "进入新增费用报销界面")
driver.find_element_by_id("erp_txtMEMO").send_keys("报销租金")
driver.airtest_touch(Template(r"tpl1595485120532.png", record_pos=(9.64, 1.79), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595485135763.png", record_pos=(15.045, 0.82), resolution=(100, 100)), "提示保存成功")
driver.assert_template(Template(r"tpl1595485175400.png", record_pos=(9.59, 5.37), resolution=(100, 100)), "显示报销明细")
driver.airtest_touch(Template(r"tpl1595485196897.png", record_pos=(9.665, 5.575), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595485239882.png", record_pos=(0.345, 1.96), resolution=(100, 100)), "进入创建明细界面")
driver.find_element_by_id("erp_txtCOST_USE").send_keys("报销租金")
driver.find_element_by_xpath("//input[@placeholder='选择费用发生日期']").click()
driver.airtest_touch(Template(r"tpl1595485303451.png", record_pos=(3.605, 5.96), resolution=(100, 100)))
driver.find_element_by_id("erp_cmbPAY_MODE").click()
print("选择冲账")
driver.airtest_touch(Template(r"tpl1595485376721.png", record_pos=(1.915, 5.615), resolution=(100, 100)))
driver.airtest_touch(Template(r"tpl1595485556579.png", target_pos=6, record_pos=(16.67, 4.73), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595485587537.png", record_pos=(0.0, 4.03), resolution=(100, 100)), "进入选择借款单界面")
driver.airtest_touch(Template(r"tpl1595485636356.png", record_pos=(9.34, 5.81), resolution=(100, 100)))
driver.airtest_touch(Template(r"tpl1595485419740.png", record_pos=(0.86, 6.255), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595485435707.png", record_pos=(0.525, 2.255), resolution=(100, 100)), "进入选择发票界面")
driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/form/div[3]/div[4]/div[2]/table/tbody/tr/td/div/label/span/span").click()
driver.airtest_touch(Template(r"tpl1595486594974.png", record_pos=(17.83, 8.5), resolution=(100, 100)))
driver.find_element_by_xpath("//input[@aria-valuenow='12258.97']").clear()
driver.find_element_by_xpath("//input[@aria-valuenow='undefined']").send_keys("1000")
driver.airtest_touch(Template(r"tpl1595486627082.png", record_pos=(17.74, 8.47), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595486710541.png", record_pos=(14.62, 0.93), resolution=(100, 100)), "提示保存成功")
driver.find_element_by_name("file").send_keys("E:\\黄振旭\\下载内容\\机打发票.jpg")   #上传发票
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.airtest_touch(Template(r"tpl1595486897613.png", record_pos=(9.72, 6.36), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595486919512.png", record_pos=(14.465, 0.81), resolution=(100, 100)), "提示操作成功")
driver.execute_script('window.scrollTo(0,0)')    #滑到顶部
driver.airtest_touch(Template(r"tpl1595486627082.png", record_pos=(17.74, 8.47), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595487095708.png", record_pos=(14.6, 0.935), resolution=(100, 100)), "提示保存成功")
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.assert_template(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)), "显示提交按钮")
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("提交意见")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595487151134.png", record_pos=(12.995, 2.27), resolution=(100, 100)), "提交成功，进入部门负责人审核")
common.quit(driver)
print("登录谭义进行审批")
common.login(driver,"tanyi")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1595487349381.png", record_pos=(9.5, 1.065), resolution=(100, 100)), "进入审批界面")
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.assert_template(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)), "显示提交按钮")
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("提交意见")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595487443021.png", record_pos=(13.175, 2.25), resolution=(100, 100)), "审批成功，进入费用所属部门/项目审批")
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.assert_template(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)), "显示提交按钮")
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("提交意见")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595487524149.png", record_pos=(12.9, 2.25), resolution=(100, 100)), "审批成功，进入费用会计标准")
common.quit(driver)
print("登录王岳进行审批")
common.login(driver,"wangyue","111111")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1595487349381.png", record_pos=(9.5, 1.065), resolution=(100, 100)), "进入审批界面")
time.sleep(1)
driver.execute_script('window.scrollTo(0,400)')   #滑到400的位置
driver.airtest_touch(Template(r"tpl1595231823112.png", record_pos=(2.29, 4.65), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595231835240.png", record_pos=(3.645, 1.865), resolution=(100, 100)), "进入发票检验页面")
driver.airtest_touch(Template(r"tpl1595231863516.png", record_pos=(13.825, 8.73), resolution=(100, 100)))
driver.execute_script('window.scrollTo(0,0)')    #滑到顶部
driver.airtest_touch(Template(r"tpl1595229065206.png", record_pos=(2.195, 1.705), resolution=(100, 100)))
time.sleep(1)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("意见")
driver.assert_template(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)),"显示提交按钮")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
common.quit(driver)
print("登录李邦特账号，审批")
common.login(driver,"libangte")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1595487349381.png", record_pos=(9.5, 1.065), resolution=(100, 100)), "进入审批界面")
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("意见")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595234585754.png", record_pos=(8.6, 2.495), resolution=(100, 100)), "审批成功，进入下一节点")
common.quit(driver)
print("登录陈国媚进行审批")
common.login(driver,"chenguomei")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1595487349381.png", record_pos=(9.5, 1.065), resolution=(100, 100)), "进入审批界面")
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.airtest_touch(Template(r"tpl1595213823428.png", target_pos=4, record_pos=(12.16, 8.805), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595236089746.png", record_pos=(5.53, 8.41), resolution=(100, 100)), "勾选成功")
driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("意见")
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595235508777.png", record_pos=(7.55, 2.5), resolution=(100, 100)), "提交成功")
common.quit(driver)
print("登录陈伟强账号进行审批")
common.login(driver,"chenweiqiang")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1595487349381.png", record_pos=(9.5, 1.065), resolution=(100, 100)), "进入审批界面")
time.sleep(3) 
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595214218910.png", record_pos=(8.665, 2.51), resolution=(100, 100)), "提交成功")
common.quit(driver)
print("登录吴希文账号")
common.login(driver,"wuxiwen")
driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
driver.assert_template(Template(r"tpl1595487349381.png", record_pos=(9.5, 1.065), resolution=(100, 100)), "进入审批界面")
time.sleep(1)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1595214426769.png", record_pos=(13.285, 2.68), resolution=(100, 100)), "审批结束")
driver.close()
        

auto_setup(__file__)









