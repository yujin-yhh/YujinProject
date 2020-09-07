'''
主页

'''
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from YujinProject.test_appium.pages.addresslist_page import AddressListPage
from YujinProject.test_appium.pages.basepage import BasePage
from YujinProject.test_appium.pages.workbench_page import WorkBenchPage


class MainPage(BasePage):

    # 定位 通讯录
    _addresslist_locator = (MobileBy.XPATH, "//*[@text='通讯录']")
    # 定位 工作台
    _workbench_locator = (MobileBy.XPATH, "//*[@text='工作台']")

    # 跳转到通讯录页面
    def goto_addresslist(self):
        # 显式等待，直到通讯录可见
        self.wait_until_visibility(self._addresslist_locator)
        # 查找并点击 通讯录
        self.find_and_click(self._addresslist_locator)
        # 跳转到 通讯录页面
        return AddressListPage(self.driver)

    # 跳转到工作台页面
    def goto_workbench(self):
        # 定位 工作台，并点击
        self.find_and_click(*self._workbench_locator)
        # 跳转到 工作台 页面
        return WorkBenchPage(self.driver)

