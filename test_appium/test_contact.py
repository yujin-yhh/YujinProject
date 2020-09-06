from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestContact:
    def setup(self):
        desire_cap = {}
        desire_cap["platformName"] = "android"
        desire_cap["deviceName"] = "emulator-5554"
        desire_cap["appPackage"] = "com.tencent.wework"
        desire_cap["appActivity"] = ".launch.WwMainActivity"
        desire_cap["resetKeyboard"] = "true"
        desire_cap["noReset"] = "true"
        desire_cap["settings[waitForIdleTimeout"] = 0
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    # 添加联系人
    def test_add_contact(self):
        name = "hogwarts01"
        gender = '女'
        phonenum = '13212341222'
        # 定位到通讯录 并点击
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        # 下拉查找 添加成员 并点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        # 定位到手动输入添加，并点击
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        # 定位到 姓名 文本输入框，并输入内容
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        # 定位到性别下拉框，并点击
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'性别')]/..//*[@class= 'android.widget.LinearLayout']").click()
        # 定位到性别，选择性别，并点击
        if gender == "女":
            self.driver.find_element(MobileBy.XPATH,"//*[@text='女']").click()
        else:
            self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        # 定位到手机号，并输入内容
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'手机号')]").send_keys(phonenum)
        # 定位到保存按钮，并点击
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'保存')]").click()

        # 定位到toast,并获取text属性
        result_toast = self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text
        # 添加断言
        assert "添加成功" == result_toast

    # 删除联系人
    def test_del_contact(self):
        name = 'hogwarts01'
        # 定位到通讯录 并点击
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        # 定位到搜索按钮，并点击
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hvn").click()
        # 定位到搜索框，并输入内容
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/gfs").send_keys(name)
        # 定位到搜索结果，并点击
        print(f"//*[@text='{name}' and @class='android.widget.TextView']")
        self.driver.find_element(MobileBy.XPATH,f"//*[@text='{name}' and @class='android.widget.TextView']").click()
        # 定位到更多，并点击
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hvd").click()
        # 定位到编辑成员，并点击
        self.driver.find_element(MobileBy.XPATH,"//*[@text='编辑成员']").click()
        # 定位到删除成员，并点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("删除成员").instance(0));').click()

        # 定位到确定，并点击
        self.driver.find_element(MobileBy.XPATH,"//*[@text='确定']").click()
        # 添加显示等待，直到查询联系人的结果列表不可见
        locator = (MobileBy.XPATH,f"//*[@text='{name}' and @class='android.widget.TextView']")
        WebDriverWait(self.driver,10).until(expected_conditions.invisibility_of_element_located(locator))
        # 断言 查询联系人的结果列表长度为0即为删除成功
        lenth_list = len(self.driver.find_elements(MobileBy.XPATH,f"//*[@text='{name}' and @class='android.widget.TextView']"))
        assert lenth_list == 0