from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# from appium.webdriver.extensions.android.nativekey import AndroidKey
from app_information import desired_caps  # 导入被测试app的信息
import uiautomator2
import unittest, time, re

case_result = '/Users/yuanxinming/python_demo/NeteaseMusice-main/NeteaseHomework/result3.html'

# case 条数
casenumber = 0


class NeteaseCloudMusic(unittest.TestCase):

    # 连接Appium Server，初始化自动化环境
    def setUp(self) -> None:
        self.driver = webdriver.Remote('http://10.242.83.84:4723/wd/hub', desired_caps)
        # 设置缺省等待时间
        self.driver.implicitly_wait(20)
        self.verificationErrors = []  # 脚本运行时，错误的信息将被打印到这个列表中#
        self.accept_next_alert = True  # 是否继续接受下一个警告#


    def test05_muscilist(self, uiauto2=uiautomator2):
        try:
            try:
                driver = self.driver
                global casenumber
                casenumber += 1

                uiauto2 = uiauto2.connect_usb('a41168bc')
                uiauto2.app_start('com.netease.cloudmusic')

            except:

                raise Exception('app启动失败')

            print(f'------------------开始执行case{casenumber}-----------------------')

            try:
                # 点击首页龙珠歌单
                time.sleep(10)
                driver.tap([(512, 755)], 100)


                # 检查官方tab存在
                driver.implicitly_wait(5)
                officialmusiclist = driver.find_element(By.XPATH,
                                                        '//android.view.ViewGroup[@content-desc="官方"]/android.widget.TextView')

                # 检查精品歌单存在
                driver.implicitly_wait(5)
                elitemusictab = driver.find_element(By.XPATH,
                                                    '//android.view.ViewGroup[@content-desc="精品"]/android.widget.TextView')

                # 判断共享歌单
                driver.implicitly_wait(5)
                sharetab = driver.find_element(By.XPATH,
                                               '//android.view.ViewGroup[@content-desc="共享歌单"]/android.widget.TextView')

            except:

                raise Exception('获取歌单广场的元素失败')

            try:

                if officialmusiclist and elitemusictab and sharetab:
                    with open(case_result, 'a') as result1:
                        driver.implicitly_wait(5)
                        result1.write(f"# case:{casenumber}歌单广场页面展示正确\n")
                        print("# 歌单广场页面展示正确")
                        result1.close()

                else:
                    with open(case_result, 'a') as result1:
                        driver.implicitly_wait(5)
                        result1.write(f"# case:{casenumber}检查话题资源页面内容展示错误")
                        result1.close()
                        print(f'------------------结束执行case{casenumber}------------------------')

            except:

                raise Exception('判断歌单广场元素失败')

        except:

            with open(case_result, 'a') as result1:
                driver.implicitly_wait(5)
                result1.write(f"# case:{casenumber}检查话题资源页面内容展示错误")
                result1.close()
                print('检查点击歌单龙珠可以进入歌单广场用例执行失败')
