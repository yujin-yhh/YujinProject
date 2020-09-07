'''
跳转到编辑成员页面
'''
from appium.webdriver.common.mobileby import MobileBy

from YujinProject.test_appium.pages.basepage import BasePage


class ContactEdit(BasePage):
    # 定位 确定按钮
    _confirm_locator = (MobileBy.XPATH,"//*[@text='确定']")

    # 删除联系人
    def del_contact(self):
        # 滚动查找 删除成员，并点击
        self.find_by_scroll_and_click("删除成员")
        # 返回当前页面
        return self

    # 删除联系人确认
    def del_confirm(self):
        # 点击确定按钮
        self.find_and_click(self._confirm_locator)
        from YujinProject.test_appium.pages.searchmember_page import SearchMemberPage
        # 返回到查询联系人页面
        return SearchMemberPage(self.driver)




