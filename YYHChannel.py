# -*- coding:utf-8 -*-
import re
import time

from selenium.webdriver.common.by import By

from AppConfig import apk_path, apk_update_info, apk_version
from ChromeUtil import set_url

__author__ = 'Tianc'

'''
应用汇渠道
'''

driver = set_url('http://dev.appchina.com/dev/manage/app/upgrade/1122135')
driver.find_element_by_class_name('layer-close').click()  # 关闭应用认证弹窗


def start_update_file():
    driver.find_element_by_name('file').send_keys(apk_path)  # 上传文件
    time.sleep(2)
    status = driver.find_element_by_class_name('button-text')  # 获取上传状态

    while True:
        time.sleep(3)
        if status.text != '' and status.text == '上传成功':
            print('上传完成：', status.text)
            update_file_success()
            break
        elif status.text != '上传中' or status.text == '正在解包，请耐心等待':
            print('正在上传：', status.text)
        else:
            print(status.text)


def update_file_success():
    iframe = driver.find_element(By.ID, 'updateinfo_ifr')
    driver.switch_to.frame(iframe)
    update_info = driver.find_element_by_id('tinymce')
    update_info.clear()  # 清空原有更新信息
    update_info.send_keys(apk_update_info)  # 编辑更新信息
    driver.switch_to.parent_frame()  # 从子frame切回到父frame
    driver.switch_to.default_content()  # 切到frame中之后，我们便不能继续操作主文档的元素，这时如果想操作主文档内容，则需切回主文档。
    driver.find_element_by_xpath("//input[@type='submit']").click()  # 点击上传按钮


if __name__ == '__main__':
    start_update_file()
