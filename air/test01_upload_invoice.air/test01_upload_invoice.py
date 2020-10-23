# -*- encoding=utf8 -*-
__author__ = "janson"
#上传、搜索、查看、删除发票
from airtest.core.api import *
from airtest.core.api import using
using(r"E:\黄振旭\费用管理系统自动化测试用例\conf\common.air")
from common import common
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome   

driver = WebChrome()
driver.maximize_window()#放大浏览器
driver.get("http://14.21.59.70:1000/#/mrp/base/warehouseList")
common.login(driver,"huangzhenxu")

driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/ul/div/li/ul/div/a/li/span").click() #进入【上传发票】页面
driver.assert_template(Template(r"tpl1594800342361.png", record_pos=(7.415, 2.15), resolution=(100, 100)), "成功打开发票管理页面")
driver.airtest_touch(Template(r"tpl1594800381828.png", record_pos=(7.82, 2.985), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1594800422516.png", record_pos=(13.66, 4.545), resolution=(100, 100)), "打开识别发票接界面")
driver.airtest_touch(Template(r"tpl1594800605536.png", record_pos=(15.805, 6.9), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1594800624394.png", record_pos=(12.86, 1.925), resolution=(100, 100)), "提示请选择文件上传")
driver.find_element_by_name("file").send_keys("E:\\黄振旭\\下载内容\\机打发票.jpg")
driver.airtest_touch(Template(r"tpl1594800605536.png", record_pos=(15.805, 6.9), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1594801016639.png", record_pos=(13.32, 4.715), resolution=(100, 100)), "提示请选择发票类型")
driver.find_element_by_xpath("//*[@id=\"erp_cmbINVOICE_TYPE\"]/div/div/input").click() #点击发票类型
driver.assert_template(Template(r"tpl1594800495329.png", record_pos=(13.825, 6.28), resolution=(100, 100)), "打开下来框")
driver.airtest_touch(Template(r"tpl1594800515615.png", record_pos=(13.405, 7.275), resolution=(100, 100)))
driver.airtest_touch(Template(r"tpl1594800605536.png", record_pos=(15.805, 6.9), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1594801086480.png", record_pos=(8.285, 2.79), resolution=(100, 100)), "成功识别发票")
driver.airtest_touch(Template(r"tpl1594800463611.png", record_pos=(15.655, 4.72), resolution=(100, 100)))
driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[4]/span").click()  #选择“其他发票”
driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/form/div/div[1]/div/div[2]/div/div/div/input").send_keys("0003")    #输入发票代号0003
driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/form/div/div[1]/div/div[6]/div/div/div/input").send_keys("9144040066154040XN")  #输入识别号
driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/form/div[1]/div[1]/div/div[5]/div/div/div/input").clear()
driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/form/div[1]/div[1]/div/div[5]/div/div/div/input").send_keys("广东兆邦智能科技股份有限公司")   #输入“购方名称”
driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div/div/button/span").click()
driver.assert_template(Template(r"tpl1597387226130.png", record_pos=(4.21, 5.28), resolution=(100, 100)), "提示核对单据")
driver.airtest_touch(Template(r"tpl1597387268429.png", record_pos=(5.83, 5.805), resolution=(100, 100)))


time.sleep(2)
driver.airtest_touch(Template(r"tpl1594804957684.png", record_pos=(17.02, 4.69), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1594801086480.png", record_pos=(8.285, 2.79), resolution=(100, 100)), "查看发票")
driver.airtest_touch(Template(r"tpl1594805648832.png", record_pos=(18.085, 7.335), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1594800342361.png", record_pos=(7.415, 2.15), resolution=(100, 100)), "返回发票管理")
driver.find_element_by_xpath("//input[@placeholder='请输入发票流水号']").send_keys("0003")
driver.airtest_touch(Template(r"tpl1594806105937.png", record_pos=(10.55, 2.375), resolution=(100, 100)))
driver.assert_template(Template(r"tpl1594882830282.png", record_pos=(15.505, 4.335), resolution=(100, 100)), "查询成功")

common.delete_invoice(driver)
driver.close()

auto_setup(__file__)