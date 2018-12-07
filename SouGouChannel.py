# -*- coding:utf-8 -*-
import re
import time

from AppConfig import apk_path, apk_update_info, apk_version
from ChromeUtil import set_url

__author__ = 'Tianc'

'''
搜狗应用渠道
'''

driver = set_url('http://zhushou.sogou.com/open/app/update.html?id=25590')
driver.find_element_by_name('file').send_keys(apk_path)  # 上传文件
time.sleep(2)
update_info = driver.find_element_by_name('update_info')
update_info.clear()  # 清空原有更新信息
update_info.send_keys(apk_update_info)  # 编辑更新信息
apkInfo = driver.find_element_by_class_name('info').text  # apk信息模块
error = driver.find_element_by_class_name('error')  # 错误信息


def get_version():
    apk = re.findall(r'版本名称:([^;]+)', apkInfo.replace('\n', ';').replace(' ', ''))[0]  # 获取页面apk_version
    return int(apk.replace(".", ""))


apk_info = get_version()
print(apk_version > apk_info)

while True:
    if apk_version == apk_info:
        break
    if error.text is not '':
        break
    time.sleep(3)  # 5秒查询一次版本号 根据版本号判断是否上传成功
    apk_info = get_version()
    print('new_apk_version', apk_info)

if error.text is not '':
    print('error:', error.text)
else:
    print('上传成功------')
    driver.find_element_by_id('submit').click()  # 提交更新
