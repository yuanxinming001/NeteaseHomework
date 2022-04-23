## 对测试用例的执行进行以下说明

- app_information.py是被测APP的信息
- start_appium.py是启动Appium(必须是服务端appium，桌面端的话需要手动打开appium，不然读取不到配置（java_home、adk）)
- test_NeteaseCloudMusic.py是执行测试用例（执行前一定要保持没有账号登录）
- tescases.py是测试用例

## 执行顺序

- 运行start_appium.py
- 运行test_NeteaseCloudMusic.py

## 文件说明

- appium_log记录Appium的启动情况
- test_result.txt记录断言结果
