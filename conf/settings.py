# coding = utf-8
# author:chenjq
import os
# ---------------------------------基础类型设置-------------------------------------------
deviceType = "web"                                                             # 设备类别：app、win和web
devices = ['Windows:///9176942']                            		# 设备信息，只有当deviceType为app是有效，decices 在Airtest运行过程中可以在控制台看到
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))         # 工程根目录
air_path = os.path.join(root_path, 'air')                                        # 脚本目录（由根目录和air拼接：root/air）
log_path = os.path.join(root_path, 'log')                                         # 日志目录
template_path = os.path.join(root_path, 'template')                                # 测试报告模板目录
report_path = os.path.join(root_path, 'report')                                    # 测试报告路径
data_path = os.path.join(root_path, 'data')                                     # 测试数据目录
template_name = "summary_template.html"                                          # 测试报告模板名称
clear_report = True                                                            # 是否清空旧测试报告
# -------------------------------------邮箱设置-------------------------------------------
send_email_path = "XXXXXXX@qq.com"                                           # 发送方邮件
receive_email_path = "XXXXXXX@qq.com"                                        # 接收方邮件
email_authorization_code = "XXXXXXXXXX"                                   # 发送方邮件授权码
message_title = "自动化测试报告"                                                # 邮件标题
