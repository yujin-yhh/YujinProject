import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from YujinProject.test_page_practice.pages.basepage import Base
from YujinProject.test_page_practice.pages.contact_page import ContactPage


class AddMemberPage(Base):
    # 私有变量，用于定位姓名输入框
    _username = (By.ID, "username")
    # 私有变量，用于定位账号输入框
    _memberAdd_acctid = (By.ID, "memberAdd_acctid")
    # 私有变量，用户定位手机号输入框
    _memberAdd_phone = (By.ID, "memberAdd_phone")
    # 私有变量，用于定位保存按钮
    _js_btn_save = (By.CSS_SELECTOR, '.js_btn_save')
    # 私有变量，用于定位取消按钮
    _js_btn_cancel = (By.CSS_SELECTOR, '.js_btn_cancel')
    # 私有变量，用于定位"成员的资料尚未保存，确定要离开吗？"提示框中到"离开此页"按钮
    _cancel = (By.CSS_SELECTOR, '[node-type=cancel]')

    # 添加成员
    def add_member(self, name, acctid, phone):
        self.wait_for_locatal(self._username)
        # 定位姓名输入框并输入内容
        self.find(*self._username).send_keys(name)
        # 定位账号输入框并输入内容
        self.find(*self._memberAdd_acctid).send_keys(acctid)
        # 定位手机号并输入内容
        self.find(*self._memberAdd_phone).send_keys(phone)
        # return self是为了实现返回当前页面实例化时可以实现链式调用
        return self

    def save_member(self):
        time.sleep(2)
        # 定位保存按钮，并点击
        self.find(*self._js_btn_save).click()
        # 返回通讯录页面
        return ContactPage(self.driver)

    def cancel_member(self):
        # 定位添加成员页面到取消按钮，并点击
        self.find(*self._js_btn_cancel).click()
        # 定位到"成员的资料尚未保存，确定要离开吗？"提示框页面到"离开此页"按钮，并点击
        self.find(*self._cancel).click()
        # 返回到通讯录页面
        return ContactPage(self.driver)
