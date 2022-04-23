# # def test01_login(self, uiauto2=uiautomator2):
# #     print('------------------开始执行登录----------------------')
# #
# #
# #     try:
# #         driver = self.driver
# #         # 点击手机号登录
# #         driver.find_element(By.ID, 'com.netease.cloudmusic:id/login').click()
# #         time.sleep(3)
# #
# #         # 同意隐私协议
# #         driver.find_element(By.ID, 'com.netease.cloudmusic:id/positiveBtn').click()
# #         time.sleep(10)
# #
# #         # 点击输入框
# #         driver.find_element(By.ID, 'com.netease.cloudmusic:id/cellphone').click()
# #         driver.find_element(By.ID, 'com.netease.cloudmusic:id/cellphone').clear()
# #         time.sleep(10)
# #
# #         # 输入手机号
# #         driver.find_element(By.ID, 'com.netease.cloudmusic:id/cellphone').send_keys('17600555113')
# #         time.sleep(10)
# #
# #         # 点击下一步
# #         driver.find_element(By.ID, 'com.netease.cloudmusic:id/next').click()
# #         time.sleep(10)
# #
# #         # 点击密码登录
# #         driver.find_element(By.ID, 'com.netease.cloudmusic:id/passwordLoginBtn').click()
# #         # 输入密码
# #         time.sleep(10)
# #         driver.find_element(By.ID, 'com.netease.cloudmusic:id/password').send_keys('Cloud0508')
# #         time.sleep(10)
# #
# #         # 点击登录
# #         driver.find_element(By.ID, 'com.netease.cloudmusic:id/login').click()
# #         time.sleep(10)
# #
# #         # 断言首页内容证明登录成功
# #
# #         try:
# #             # 排行榜获取
# #             onetitleranking_list = driver.find_element(By.ID, 'com.netease.cloudmusic:id/portalV3Title3')
# #             time.sleep(5)
# #
# #             if onetitleranking_list:
# #                 with open(case_result, 'w') as result1:
# #                     driver.implicitly_wait(5)
# #                     result1.write("# 登录执行完毕\n")
# #                     result1.close()
# #                     print("# 登录成功执行完毕")
# #             else:
# #                 pass
# #
# #
# #         except:
# #
# #             raise Exception('登录失败')
# #
# #
# #         # app 重新启动
# #         try:
# #             uiauto = uiauto2.connect_usb("a41168bc")
# #             uiauto.app_start('com.netease.cloudmusic')
# #
# #         except:
# #
# #             raise Exception("启动失败")
# #
# #
# #     except:
# #
# #         raise Exception("登录用例执行失败")
#
#
# # 检查私人fm播放页面展示正确case
# def test01_playmusic(self):
#     global casenumber
#     casenumber += 1
#
#     print(f'------------------开始执行case{casenumber}------------------------')
#
#     try:
#
#         try:
#             driver = self.driver
#             driver.find_element(By.ID, 'com.netease.cloudmusic:id/portalV3Title2').click()  # 点击私人FM”
#             driver.implicitly_wait(5)
#             like = driver.find_element(By.ID, 'com.netease.cloudmusic:id/likeBtn')
#             driver.implicitly_wait(5)
#             nolike = driver.find_element(By.ID, 'com.netease.cloudmusic:id/trashBtn')
#
#         except:
#             raise Exception('红心和非红心元素查找失败')
#
#         try:
#             if like and nolike:
#                 with open(case_result, 'w') as result1:
#                     driver.implicitly_wait(5)
#                     result1.write(f"# case:{casenumber}私人FM播放页面展示正确\n")
#                     print("# 私人FM播放页面展示正确")
#                     result1.close()
#
#             else:
#                     print(f'------------------结束执行case{casenumber}------------------------')
#         except:
#
#             raise Exception("私人FM播放页面展示错误")
#
#
#     except:
#
#         with open(case_result, 'w') as result1:
#             driver.implicitly_wait(5)
#             result1.write(f"# case:{casenumber}私人FM播放页面展示错误\n")
#             result1.close()
#             print("私人FM播放页面展示正确用例执行失败")
#         raise Exception('私人FM播放页面展示正确用例执行失败！')
#
#
#
# #  检查今日推荐页面展示正确
# def test02_todayrecommend(self, uiauto2=uiautomator2):
#     global casenumber
#     casenumber += 1
#
#     print(f'------------------开始执行case{casenumber}-----------------------')
#
#     try:
#
#         # app 重新启动
#         try:
#             uiauto = uiauto2.connect_usb("a41168bc")
#             uiauto.app_start('com.netease.cloudmusic')
#
#         except:
#
#             raise Exception("启动失败")
#
#         # 用例步骤执行
#         try:
#             # 点击今日推荐龙珠
#             driver = self.driver
#             driver.find_element(By.ID, 'com.netease.cloudmusic:id/portalV3Title1').click()  # 点击今日推荐龙珠
#             time.sleep(5)
#
#             # 获取今日元素
#             todaylucky = driver.find_element(By.ID, 'com.netease.cloudmusic:id/tv_res_title')
#
#             # 获取历史日推元素
#             time.sleep(5)
#             historyrecommend = driver.find_element(By.ID, 'com.netease.cloudmusic:id/tv_pendant_historyEntry')
#
#         except:
#
#             raise Exception("元素获取失败")
#
#         # 断言获取元素是否存在
#         try:
#             if todaylucky and historyrecommend:
#                 with open(case_result, 'a') as result1:
#                     driver.implicitly_wait(5)
#                     result1.write(f"# case:{casenumber}今日推荐播放页面展示正确1\n")
#                     print("# 今日推荐页面展示正确")
#                     result1.close()
#
#             else:
#                 with open(case_result, 'a') as result1:
#                     driver.implicitly_wait(5)
#                     result1.write(f"# case:{casenumber}今日推荐页面展示错误")
#                     result1.close()
#                     print(f'------------------结束执行case{casenumber}------------------------')
#
#         except:
#
#             raise Exception("今日推荐元素和历史日推元素没找到")
#
#     except:
#
#         with open(case_result, 'a') as result1:
#             driver.implicitly_wait(5)
#             result1.write(f"# case:{casenumber}今日推荐页面展示错误")
#             result1.close()
#
#         raise Exception('检查今日推荐页面展示正用例执行失败！')
#
#
#
# # 检查排行榜页面展示正确
# def test03_rankinglist(self, uiauto2=uiautomator2):
#     global casenumber
#     casenumber += 1
#
#     print(f'------------------开始执行case{casenumber}-----------------------')
#
#     try:
#         # app重新启动
#         try:
#             uiauto = uiauto2.connect_usb("a41168bc")
#             uiauto.app_start('com.netease.cloudmusic')
#
#         except:
#             raise Exception("启动失败")
#
#         # 执行用例+获取排行榜页面标题+精选tab+曲风
#         try:
#             driver = self.driver
#             # 点击排行榜
#             driver.find_element(By.ID, 'com.netease.cloudmusic:id/portalV3Title3').click()
#             time.sleep(5)
#             # 获取排行榜
#             titleranking_list = driver.find_element_by_android_uiautomator('new UiSelector().text("排行榜")')
#             time.sleep(5)
#             # 获取精选类型
#             concentration = driver.find_element_by_android_uiautomator('new UiSelector().text("精选")')
#             time.sleep(5)
#             # 获取全球类型
#             globalstyle = driver.find_element_by_android_uiautomator('new UiSelector().text("曲风")')
#
#         except:
#
#             raise Exception("排行榜页面精选、曲风tab获取失败")
#
#         try:
#             if titleranking_list and concentration and globalstyle:
#                 with open(case_result, 'a') as result1:
#                     driver.implicitly_wait(5)
#                     result1.write(f"# case:{casenumber}排行榜页面展示正确\n")
#                     print("# 排行榜页面展示正确")
#                     result1.close()
#             else:
#                 with open(case_result, 'a') as result1:
#                     driver.implicitly_wait(5)
#                     result1.write(f"# case:{casenumber}排行榜页面展示错误\n")
#                     result1.close()
#                     print(f'------------------结束执行case{casenumber}------------------------')
#
#         except:
#
#             raise Exception("排行榜页面精选、曲风tab断言失败")
#
#     except:
#
#         with open(case_result, 'a') as result1:
#             driver.implicitly_wait(5)
#             result1.write(f"# case:{casenumber}排行榜页面展示错误\n")
#             result1.close()
#
#         raise Exception("检查排行榜页面展示正确case 执行失败")
#
#
#
# # 检查点击热门话题可以进入热门话题页面
# def test04_hothuati(self, uiauto2=uiautomator2):
#
#     try:
#         driver = self.driver
#         global casenumber
#         casenumber += 1
#
#         print(f'------------------开始执行case{casenumber}-----------------------')
#
#         try:
#             uiauto = uiauto2.connect_usb("a41168bc")
#             uiauto.app_start('com.netease.cloudmusic')
#
#         except:
#             raise Exception("app启动失败！")
#
#         try:
#             # 执行case步骤 滑动找到模块+点击话题内容
#             time.sleep(2)
#             driver.swipe(429, 1553, 507, 390)
#
#             # 点击热门话题资源
#             time.sleep(2)
#             driver.tap([(99, 1287), (961, 1419)])
#
#         except:
#
#             raise Exception("热门话题未找到！")
#
#         try:
#             # 断言全部内容title
#             allTranslation = driver.find_element(By.XPATH, '//android.widget.LinearLayout[@content-desc="全部内容"]/android.widget.TextView')
#             if allTranslation:
#                 with open(case_result, 'a') as result1:
#                     driver.implicitly_wait(5)
#                     result1.write(f"# case:{casenumber}话题资源页面内容展示正确\n")
#                     print("# 检查话题资源页面内容展示正确")
#                     result1.close()
#
#             else:
#                 with open(case_result, 'a') as result1:
#                     driver.implicitly_wait(5)
#                     result1.write(f"# case:{casenumber}检查话题资源页面内容展示错误")
#                     result1.close()
#                     print(f'------------------结束执行case{casenumber}------------------------')
#
#
#         except:
#
#             raise Exception("检查话题资源页面内容展示错误")
#
#
#     except:
#
#         with open(case_result, 'a') as result1:
#             driver.implicitly_wait(5)
#             result1.write(f"# case:{casenumber}检查话题资源页面内容展示错误")
#             result1.close()
#
#         raise Exception("检查话题资源页面内容用例展示错误")

# 检查点击歌单龙珠可以进入歌单广场