from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWeixin():
    def setup(self):
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        # 设置隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        # get cookies()获取当前页面的cookie
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # 打开企业微信首页，需要登录
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # 带有登录信息的cookie
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'JBO1qZSWH_NhjddEdy_9rjkhFgWu8ul0g2IDbS_dd8SxMxEvWTixDrTEg5Kt-xMGSktpq59GvOOAFIe6gcoSFTCoHCagbbPebBD94a4RXfTSA4kbyF2AthJKYQyEc1AjEfCLFsczBMP90ZM2b3IKibhxn8riyipoJ-ojfSrPs3BSVrzSWzuLH5Dbx6rzlmPpDSBYsriEfvTfPLclSO-7Mgau6dKO5ivxSkiET2rCjIE7nAzWDNoraJ5MHZuFPzUV9uuOiB1u7kfuO55dnF08rA'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'NacXrRwkCLHNPwHC8VaEOyUqbs3ACW_5n7Ygx9A6R66oSE49NAea1ljrg01a945B'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a4772354'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688852933222337'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688852933222337'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325086154374'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1598087013'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '364762995213269'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1598110163, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '6irl2ms'},
            {'domain': '.qq.com', 'expiry': 1598190085, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1548692783.1598078636'},
            {'domain': '.qq.com', 'expiry': 1661175685, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.644568860.1597235634'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1628771621, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1598536398, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
             'secure': False, 'value': '751665720'},
            {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '6f4f1da0bf899fb172c410bb32700713cddaf39d909cbfb32a20b5500ccd2496'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629623013, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1597235624,1597406992,1598078635,1598087013'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '4735762747'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147483643, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'jXS5JN4ybs'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '3520174080'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600695688, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'en-us%2Cen%2Czh-hk%2Ccht'}]
        for cookie in cookies:
            #避免expiry的值里出现浮点数的情况，将expiry值从cookie中移除，不影响成功登录
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        #重新打开已有cookie信息的企业微信页面
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # sleep(3)
        #定位元素import company contacts并点击
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        # sleep(2)
        #定位元素upload file并上传文件
        self.driver.find_element_by_id('js_upload_file_input').send_keys('C:/Users/Paula/Desktop/test excel.xlsx')
        # sleep(2)
        #判断文件是否上传成功
        assert 'test excel.xlsx' == self.driver.find_element_by_id('upload_file_name').text
        # sleep(2)


