from airtest.cli.runner import AirtestCase,run_script
import airtest.report.report as report

from conf.send_email import send_email
from conf.settings import *
from argparse import *
import shutil,os,io,jinja2,datetime
from lib.common import RetryFunc
from lib import video
from airtest.core.helper import device_platform
from airtest.core.api import auto_setup, log, connect_device


class Air_Case_Handler(AirtestCase):
    def __init__(self,dev_id):
        ''' 初始化，如果是web直接通过，如果不是，传入设备id
        connect_device 连接该设备
        '''
        super(Air_Case_Handler, self).__init__()
        if deviceType.upper() == "WEB":
            pass
        else:
            self.dev = connect_device(dev_id)

    def setUp(self):
        # 程序开始前
        super(Air_Case_Handler, self).setUp()

    def tearDown(self):
        # 程序开始后
        super(Air_Case_Handler,self).tearDown()


    def run_air(self,air_dir,device):
        ''' 跑用例'''
        start_time = datetime.datetime.now()
        start_time_fmt = start_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        # 结果数组，下面用到
        results = []
        root_log = log_path
        # 判断该路径是否为目录
        if os.path.isdir(root_log):
            # shutil.rmtree() 表示递归删除文件夹下的所有子文件夹和子文件
            shutil.rmtree(root_log)

        else:
            # os.makedirs() 方法用于递归创建目录。
            os.makedirs(root_log)

        # 返回指定目录下的所有文件和目录名，通过file进行循环
        for file in os.listdir(air_path):
            # 如果file中结尾带了“.air”
            if file.endswith(".air"):
                airName = file
                # 把“.air”换成空格,因为airtest自动生成的文件名带.air
                airDirName = file.replace(".air","")
                # root\air\xxx.air，每个用例的脚本路径
                script = os.path.join(air_dir,file)
                # root\log\\xxx,每个用例的测试报告
                air_log = os.path.join(root_path,"log\\" + airDirName)
                 # 如果air_log是目录，删除其目录下的子目录及文件夹
                if os.path.isdir(air_log):
                    # print(air_log)
                    shutil.rmtree(air_log)

                else:
                    os.makedirs(air_log)
                # html每个用例测试报告（html文件）存放的路径，root\log\\xxx\log.html
                html = os.path.join(air_log,"log.html")
                if deviceType.upper() == "WEB":
                    args = Namespace(device=[],log=air_log, recording=None, script=script,language="zh",compress=0)
                elif deviceType.upper() == "APP":
                    args = Namespace(device=device, log = air_log, recording=airDirName+".mp4", script=script,language="zh",compress=0)
                else:
                    args = Namespace(device=device, log=air_log, recording=None, script=script,language="zh",compress=0)
                try:
                    run_script(args,AirtestCase) # airtest的run方法
                except AssertionError as e:
                    pass
                finally:
                    # 将脚本路径和测试报告（截图）路径用report.py的LogToHtml生成html文件
                    rpt = report.LogToHtml(script, air_log)
                    # "log_template.html"报告名称，输出文件是HTML文件
                    rpt.report("log_template.html", output_file=html)
                    result = {}
                    result["name"] = airName.replace('.air', '')
                    result["result"] = rpt.test_result
                    results.append(result)

        end_time = datetime.datetime.now()
        end_time_fmt = end_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]


        duration = (end_time - start_time).seconds

        # jinja2是python的模板引擎（语法），loader模板加载器，FileSystemLoader从文件目录中获取模板
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_path),
            extensions=(),
            autoescape=True
        )

        template = env.get_template(template_name, template_path)
        project_name = root_path.split("\\")[-1]
        success = 0
        fail = 0
        for res in results:
            if res['result']:
                success += 1
            else:
                fail += 1
        report_name = "report_"+end_time.strftime("%Y%m%d%H%M%S")+".html"
        html = template.render({"results": results,"device":device,"stime":start_time_fmt,'etime':end_time_fmt,'duration':duration,"project":project_name,"success":success,"fail":fail})
        output_file = os.path.join(root_path,"report" ,report_name)
        with io.open(output_file, 'w', encoding="utf-8") as f:
            f.write(html)

if __name__ == "__main__":
    for device in devices:
        test = Air_Case_Handler(device)
        test.run_air(air_path,device)

    # 发送测试报告到邮箱
    email = send_email()
    new_report = email.new_report(report_path)
    email.send_mail(new_report)
