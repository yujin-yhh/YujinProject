import time
from selenium.webdriver.common.by import By
from YujinProject.test_page_practice.pages.basepage import Base


class ContactPage(Base):
    # 私有变量，定义首页
    _menu_index = (By.ID, "menu_index")
    # 私有变量，定义通讯录页面姓名
    _get_namelist = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    # 私有变量，定义通讯录页面"添加成员"按钮
    _js_add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    # 私有变量，搜索部门旁边的"+"
    _member_colLeft_top_addBtn = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    # 私有变量，点击+后的"添加部门"链接
    _js_create_party = (By.CSS_SELECTOR, ".js_create_party")
    # 定位部门列表
    _party_list = (By.CSS_SELECTOR, ".jstree-open a")

    # 跳转到添加成员页面
    def go_to_addmember(self):
        # 解决循环导入的问题
        from YujinProject.test_page_practice.pages.addmember_page import AddMemberPage
        time.sleep(2)
        # 点击通讯录页面添加成员按钮
        self.find(*self._js_add_member)
        # 跳转到添加成员页面
        return AddMemberPage(self.driver)

    def get_member_list(self):
        time.sleep(5)
        # 解元祖方式，查找通讯录页面成员列表的姓名集合
        ele = self.finds(*self._get_namelist)
        # 获取姓名集合中的姓名内容添加到列表list1中
        list1 = []
        for name in ele:
            list1.append(name.text)
        print(list1)
        # 返回通讯录页面成员列表的姓名
        return list1

    # 回到首页
    def go_to_indexpage(self):
        from YujinProject.test_page_practice.pages.main_page import MainPage
        # 定位首页，并点击，回到首页
        self.find(*self._menu_index).click()
        # 返回首页
        return MainPage(self.driver)

    # 跳转到新增部门页面
    def go_to_createparty_page(self):
        from YujinProject.test_page_practice.pages.createparty_page import CreateParty
        time.sleep(2)
        # 定位+并点击
        self.find(*self._member_colLeft_top_addBtn).click()
        # 定位添加部门并点击
        self.find(*self._js_create_party).click()
        # 跳转到新增部门页面
        return CreateParty(self.driver)

    # 获取部门列表值
    def get_partylist(self):
        partylist =[]
        ele = self.finds(*self._party_list)
        for partyname in ele:
            partylist.append(partyname.text)
        print(partylist)
        return partylist
