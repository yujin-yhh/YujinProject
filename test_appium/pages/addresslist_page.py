'''
通讯录页面
1。点击添加成员，跳转到goto_memberinvite页面（MemberInvite）
'''
from appium.webdriver.common.mobileby import MobileBy

from YujinProject.test_appium.pages.basepage import BasePage
from YujinProject.test_appium.pages.memberinvite_page import MemberInvite
from YujinProject.test_appium.pages.searchmember_page import SearchMemberPage


class AddressListPage(BasePage):
    # 定位 搜索框
    _search_elcator = (MobileBy.ID, "com.tencent.wework:id/hvn")

    # 跳转到添加成员页面
    def goto_memberinvite(self):
        # 下拉寻找，添加成员 并点击
        self.find_by_scroll_and_click("添加成员")
        # 跳转到 添加成员页面
        return MemberInvite(self.driver)

    # 跳转到搜索联系人 页面
    def goto_searchmember(self):
        # 定位到搜索按钮，并点击：
        self.find_and_click(self._search_elcator)
        # 跳转到搜索联系人页面
        return SearchMemberPage(self.driver)