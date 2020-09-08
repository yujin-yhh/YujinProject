from time import sleep

import pytest
import yaml

from YujinProject.test_appium.pages.app import App


def get_data():
    with open("../datas/contact.yml") as f:
        contact_data = yaml.safe_load(f)
        add_contact_data = contact_data["add"]
        del_cantact_data = contact_data["del"]
    return [add_contact_data, del_cantact_data]


class TestContact:
    def setup(self):
        '''
        应用的启动
        '''
        self.app = App()
        self.main = self.app.start().goto_mainpage()

    def teardown(self):
        '''
        应用的关闭
        '''
        self.app.stop()

    @pytest.mark.parametrize("name,gender,phonenum", get_data()[0])
    def test_addcontact(self, name, gender, phonenum):
        '''
        1。首页，点击通讯录
        2。点击手动添加，跳转到手动添加成员页面
        3。编辑姓名、编辑性别、编辑手机号，点击保存按钮
        '''
        mypage = self.main.goto_addresslist().goto_memberinvite().goto_contactadd() \
            .edit_name(name).edit_gender(gender).edit_phonenum(phonenum).save_click()
        # 获取toast文本，添加断言
        mytoast = mypage.get_toast()
        assert "添加成功" == mytoast

    @pytest.mark.parametrize("name",get_data()[1])
    def test_delcontact(self, name):
        '''
        1。首页，点击通讯录。
        2。点击搜索按钮，并输入name
        '''
        before_del = self.main.goto_addresslist().goto_searchmember().send_search_member(name)
        # 获取删除前的查询联系人个数
        before_del_num = before_del.get_member_num_befordel(name)
        '''
        3。点击第一条查询结果，进入联系人详细信息简介
        4。在联系人详细信息简介页面，点击又上角3个点号，进入编辑成员页面
        5。下拉点击删除成员连接，弹出的确认框中点击确定按钮
        '''
        after_del = before_del.click_search_result(
            name).goto_contactdetailsttings().goto_contactedit().del_contact().del_confirm()
        sleep(2)
        # 获取删除后的查询联系人个数
        after_del_num = after_del.get_member_num_afterdel(name)
        assert before_del_num - after_del_num == 1
