'''
联系人详细信息简介
'''
from appium.webdriver.common.mobileby import MobileBy

from YujinProject.test_appium.pages.basepage import BasePage
from YujinProject.test_appium.pages.contact_detail_settings_page import ContactDetailSetting


class ContactDetailBriefInfoProfile(BasePage):
    # 定位 页面右上角的三个点号
    _eidtkey_locator = (MobileBy.ID, "com.tencent.wework:id/hvd")

    # 跳转到联系人详情设置页面
    def goto_contactdetailsttings(self):
        # 点击页面右上角到三个点，跳转到联系人详情设置页面
        self.wait_until_visibility(self._eidtkey_locator)
        self.find_and_click(self._eidtkey_locator)
        # 跳转到联系人详情设置页面
        return ContactDetailSetting(self.driver)
