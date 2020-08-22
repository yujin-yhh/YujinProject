import shelve
from time import sleep
import pytest
from selenium import webdriver


class TestWeiXin():
    def setup(self):
        self.driver = webdriver.Chrome()
        # 添加隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    # 实现将浏览器复用到cookie添加到新实例化到浏览器页面中
    @pytest.mark.skip
    def test_weixin(self):
        # 实例化浏览器并打开URL
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        # 使用浏览器复用获取的cookie值
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851926895696'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'xw_main_login', 'path': '/', 'secure': False, 'value': 'qq'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'qq_client_id', 'path': '/', 'secure': False, 'value': '101487368'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851926895696'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '2908386304'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '8497648200'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325041161079'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'uw8k93GR_IIL9PC_b_e0NQKpAdjgvxxGdzbXK-aYX3BcifFWRByNDPMDJpqMjgpQ'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a2871090'}, {'domain': 'work.weixin.qq.com', 'expiry': 1597968833, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '1kgdfbi'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '10888041231052441'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600531442, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629109295, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1597572953'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '3_39281020F241DEB8490F5DE5E029F82F'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'fLp4kk7SqX_a05Qx1GvNzn4EYAJe5TGS1U5rM7Kvjk9mzCrNbfmEaXyY5BPkpHeMirHnkEaPTH3_WaT9P1CUKoUSKNoGYmDCyYBGHcMuh_lFToAWXRrBD_-oWYWVaZFRqjPVTHNb-nmyIAzDqnvSy3cm-HiOhOBkcC4yMAF2202lnsbnauXORZe6YKxCHNzdKOykTTTr_5z1Wfs7yNByrHrgbIU4GEn4UlpEfPK1QG7kR_4PhLhUhOHpDtpVZQMVgEU-OoSIdgLn2UvTJVMWDQ'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'qq_access_token', 'path': '/', 'secure': False, 'value': '5488B2DD46389230BD69360AD5B3621F'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'qq_openid', 'path': '/', 'secure': False, 'value': '39281020F241DEB8490F5DE5E029F82F'}, {'domain': '.qq.com', 'expiry': 1599877974, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '1158501442@qq.com'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '261b0894e3bf26cfca0b77f37345e332df673139912f1281c04d18f03d09feec'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629108946, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1908785182, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '93956d24bd4436eb'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'm/gRh5ODQ/'}]
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851926895696'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'xw_main_login', 'path': '/', 'secure': False, 'value': 'qq'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'qq_client_id', 'path': '/', 'secure': False, 'value': '101487368'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851926895696'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '2908386304'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '8497648200'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325041161079'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'uw8k93GR_IIL9PC_b_e0Ncf6Whr8NwgXabyy3y39MxrcQHYv_9em8pZ8_J5xj2IB'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a980284'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '21897405062340490'}, {'domain': 'work.weixin.qq.com', 'expiry': 1598026326, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '8hs49k6'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600587776, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629109295, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1597572953'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '3_39281020F241DEB8490F5DE5E029F82F'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'tbZ_bDz9njdDZ-9O5HZk-DtG5ogCZk2PHQBK2XcJK1eseTOtSvqVHanZsUHocAgSQzjDa_XUC7ABonBHbKgNZhX7ABeZ2E-Ww9G2aMGwnggu-TYCj1uMO9VMqCEaO9y7oVNrJuoe4lt8j1IKbcB3GOx7Yft5LqV5PB5MJO48ijJHEo4Ik1HpaQ11Fb7lVO2COWq-ZnpatwIsL_eyWXOspsIKi1l-ZoG4iRUBWBMvutoF4ri4soozDCX7cE26NY4GguoeOQJ47Sa0Di0i19taBg'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'qq_access_token', 'path': '/', 'secure': False, 'value': '5488B2DD46389230BD69360AD5B3621F'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'qq_openid', 'path': '/', 'secure': False, 'value': '39281020F241DEB8490F5DE5E029F82F'}, {'domain': '.qq.com', 'expiry': 1599877974, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '1158501442@qq.com'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '261b0894e3bf26cfca0b77f37345e332df673139912f1281c04d18f03d09feec'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629108946, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1908785182, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '93956d24bd4436eb'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'm/gRh5ODQ/'}]

        # 将cookie值加入到实例化到driver中
        for cookie in cookies:
            # 如果expiry值有浮点数报错时将expiry移除，不添加到cookie中
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        # 重新打开浏览器
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    # 使用浏览器复用读取到cookie完成登录，实现联系人导入到测试用例
    @pytest.mark.skip
    def test_importcontacts(self):
        # 打开微信首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        # 使用浏览器复用获取的cookie值
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851926895696'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'xw_main_login', 'path': '/', 'secure': False, 'value': 'qq'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'qq_client_id', 'path': '/', 'secure': False, 'value': '101487368'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851926895696'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '2908386304'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '8497648200'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325041161079'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'uw8k93GR_IIL9PC_b_e0NXppHzzNYLoEoUmQooyZyZb14NUjVwq33rNQwpw4-W7U'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a9201264'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '1088804123286733'}, {'domain': 'work.weixin.qq.com', 'expiry': 1598026326, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '8hs49k6'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600613281, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629109295, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1597572953'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '3_39281020F241DEB8490F5DE5E029F82F'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'kYKvCQbINWe_zOZeUukjNpG2AgAqzDv5E7nOmfPpPI1QKR3AtIyndAW9AdVl-HflWps0N_YX6-b_BIpUGmtYWPIHPel5COv3aLdjD1IvbfR-KCIPeC-9j1rEEefgEcTC787fO1cErbl-qzdKFAyZAQNduwfE8JWERPldYiU4ju5VfXt2IZtO9IRW2GL4MwgHk_CrEMV5f7Sle1gEue5ZaJHlCRFpAG0oHBeEiNNIWqJKPpD2wL74BMNG49frpEYC9DEaydZu2eULsAmc2gdxGw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'qq_access_token', 'path': '/', 'secure': False, 'value': '5488B2DD46389230BD69360AD5B3621F'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'qq_openid', 'path': '/', 'secure': False, 'value': '39281020F241DEB8490F5DE5E029F82F'}, {'domain': '.qq.com', 'expiry': 1599877974, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '1158501442@qq.com'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '261b0894e3bf26cfca0b77f37345e332df673139912f1281c04d18f03d09feec'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629108946, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1908785182, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '93956d24bd4436eb'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'm/gRh5ODQ/'}]
        # 将cookie值加入到实例化到driver中
        for cookie in cookies:
            # 如果expiry值有浮点数报错时将expiry移除，不添加到cookie中
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        # 重新打开浏览器，此时登录成功，跳转到首页页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        # 定位元素导入通讯录，并点击
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click()
        # 定位元素上传文件，并传入文件
        self.driver.find_element_by_id("js_upload_file_input").send_keys("/Users/huanhuan/Downloads/mycontacts.xlsx")
        sleep(3)
        # 获取导入文件结果页面的文件信息
        filename = self.driver.find_element_by_id("upload_file_name").text
        # 添加断言，如果导入结果页面的文件名和传入的文件名一一致，则导入成功
        assert filename == "mycontacts.xlsx"
        # 定位确认导入按钮并点击
        self.driver.find_element_by_id('submit_csv').click()
        # 定位到导入结果页面的提示信息
        alert = self.driver.find_element_by_class_name("import_succStage_resultShow").text
        # 添加断言，如果提示信息为新增导入1人则导入成功
        assert alert == "新增导入1人"

    # 定义方法，将cookie存入的文件中
    @pytest.mark.skip
    def test_shelve(self):
        # 通过页面复用已获取页面的cookie
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851926895696'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'xw_main_login', 'path': '/', 'secure': False, 'value': 'qq'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'qq_client_id', 'path': '/', 'secure': False, 'value': '101487368'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851926895696'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '2908386304'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '8497648200'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325041161079'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'uw8k93GR_IIL9PC_b_e0NXppHzzNYLoEoUmQooyZyZb14NUjVwq33rNQwpw4-W7U'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a9201264'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '1088804123286733'}, {'domain': 'work.weixin.qq.com', 'expiry': 1598026326, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '8hs49k6'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600613281, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629109295, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1597572953'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '3_39281020F241DEB8490F5DE5E029F82F'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'kYKvCQbINWe_zOZeUukjNpG2AgAqzDv5E7nOmfPpPI1QKR3AtIyndAW9AdVl-HflWps0N_YX6-b_BIpUGmtYWPIHPel5COv3aLdjD1IvbfR-KCIPeC-9j1rEEefgEcTC787fO1cErbl-qzdKFAyZAQNduwfE8JWERPldYiU4ju5VfXt2IZtO9IRW2GL4MwgHk_CrEMV5f7Sle1gEue5ZaJHlCRFpAG0oHBeEiNNIWqJKPpD2wL74BMNG49frpEYC9DEaydZu2eULsAmc2gdxGw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'qq_access_token', 'path': '/', 'secure': False, 'value': '5488B2DD46389230BD69360AD5B3621F'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1605061975, 'httpOnly': False, 'name': 'qq_openid', 'path': '/', 'secure': False, 'value': '39281020F241DEB8490F5DE5E029F82F'}, {'domain': '.qq.com', 'expiry': 1599877974, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '1158501442@qq.com'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '261b0894e3bf26cfca0b77f37345e332df673139912f1281c04d18f03d09feec'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629108946, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1908785182, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '93956d24bd4436eb'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'm/gRh5ODQ/'}]
        # 将cookies的内容存到db文件中
        db = shelve.open('./datas/cookie')
        db['cookie'] = cookies
        db.close()

    # 将存入到cookie中的数据读取出来存放到cookie中
    @pytest.mark.skip
    def test_redecookie(self):
        db = shelve.open('./datas/cookie.db')
        cookies = db['cookie']
        db.close()

    # 从文件中读取cookie完成联系人导入到测试用例
    def test_importcontactsfromdb(self):
        # 打开微信首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        # 从cookie.db文件中读取cookies
        db = shelve.open('./datas/cookie')
        cookies = db['cookie']
        db.close()
        # 将cookie值加入到实例化到driver中
        for cookie in cookies:
            # 如果expiry值有浮点数报错时将expiry移除，不添加到cookie中
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        # 重新打开浏览器，此时登录成功，跳转到首页页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        # 定位元素导入通讯录，并点击
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click()
        # 定位元素上传文件，并传入文件
        self.driver.find_element_by_id("js_upload_file_input").send_keys("/Users/huanhuan/Downloads/mycontacts.xlsx")
        sleep(3)
        # 获取导入文件结果页面的文件信息
        filename = self.driver.find_element_by_id("upload_file_name").text
        # 添加断言，如果导入结果页面的文件名和传入的文件名一一致，则导入成功
        assert filename == "mycontacts.xlsx"
        # 定位确认导入按钮并点击
        self.driver.find_element_by_id('submit_csv').click()
        # 定位到导入结果页面的提示信息
        alert = self.driver.find_element_by_class_name("import_succStage_resultShow").text
        # 添加断言，如果提示信息为新增导入1人则导入成功
        assert alert == "新增导入1人"


