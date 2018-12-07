# -*- coding:utf-8 -*-

__author__ = 'Tianc'


def checkVersion(currentversion, expectedversion):
    """
    检查版本号是否相同，当前版本小于期望版本则进行升级，大于等于则忽略。
    CODE有两种，88和99 表示建议，88表示当前版本大于等于期待的版本忽略，99表示小于期待版本要进行升级。
    :param currentversion: 当前系统存在的版本号
    :param expectedversion: 期望的版本号
    :return: CODE, MAX_VERSION
    """

    MAX_VERSION = "0.0.0"
    CODE = 88

    # 如果两者一样就直接返回，用于加快处理速度。 这里不要用 is 要用 == 来比较内容是否一致。
    if expectedversion == currentversion:
        CODE = 88
        MAX_VERSION = expectedversion
        return CODE, MAX_VERSION

    # 切割成列表
    currentversionBITS = currentversion.split(".")
    expectedversionBITS = expectedversion.split(".")

    """
    为了避免版本号长度不同比如  1.0.8和1.2 我们把版本号要补全都变成相同长度，比如 1.2.0 这样比较的时候循环次数相同
    """
    if len(currentversionBITS) >= len(expectedversionBITS):
        amount = len(currentversionBITS) - len(expectedversionBITS)
        for i in range(amount):
            expectedversionBITS.append("0")
    else:
        amount = len(expectedversionBITS) - len(currentversionBITS)
        for i in range(amount):
            currentversionBITS.append("0")

    """
    逐位比较版本大小，为什么这里采用currentversionBITS的长度来循环呢，其实讲过上面的if语句后无论是currentversionBITS还是expectedversionBITS
    位数都相同，这里采用那个长度来控制循环都可以。
    """
    for i in range(len(currentversionBITS)):
        try:
            if int(currentversionBITS[i]) > int(expectedversionBITS[i]):
                CODE = 88
                MAX_VERSION = currentversion
                return CODE, MAX_VERSION
            elif int(currentversionBITS[i]) < int(expectedversionBITS[i]):
                CODE = 99
                MAX_VERSION = expectedversion
                return CODE, MAX_VERSION
            else:
                CODE = 88
                MAX_VERSION = expectedversion
        except IndexError as err:
            pass

    return CODE, MAX_VERSION
