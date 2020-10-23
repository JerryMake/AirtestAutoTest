# -*- encoding=utf8 -*-
__author__ = "janson"


from airtest.core.api import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome

class common():
    # 通用函数
    def login(driver,username,password="zxcvbn"):
        u'''输入用户名和密码,点击登录'''
        driver.assert_exist("//input[@tabindex='1']", "xpath", "验证账号输入框是否存在")
        driver.find_element_by_xpath("//input[@tabindex='1']").clear()
        driver.find_element_by_xpath("//input[@tabindex='1']").send_keys(username)
        driver.find_element_by_xpath("//input[@tabindex='2']").clear()
        driver.find_element_by_xpath("//input[@tabindex='2']").send_keys(password)
        driver.find_element_by_xpath("//*[@id=\"app\"]/div/form/button/span").click()
        time.sleep(2)
        driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")
        
    def quit(driver):
        # 注销
        driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div/div[1]/div[3]/div[6]/div/div/img").click()
        driver.assert_template(Template(r"tpl1594978895167.png", record_pos=(17.755, 2.2), resolution=(100, 100)), "显示注销")
        driver.airtest_touch(Template(r"tpl1594978895167.png", record_pos=(17.755, 2.2), resolution=(100, 100)))
        
    def pay_loan(driver):
        # 支付借款
        driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/ul/div[5]/li/ul/div/a/li/span").click()
        driver.assert_template(Template(r"tpl1595321987970.png", record_pos=(9.58, 1.13), resolution=(100, 100)), "进入付款页面")
        driver.airtest_touch(Template(r"tpl1595322027149.png", record_pos=(17.1, 3.345), resolution=(100, 100)))
        driver.assert_template(Template(r"tpl1595322041190.png", record_pos=(10.525, 4.17), resolution=(100, 100)), "进入上传付款凭证")
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/form/div[1]/div/div/div/div/input").click()
        driver.airtest_touch(Template(r"tpl1597734608434.png", record_pos=(4.745, 6.965), resolution=(100, 100)))

        driver.airtest_touch(Template(r"tpl1595322076668.png", target_pos=6, record_pos=(12.25, 4.55), resolution=(100, 100)))
        driver.assert_template(Template(r"tpl1595322095187.png", record_pos=(7.815, 3.485), resolution=(100, 100)), "进入选择科目")
        driver.airtest_touch(Template(r"tpl1595322114247.png", record_pos=(16.665, 5.29), resolution=(100, 100)))
        driver.find_element_by_name("file").send_keys("E:\\黄振旭\\下载内容\\机打发票.jpg")
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/div/button/span").click()
        driver.assert_template(Template(r"tpl1595322185516.png", record_pos=(14.5, 0.875), resolution=(100, 100)), "提示操作成功")
        
    def confirm_repayment(driver):
        # 确认还款
        driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/ul/div[5]/li/ul/div[2]/a/li/span").click()
        driver.assert_template(Template(r"tpl1595319649907.png", record_pos=(9.585, 1.13), resolution=(100, 100)), "进入确认还款")
        driver.airtest_touch(Template(r"tpl1595319672560.png", record_pos=(17.05, 3.345), resolution=(100, 100)))
        driver.assert_template(Template(r"tpl1595473780838.png", record_pos=(7.35, 4.265), resolution=(100, 100)), "进入上传收款回执")

        driver.airtest_touch(Template(r"tpl1595319731654.png", target_pos=6, record_pos=(12.76, 4.8), resolution=(100, 100)))
        driver.assert_template(Template(r"tpl1595319752203.png", record_pos=(7.8, 3.475), resolution=(100, 100)), "进入选择科目")
        driver.airtest_touch(Template(r"tpl1595319769752.png", record_pos=(16.66, 5.295), resolution=(100, 100)))
        time.sleep(2)
        driver.find_element_by_name("file").send_keys("E:\\黄振旭\\下载内容\\机打发票.jpg")
        driver.airtest_touch(Template(r"tpl1595319847882.png", record_pos=(14.075, 6.06), resolution=(100, 100)))
        driver.assert_template(Template(r"tpl1595474007697.png", record_pos=(14.945, 0.86), resolution=(100, 100)), "提示操作成功")
        
    def upload_invoice(driver,Invoice_code=str(time.time())):
        # 上传发票
        driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/ul/div/li/ul/div/a/li/span").click() #进入【上传发票】页面
        driver.assert_template(Template(r"tpl1594800342361.png", record_pos=(7.415, 2.15), resolution=(100, 100)), "成功打开发票管理页面")
        driver.airtest_touch(Template(r"tpl1594800381828.png", record_pos=(7.82, 2.985), resolution=(100, 100)))
        driver.assert_template(Template(r"tpl1594800422516.png", record_pos=(13.66, 4.545), resolution=(100, 100)), "打开识别发票接界面")
        driver.find_element_by_name("file").send_keys("E:\\黄振旭\\下载内容\\机打发票.jpg")
        driver.find_element_by_xpath("//*[@id=\"erp_cmbINVOICE_TYPE\"]/div/div/input").click() #点击发票类型
        driver.assert_template(Template(r"tpl1594800495329.png", record_pos=(13.825, 6.28), resolution=(100, 100)), "打开下来框")
        driver.airtest_touch(Template(r"tpl1594800515615.png", record_pos=(13.405, 7.275), resolution=(100, 100)))
        driver.airtest_touch(Template(r"tpl1594800605536.png", record_pos=(15.805, 6.9), resolution=(100, 100)))
        driver.assert_template(Template(r"tpl1594801086480.png", record_pos=(8.285, 2.79), resolution=(100, 100)), "成功识别发票")
        driver.airtest_touch(Template(r"tpl1594800463611.png", record_pos=(15.655, 4.72), resolution=(100, 100)))
        driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[4]/span").click()  # 选择“其他发票”
        driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/form/div/div[1]/div/div[2]/div/div/div/input").send_keys(Invoice_code)    # 输入发票代号Invoice_code
        driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/form/div/div[1]/div/div[6]/div/div/div/input").send_keys("9144040066154040XN")  # 输入识别号
        driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/form/div[1]/div[1]/div/div[5]/div/div/div/input").clear()
        driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/form/div[1]/div[1]/div/div[5]/div/div/div/input").send_keys("广东兆邦智能科技股份有限公司")   # 输入“购方名称”
        driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div/div/button/span").click()
        driver.assert_template(Template(r"tpl1597395951858.png", record_pos=(3.815, 4.715), resolution=(100, 100)), "提示核对发票信息")
        driver.airtest_touch(Template(r"tpl1597395994711.png", record_pos=(5.815, 5.8), resolution=(100, 100)))


        
    def delete_invoice(driver):
        # 删除发票
        driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/ul/div/li/ul/div/a/li/span").click() #进入【上传发票】页面
        driver.assert_template(Template(r"tpl1594800342361.png", record_pos=(7.415, 2.15), resolution=(100, 100)), "成功打开发票管理页面")
        
        driver.airtest_touch(Template(r"tpl1594804318156.png", target_pos=9, record_pos=(16.6, 4.17), resolution=(100, 100)))
        driver.assert_template(Template(r"tpl1594804346304.png", record_pos=(12.42, 5.24), resolution=(100, 100)), "删除提醒")
        driver.airtest_touch(Template(r"tpl1594804371587.png", record_pos=(14.785, 5.68), resolution=(100, 100)))
        driver.assert_template(Template(r"tpl1594804380204.png", record_pos=(14.075, 1.34), resolution=(100, 100)), "提示删除成功")
        
    def create_loan(driver):
        # 银河装备人员提交出差借款申请单进行审核
        driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")
        driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/ul/div[3]/li/ul/div[2]/a/li/span").click()
        driver.assert_template(Template(r"tpl1594869915353.png", record_pos=(10.275, 1.0), resolution=(100, 100)), "进入借款申请单")
        driver.airtest_touch(Template(r"tpl1594869936750.png", record_pos=(10.49, 1.835), resolution=(100, 100)))
        driver.assert_template(Template(r"tpl1594869946851.png", record_pos=(9.805, 1.6), resolution=(100, 100)), "进入新增页面")
        driver.airtest_touch(Template(r"tpl1594870014188.png", record_pos=(10.93, 4.31), resolution=(100, 100)))
        driver.airtest_touch(Template(r"tpl1597389349872.png", record_pos=(3.49, 6.075), resolution=(100, 100)))

        driver.assert_template(Template(r"tpl1597389365481.png", record_pos=(2.915, 4.5), resolution=(100, 100)), "选择出差借款")


        driver.find_element_by_id("erp_txtLOAN_AMOUNT").clear()
        driver.find_element_by_id("erp_txtLOAN_AMOUNT").send_keys("1000")
        driver.airtest_touch(Template(r"tpl1594870113653.png", record_pos=(17.17, 4.315), resolution=(100, 100)))
        driver.airtest_touch(Template(r"tpl1594870123790.png", target_pos=6, record_pos=(17.29, 6.435), resolution=(100, 100)))
        driver.assert_template(Template(r"tpl1594870138930.png", record_pos=(16.69, 4.2), resolution=(100, 100)), "选择还款日期")
        driver.assert_template(Template(r"tpl1594870164177.png", record_pos=(10.91, 4.705), resolution=(100, 100)), "自动匹配借方科目")
        driver.find_element_by_id("erp_txtLOAN_REASON").send_keys("租金")
        driver.find_element_by_id("erp_txtMEMO").send_keys("租金")
        driver.airtest_touch(Template(r"tpl1594870224535.png", record_pos=(9.71, 1.825), resolution=(100, 100)))
        driver.assert_template(Template(r"tpl1594867309884.png", record_pos=(14.975, 0.84), resolution=(100, 100)), "提示保存成功")
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
        time.sleep(2) 
        driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("填写意见后点击提交")
        driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
        time.sleep(2)
        driver.execute_script('window.scrollTo(0,0)')    #滑到顶部
        common.quit(driver)
        # 登录何英
        common.login(driver,"heying")
        driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")
        driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()

        driver.assert_template(Template(r"tpl1594979205529.png", record_pos=(7.03, 1.05), resolution=(100, 100)), "进入待审批的借款申请单")
        time.sleep(3) 
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
        driver.assert_template(Template(r"tpl1597388142563.png", record_pos=(7.24, 6.84), resolution=(100, 100)), "下滑到底部显示审批状态")
        driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("填写意见后点击提交")
        driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
        driver.assert_template(Template(r"tpl1597388688257.png", record_pos=(4.15, 1.69), resolution=(100, 100)), "提交成功，进入部门负责人节点")

        common.quit(driver)
        
        # 登录谭义账号
        common.login(driver,"tanyi")
        driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")
        driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()

        driver.assert_template(Template(r"tpl1594979205529.png", record_pos=(7.03, 1.05), resolution=(100, 100)), "进入待审批的借款申请单")
        time.sleep(3) 
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
        driver.assert_template(Template(r"tpl1597388142563.png", record_pos=(7.24, 6.84), resolution=(100, 100)), "下滑到底部显示审批状态")
        driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("填写意见后点击提交")
        driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
        driver.assert_template(Template(r"tpl1597388239499.png", record_pos=(3.87, 2.65), resolution=(100, 100)), "提交成功，进入成本会计节点")
        common.quit(driver)
        #登录王岳账号
        common.login(driver,"wangyue")
        driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")
        driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()

        driver.assert_template(Template(r"tpl1594979205529.png", record_pos=(7.03, 1.05), resolution=(100, 100)), "进入待审批的借款申请单")
        time.sleep(3) 
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
        driver.assert_template(Template(r"tpl1594979780545.png", record_pos=(8.165, 7.965), resolution=(100, 100)), "滑动至底部")
        driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("填写意见后点击提交")
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
        driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("填写意见后点击提交")
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
        driver.airtest_touch(Template(r"tpl1595213823428.png", target_pos=4, record_pos=(12.16, 8.805), resolution=(100, 100)))
        driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[4]/div/div/div/div/input").send_keys("填写意见后点击提交")
        driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
        common.quit(driver)
        #登录陈伟强账号
        common.login(driver,"chenweiqiang")
        driver.assert_exist("//*[@id=\"tags-view-container\"]/div/div/div/span", "xpath", "验证是否登录进入主页.")
        driver.find_element_by_xpath("//*[@id=\"dashboard\"]/form/div/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr/td[2]/div/span").click()
        driver.assert_template(Template(r"tpl1594979205529.png", record_pos=(7.03, 1.05), resolution=(100, 100)), "进入待审批的借款申请单")
        sleep(3) 
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')   #滑到底部
        driver.find_element_by_xpath("//*[@id=\"pane-first\"]/form/div[2]/div/div/div/div/input").send_keys("填写意见后点击提交")
        driver.airtest_touch(Template(r"tpl1595490704194.png", record_pos=(1.755, 9.28), resolution=(100, 100)))
        driver.assert_template(Template(r"tpl1595214426769.png", record_pos=(13.285, 2.68), resolution=(100, 100)), "审批结束")
        common.quit(driver)
        






auto_setup(__file__)