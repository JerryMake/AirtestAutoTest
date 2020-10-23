# -*- encoding=utf8 -*-
__author__ = "janson"
from airtest.core.api import *
# 查看借还款界面
from airtest.core.api import *
using(r"E:\黄振旭\费用管理系统自动化测试用例\conf\common.air")
from common import common
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)

driver.get("http://14.21.59.70:1000")
driver.maximize_window()#放大浏览器
common.login(driver,"huangzhenxu")
driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")
driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/ul/div[3]/li/ul/div/a/li/span").click()
driver.assert_template(Template(r"tpl1594869543864.png", record_pos=(10.415, 1.0), resolution=(100, 100)), "进入借还款追踪管理")
driver.close()

auto_setup(__file__)