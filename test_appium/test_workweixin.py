import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWorkWeiXin:

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
        self.driver.quit()

    # 外出打卡
    @pytest.mark.skip
    def test_clock_in(self):
        # 定位到工作台并点击
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 滚动查找，定位打卡
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("打卡").instance(0));').click()
        # 定位到 外出打卡 并点击
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hgs").click()
        # 定位到 打卡框，并点击
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/at4").click()
        # 定位到打卡结果元素
        result = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/oh")
        # 添加断言，打卡结果是"外出打卡成功"
        assert "外出打卡成功" == result.text

    # 发送消息
    def test_send_message(self):
        # 定位到搜索框，并点击
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hvn").click()
        # 定位到搜索框并输入联系人。
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/gfs").send_keys("。")
        # 定位到联系人并点击
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/e12']").click()
        # 定位到文本输入框，并输入内容
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/ei_").send_keys("this is a test message")
        # 定位到发送，并点击
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/ei6").click()
        # 定位到已发送消息列表元素的最后一个消息
        message = self.driver.find_elements(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/ehv']")[-1].text

        assert "this is a test message" == message
