from appium.webdriver.common.mobileby import MobileBy

from YujinProject.test_appium.pages.basepage import BasePage
from YujinProject.test_appium.pages.contact_edit_page import ContactEdit

'''
联系人详情设置页面
'''
class ContactDetailSetting(BasePage):
    # 定位 编辑成员
    _editcontact_locator = (MobileBy.XPATH, "//*[@text='编辑成员']")

    def goto_contactedit(self):
        # 点击编辑成员
        self.find_and_click(self._editcontact_locator)
        # 跳转到编辑成员页面
        return ContactEdit(self.driver)
