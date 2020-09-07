'''
basepage 基类
最基本到操作：初始化driver，find，显式等待等。。。。

'''
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 封装find_element方法
    def find(self, locator):
        return self.driver.find_element(*locator)

    # 封装find_elements方法
    def finds(self, locator):
        return self.driver.find_elements(*locator)

    # 封装查找元素并点击
    def find_and_click(self, locator):
        return self.find(locator).click()

    # 封装滚动查找
    def find_by_scroll(self, text):
        ele = (MobileBy.ANDROID_UIAUTOMATOR,
               f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));')
        self.find(ele)

    # 封装滚动查找并点击
    def find_by_scroll_and_click(self, text):
        ele = (MobileBy.ANDROID_UIAUTOMATOR,
               f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));')
        self.find_and_click(ele)

    # 封装获取toast控件文本信息
    def get_toast_text(self):
        toast_locator = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        return self.find(toast_locator).text

    # 封装 find_element().send_keys()
    def find_and_sendkeys(self, locator, text):
        self.find(locator).send_keys(text)

    # 封装显式等待，直到元素可见
    def wait_until_visibility(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    # 封装显式等待，直到元素不可见
    def wait_until_ivisibility(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))
