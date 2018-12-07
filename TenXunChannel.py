# -*- coding:utf-8 -*-
import re
import time

from AppConfig import apk_path, apk_update_info, apk_version, apk_version_code
from ChromeUtil import set_url

__author__ = 'Tianc'

'''
腾讯渠道
'''

driver = set_url('http://op.open.qq.com/mobile_appinfov2/apkinfo?appid=1101043674')
driver.find_element_by_name('file').send_keys(apk_path)  # 上传文件
time.sleep(2)
update_info = driver.find_element_by_name('update_des')
update_info.clear()  # 清空原有更新信息
update_info.send_keys(apk_update_info)  # 编辑更新信息

while True:
    time.sleep(3)  # 5秒查询一次是否有上传完成提示
    try:
        result_message = driver.find_element_by_id('mode_tips_v2').text  # 上传信息
        print('result_message', result_message)
        break
    except Exception as e:
        error = ''
        print('上传中，请等待...')

if result_message != '上传成功！':
    print('error:', result_message)
else:
    print('上传成功------')
    driver.find_element_by_id('j-submit-all-btn').click()  # 提交更新
