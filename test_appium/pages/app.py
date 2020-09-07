'''
app.py 存放app特有的操作，
比如：启动app、关闭app、重启app、进入首页
'''
from appium import webdriver

from YujinProject.test_appium.pages.basepage import BasePage
from YujinProject.test_appium.pages.mainpage import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            desire_cap = {}
            desire_cap["platformName"] = "android"
            desire_cap["deviceName"] = "emulator-5554"
            desire_cap["appPackage"] = "com.tencent.wework"
            desire_cap["appActivity"] = ".launch.WwMainActivity"
            desire_cap["resetKeyboard"] = "true"
            desire_cap["noReset"] = "true"
            desire_cap["settings[waitForIdleTimeout"] = 0
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
            self.driver.implicitly_wait(3)
        else:
            # launch_app():启用capability里设置的的appPackage和appActivity
            self.driver.launch_app()
            # start_activity()，可以启用任何app，需要传入appPackage和appActiviyt
            self.driver.start_activity()
        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def goto_mainpage(self) -> MainPage:
        return MainPage(self.driver)
