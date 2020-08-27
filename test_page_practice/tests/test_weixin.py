import time

from YujinProject.test_page_practice.pages.basepage import Base
from YujinProject.test_page_practice.pages.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    # 1。首页点击通讯录，点击添加成员跳转到添加成员页面，输入页面元素点击保存
    # 2。获取成员列表，添加断言
    def test_add_member_succes(self):
        namelist = self.main.go_to_addmember().add_member('小红', '222222', '13809091234').save_member().get_member_list()
        assert "小红" in namelist

    # 1。首页点击添加成员，2。添加成员页面点击添加成员，输入页面元素，点击取消按钮
    # 3。获取成员列表，添加断言
    def test_add_member_fail(self):
        namelist = self.main.go_to_addmember().add_member('小吕', '222223',
                                                          '13809091235').cancel_member().get_member_list()
        assert "小吕" not in namelist

    # 添加部门测试用例
    # 1。通讯页点击+，点击添加部门页面；2。输入部门名称及所属部门，点击确定按钮
    def test_addparty_succ(self):
        # 执行到点击确认按钮
        a = self.main.go_to_contact().go_to_createparty_page().addparty("测试三部").confirm()
        time.sleep(5)
        # 获取当前页面到部门信息
        partylist = a.get_partylist()
        # 断言，判断新增到部门在部门列表中
        assert "测试三部" in partylist

    # 添加部门测试用例
    # 1。通讯页点击+，点击添加部门页面；2。输入部门名称及所属部门，点击取消按钮
    def test_addparty_fail(self):
        partylist = self.main.go_to_contact().go_to_createparty_page().addparty("测试二部").cancle().get_partylist()
        assert "测试二部" not in partylist

    # 方法级别的setup,每执行用例前都回到首页
    def setup_method(self):
        self.main.go_to_indexpage()
        time.sleep(2)

    # 类级别的teardown，关闭浏览器
    def teardown_class(self):
        self.main.driver.quit()

