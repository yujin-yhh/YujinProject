from selenium.webdriver.common.by import By
from YujinProject.test_page_practice.pages.addmember_page import AddMemberPage
from YujinProject.test_page_practice.pages.basepage import Base
from YujinProject.test_page_practice.pages.contact_page import ContactPage


class MainPage(Base):
    # 私有变量，定义URL
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    # 私有变量，首页"添加成员"链接
    _addmember = (By.CSS_SELECTOR, "[node-type=addmember]")
    # 私有变量，通讯录链接
    _menu_contacts = (By.ID, "menu_contacts")

    # 跳转到通讯录页面
    def go_to_contact(self):
        # 定位通讯录，并点击
        self.find(*self._menu_contacts).click()
        # 对ContactPage进行实例化，表示业务逻辑的转换关系
        return ContactPage(self.driver)

    # 跳转到添加联系人页面
    def go_to_addmember(self):
        # 定位添加成员按钮，并点击
        self.find(*self._addmember).click()
        # 跳转到添加成员页面
        return AddMemberPage(self.driver)
