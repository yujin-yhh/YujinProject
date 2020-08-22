from time import sleep

from seleniumpractice.test_seleniumprac_one.base import Base


class TestGetCookies(Base):
    def test_getcookie(self):
        self.driver.maximize_window()
        sleep(3)
        # 获取当前页面的cookie
        cookies = self.driver.get_cookies()
        print(cookies)