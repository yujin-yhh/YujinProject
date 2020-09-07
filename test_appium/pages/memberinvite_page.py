'''

添加成员页面
1。微信邀请同事
2。从微信/手机通讯录中添加
3。手动添加
'''
from appium.webdriver.common.mobileby import MobileBy

from YujinProject.test_appium.pages.basepage import BasePage
from YujinProject.test_appium.pages.contactadd_page import ContactAdd


class MemberInvite(BasePage):
    # 定位到 手动添加联系人
    _addcontact_locator =(MobileBy.XPATH,"//*[@text='手动输入添加']")

    # 点击手动输入添加，跳转到 添加成员 页面
    def goto_contactadd(self):
        # 点击手动输入添加
        self.find_and_click(self._addcontact_locator)
        # 跳转到添加成员页面
        return ContactAdd(self.driver)

    # 返回toast控件的文本
    def get_toast(self):
        # 返回toast文本
        return self.get_toast_text()