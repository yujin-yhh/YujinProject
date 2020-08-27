from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    _base_url = ""

    def __init__(self, driver_base=None):
        # 避免driver被重复初始化
        if driver_base is None:
            opt = Options()
            opt.set_capability("pageLoadStrategy", "eager")
            self.driver = webdriver.Chrome(options=opt)
            self.driver.maximize_window()
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            cookies = [
                {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
                 'value': '1688851926895696'},
                {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'xw_main_login', 'path': '/',
                 'secure': False, 'value': 'qq'},
                {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'qq_client_id', 'path': '/',
                 'secure': False, 'value': '101487368'},
                {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
                 'value': '1688851926895696'},
                {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
                 'secure': False, 'value': '2908386304'},
                {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
                 'secure': False, 'value': '8497648200'},
                {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/',
                 'secure': False, 'value': '1970325041161079'},
                {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
                 'value': 'uw8k93GR_IIL9PC_b_e0NalSdtDaEkMMNUch1lEPtjYtaNhVgrXNoAOv5t2JnU5A'},
                {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
                 'value': 'a8826100'},
                {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
                 'value': '21897405062032992'},
                {'domain': 'work.weixin.qq.com', 'expiry': 1598519933, 'httpOnly': True, 'name': 'ww_rtkey',
                 'path': '/', 'secure': False, 'value': '1k7dl76'},
                {'domain': '.qq.com', 'expiry': 1661093388, 'httpOnly': False, 'name': '_ga', 'path': '/',
                 'secure': False, 'value': 'GA1.2.50127725.1598021388'},
                {'domain': '.work.weixin.qq.com', 'expiry': 1601080446, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
                 'path': '/', 'secure': False, 'value': 'zh-cn'},
                {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
                 'value': '3lwsmy6UKwW-MgCayK3db56a108TOi_Dc-OwhmpA1Ymj09-HExDrgQumF3hASuENCubeN79qqfTtrt5nEEDbuQh_lZgclLTPmeW2ex9BfmocvQWt-xUVLiTdG6FOSkK5pPGnlH-WUQtNv5kvc-0U71_sak18TjQMMFSzlSl-ZeQ7LjI4vicKxYL1uPqy0ZmA1I-Res2DfWfFmPFQD8uMRUrqm24NF0g96YfOSQM0nnhjn3deEt4pRqiSesUCkr_C60AfELw9SH0k5mYVAyRjZw'},
                {'domain': '.work.weixin.qq.com', 'expiry': 1629109295, 'httpOnly': False,
                 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                 'value': '1597572953'},
                {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
                 'secure': False, 'value': '3_39281020F241DEB8490F5DE5E029F82F'},
                {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
                 'value': 'direct'},
                {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'qq_access_token', 'path': '/',
                 'secure': False, 'value': '5488B2DD46389230BD69360AD5B3621F'},
                {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
                 'value': '1'},
                {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'qq_openid', 'path': '/',
                 'secure': False, 'value': '39281020F241DEB8490F5DE5E029F82F'},
                {'domain': '.qq.com', 'expiry': 1599877974, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
                 'secure': False, 'value': '1158501442@qq.com'},
                {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/',
                 'secure': False, 'value': '261b0894e3bf26cfca0b77f37345e332df673139912f1281c04d18f03d09feec'},
                {'domain': '.work.weixin.qq.com', 'expiry': 1629108946, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
                 'path': '/', 'secure': False, 'value': '0'},
                {'domain': '.qq.com', 'expiry': 1908785182, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
                 'secure': False, 'value': '93956d24bd4436eb'},
                {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/',
                 'secure': False, 'value': 'm/gRh5ODQ/'}]

            for cookie in cookies:
                self.driver.add_cookie(cookie)
        else:
            self.driver: WebDriver = driver_base
        if self._base_url != "":
            self.driver.get(self._base_url)

        self.driver.implicitly_wait(5)

    # 定义方法，点击回到首页回到主页面
    def go_to_indexpage(self):
        self.driver.find_element_by_id("menu_index").click()

    # 封装find_element方法
    def find(self, by, value):
        return self.driver.find_element(by, value)

    # 封装find_elements方法
    def finds(self, by, value):
        return self.driver.find_elements(by, value)

    def wait_for_clickable(self, element):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(element))

    def wait_for_locatal(self, element):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(element))

    def company_in_partylist(self):
        pass
