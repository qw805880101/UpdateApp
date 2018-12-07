# -*- coding:utf-8 -*-
import os
import time

from selenium.webdriver.common.by import By

from AppConfig import apk_path, apk_update_info, apk_version, apk_version_code
from ChromeUtil import set_url

__author__ = 'Tianc'

'''
360应用渠道
'''

driver = set_url('http://dev.360.cn/mod3/mobileapp/?qid=819538888&appid=201495736')

time.sleep(2)


# 切换到frame中查找元素
def switch_to_frame():
    iframe = driver.find_element(By.NAME, 'iframe0')
    driver.switch_to.frame(iframe)


# 开始上传文件
def start_update_file():
    switch_to_frame()

    driver.find_element_by_class_name('btn-link ').click()

    driver.find_element_by_link_text('点击进行下载').click()

    time.sleep(2)

    os.system(r'D:\pythonProjects\UpdateApp\aut\flash_mouse.exe')  # 执行自动点击允许flash插件

    time.sleep(2)

    switch_to_frame()

    driver.find_element_by_class_name('btn-link ').click()

    update = driver.find_element_by_id('SWFUpload_0')

    update.click()

    time.sleep(1)

    update.click()

    time.sleep(2)

    os.system(
        r'D:\pythonProjects\UpdateApp\aut\update_file.exe %s' % apk_path)

    time.sleep(4)

    status = driver.find_element_by_class_name('progressBarStatus')

    while True:
        time.sleep(3)
        if status.text != '上传中...' and status.text == '上传应用文件成功':
            print('上传完成:', status.text)
            update_file_success()
            break
        else:
            print('上传失败:', status.text)
            # driver.quit()


# 上传apk文件成功
def update_file_success():
    update_info = driver.find_element_by_id('desc_desc')
    update_info.clear()  # 清空原有更新信息
    update_info.send_keys(apk_update_info)  # 编辑更新信息
    time.sleep(2)
    # driver.find_element_by_id('submitform').click()  # 点击提交审核
    # driver.quit()


if __name__ == '__main__':
    start_update_file()
