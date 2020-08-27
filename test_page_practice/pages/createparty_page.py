import time
from selenium.webdriver.common.by import By
from YujinProject.test_page_practice.pages.basepage import Base
from YujinProject.test_page_practice.pages.contact_page import ContactPage


class CreateParty(Base):
    # 添加部门页面部门名称输入框
    _name = (By.CSS_SELECTOR, "[name='name']")
    # 定位所属部门下拉框
    _parent_partyname = (By.CSS_SELECTOR, ".js_toggle_party_list")
    # 定位点击所属部门下拉框后的所属部门列表
    _partylist = (By.CSS_SELECTOR, ".js_party_list_container a")
    # 确定按钮
    _submit = (By.CSS_SELECTOR, '[d_ck="submit"]')
    # 取消按钮
    _cancel = (By.CSS_SELECTOR, '[d_ck="cancel"]')

    # 新增部门信息
    def addparty(self, name):
        time.sleep(3)
        # 定位部门名称并输入内容
        self.find(*self._name).send_keys(name)
        # 定位"选择所属部门"并点击
        self.find(*self._parent_partyname).click()
        time.sleep(2)
        # 定位所属部门列表第一个，并点击
        self.finds(*self._partylist)[0].click()
        return self

    # 点击确认按钮
    def confirm(self):
        time.sleep(3)
        # 定位确定按钮，并点击
        self.find(*self._submit).click()
        return ContactPage(self.driver)

    # 点击取消按钮
    def cancle(self):
        # 定位到取消按钮并点击
        self.find(*self._cancel).click()
        return ContactPage(self.driver)
