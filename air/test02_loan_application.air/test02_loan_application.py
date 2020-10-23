# -*- encoding=utf8 -*-
__author__ = "janson"
# 提交出差借款借款申请单，进入审核流程，有影响，使用huangzhenxu
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
#登录黄振旭账号
common.login(driver,"huangzhenxu")
common.create_loan(driver)
driver.close()

auto_setup(__file__)