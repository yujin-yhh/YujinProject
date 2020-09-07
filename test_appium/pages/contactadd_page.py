'''
添加成员编辑页面
'''
from appium.webdriver.common.mobileby import MobileBy

from YujinProject.test_appium.pages.basepage import BasePage


class ContactAdd(BasePage):
    # 定位 姓名输入框
    _name_locator = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']")
    # 定位性别 下拉框
    _gender_locator = (MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@class= 'android.widget.LinearLayout']")
    # 性别下拉框 定位女
    _femal_locaotr = (MobileBy.XPATH, "//*[@text='女']")
    # 性别下拉框，定位男
    _male_locaotr = (MobileBy.XPATH, "//*[@text='男']")
    # 定位到 手机号 输入框
    _phonenum_locator = (MobileBy.XPATH, "//*[contains(@text,'手机号')]")
    # 定位 保存按钮
    _save_locaotr = (MobileBy.XPATH, "//*[contains(@text,'保存')]")

    # 编辑姓名
    def edit_name(self, name):
        # 定位姓名输入框，并输入姓名
        self.find_and_sendkeys(self._name_locator, name)
        # 返回到当前页面
        return self

    # 编辑性别
    def edit_gender(self, gender):
        # 定位性别，并点击
        self.find_and_click(self._gender_locator)
        # 定位到性别，选择性别，并点击
        # 下拉框 选择女
        if gender == "女":
            self.find_and_click(self._femal_locaotr)
        # 下拉框 选择男
        else:
            self.find_and_click(self._male_locaotr)
        # 返回当前页面
        return self

    # 编辑手机号
    def edit_phonenum(self, phonenum):
        # 定位到手机号输入框，并输入手机号
        self.find_and_sendkeys(self._phonenum_locator, phonenum)
        # 返回当前页面
        return self

    # 点击保存按钮
    def save_click(self):
        from YujinProject.test_appium.pages.memberinvite_page import MemberInvite
        # 定位并点击保存按钮
        self.find_and_click(self._save_locaotr)
        # 返回添加成员页面
        return MemberInvite(self.driver)
