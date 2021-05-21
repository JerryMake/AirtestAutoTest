# AirtestAutoTest
基于Airtest的自动化测试框架，生成测试报告，并通过邮件发送报告。
Based on airtest, the automatic test framework generates test reports and sends reports by email.
# -----------------------------------------------------------------
2021-5-10 21:26 Beijingtime
由于有的小伙伴遇到了运行时的报错：AttributeError: 'Namespace' object has no attribute 'no_image'
这是Airtest的更新造成的，新版本的runner.py文件的setup_by_args()添加了一个参数“no_image”，用来控制是否在运行期间保存屏幕截图。
我们直接注释掉这个参数就好。具体解释请看我的博客：https://blog.csdn.net/hzx18022464374/article/details/116611680
# -----------------------------------------------------------------
2021-5-10 22:08 Beijingtime
关于遇到报错就停止执行剩余用例的问题
找到pthon\Lib\site-packages\airtest\cli\runner.py
将run_script（）中的sys.exit(-1)更换成raise AssertionError。

# -----------------------------------------------------------------
2021-5-10 22:14 Beijingtime
关于运行过程中提示：ModuleNotFoundError No module named 'HTMLTestRunner'
这是缺少HTMLTestRunner.py造成的，具体解决方法请看博客：https://blog.csdn.net/weixin_37579123/article/details/84900157
