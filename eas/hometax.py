import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains
import os
import sys
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# print("홈텍스 매입조회:0 / 로그인만:1")
# select_work = input ("선택입력 :  ")
# select_work = 'y'
# while select_work != 'Ctrl+c':
    # print("홈텍스 매입조회:0 / 로그인만:1 / 상사:2")
    # select_work = input("선택입력 :  ")
    #
    # if select_work == "0":
    #     print("날짜입력 ex)20210302 ")
    #     start_date = input("조회 시작일 : ")
    #     last_date = input("조회 종료일 : ")
    #     name = input("거래처명 : ")
# 1.크롬접속
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # driver = webdriver(options=options)
driver = webdriver.Chrome("/home/ubuntu/projects/mysite/eas/chromedriver.exe", options=options)
driver.implicitly_wait(20)
driver.implicitly_wait(10)


driver.get('https://www.hometax.go.kr/')
driver.maximize_window()

        #  2) 로그인화면으로 이동
driver.implicitly_wait(10)
time.sleep(3)
driver.find_element_by_id('textbox81212912').click()
time.sleep(2)

        #  3) iframe 전환 : 로그인화면은 화면전체가 iframe
driver.implicitly_wait(10)
iframe = driver.find_element_by_css_selector('#txppIframe')
driver.switch_to.frame(iframe)
driver.implicitly_wait(10)
time.sleep(0.5)

        # 공동인증서 추가된 페이지 버튼 클릭
driver.implicitly_wait(10)
driver.find_element_by_css_selector('#anchor22').click()
driver.implicitly_wait(10)

  # 3) iframe 전환 : 로그인화면은 화면전체가 iframe
driver.implicitly_wait(10)
iframe = driver.find_element_by_css_selector('#dscert')
driver.switch_to.frame(iframe)
driver.implicitly_wait(10)
time.sleep(0.5)

  # 6) 공인인증서 선택
driver.implicitly_wait(10)
driver.find_element_by_css_selector('#row1dataTable').click()
driver.implicitly_wait(3)

#  7) 패스워드 입력0
driver.implicitly_wait(3)
passwd = 'djkbg-4107'
driver.find_element_by_id('input_cert_pw').send_keys(passwd)
driver.implicitly_wait(3)

#  8) 확인버튼 클릭
driver.find_element_by_id('btn_confirm_iframe').click()
time.sleep(2)

#  1) 조회발급 페이지로 이동
driver.get(
    'https://www.hometax.go.kr/websquare/websquare.wq?w2xPath=/ui/pp/index_pp.xml&tmIdx=1&tm2lIdx=&tm3lIdx=')
time.sleep(1)

#  2) iframe전환
iframe = driver.find_element_by_css_selector('#txppIframe')
driver.switch_to.frame(iframe)
time.sleep(0.5)

#  3) 목록조회 메뉴선택
driver.find_element_by_xpath('//*[@id="sub_a_0104020000"]').click()
time.sleep(0.5)

#  4) 발급 목록조회 선택
driver.find_element_by_xpath('//*[@id="sub_a_0104020100"]').click()
time.sleep(1)

#  5) 구분 매입/ 매출에서 매입 선택
driver.find_element_by_xpath('//*[@id="radio7_input_1"]').click()
driver.implicitly_wait(3)
time.sleep(0.5)

        # #  5) 조회시작일 입력
        # actions = ActionChains(driver)
        # time.sleep(1)
        # elem = driver.find_element_by_xpath('//*[@id="inqrDtStrt_input"]')
        # # driver.implicitly_wait(5)
        # time.sleep(1)
        # actions.double_click(elem).perform()  # 클리어처리로 비우고 쓰는 방법 전환 할것
        # time.sleep(1)
        # # driver.implicitly_wait(3)
        # elem.send_keys(start_date)
        # elem.send_keys(Keys.TAB)
        # time.sleep(1)
        # # elem.send_keys(Keys.TAB)
        # # time.sleep(0.5)
        # driver.implicitly_wait(3)
        #
        # #  5) 조회종료일 입력
        # time.sleep(0.5)
        # elem2 = driver.find_element_by_xpath('//*[@id="inqrDtEnd_input"]')
        # time.sleep(0.5)
        # actions.double_click(elem2).perform()
        # time.sleep(0.5)
        # driver.implicitly_wait(10)
        # elem2.send_keys(last_date)
        # driver.implicitly_wait(30)
        # elem2.send_keys(Keys.TAB)
        # # time.sleep(0.5)
        # elem2.send_keys(Keys.TAB)
        # # time.sleep(0.5)
        #
        # #  5) 거래처명 입력
        # time.sleep(0.5)
        # elem3 = driver.find_element_by_xpath('//*[@id="tnmNmInput"]')
        # # actions.double_click(elem2).perform()
        # driver.implicitly_wait(5)
        # elem3.send_keys(name)
        # driver.implicitly_wait(5)
        #
        # if name == "":
        #     select = Select(driver.find_element_by_id('selectbox90'))
        #     select.select_by_visible_text('50')
        #     time.sleep(2)
        #
        # #  5) 조회버튼 클릭
        # driver.find_element_by_xpath('//*[@id="trigger50"]').click()

        # 팝업창 닫기
main = driver.window_handles
for handle in main:
    if handle != main[0]:
        driver.switch_to_window(handle)
        driver.close()

        # slist = driver.find_element_by_id("resultGrid_body_tbody")
        # print(slist)
        # continue


    # elif select_work == "1":
    #     # 1.크롬접속
    #     driver = webdriver.Chrome("c:\chromedriver.exe")
    #     driver.implicitly_wait(20)
    #
    #     # 2. 홈택스 접속
    #
    #     #  1) 홈택스로 이동
    #     driver.get('https://www.hometax.go.kr/')
    #     driver.implicitly_wait(10)
    #     driver.maximize_window()
    #
    #     #  2) 로그인화면으로 이동
    #     driver.implicitly_wait(10)
    #     time.sleep(1)
    #     driver.find_element_by_id('textbox81212912').click()
    #     time.sleep(2)
    #     driver.implicitly_wait(10)
    #
    #     #  3) iframe 전환 : 로그인화면은 화면전체가 iframe
    #     iframe = driver.find_element_by_css_selector('#txppIframe')
    #     driver.switch_to.frame(iframe)
    #     driver.implicitly_wait(10)
    #     time.sleep(0.5)
    #
    #     # 공동인증서 추가된 페이지 버튼 클릭
    #     driver.implicitly_wait(10)
    #     # time.sleep(1)
    #     driver.find_element_by_css_selector('#anchor22').click()
    #     driver.implicitly_wait(10)
    #
    #     #  3) iframe 전환 : 로그인화면은 화면전체가 iframe
    #     driver.implicitly_wait(10)
    #     iframe = driver.find_element_by_css_selector('#dscert')
    #     driver.switch_to.frame(iframe)
    #     driver.implicitly_wait(10)
    #     time.sleep(0.5)
    #
    #     #  6) 공인인증서 선택
    #     driver.implicitly_wait(10)
    #     driver.find_element_by_css_selector('#row0dataTable').click()
    #     driver.implicitly_wait(3)
    #
    #     #  7) 패스워드 입력
    #     driver.implicitly_wait(3)
    #     passwd = 'djkbg-4107'
    #     driver.find_element_by_id('input_cert_pw').send_keys(passwd)
    #     driver.implicitly_wait(3)
    #
    #     #  8) 확인버튼 클릭
    #     driver.find_element_by_id('btn_confirm_iframe').click()
    #     time.sleep(2)
    #
    #     # 팝업창 닫기
    #     main = driver.window_handles
    #     for handle in main:
    #         if handle != main[0]:
    #             driver.switch_to_window(handle)
    #             driver.close()
    #     sys.exit()
    #
    # elif select_work == "2":
    #
    #     # 1.크롬접속
    #     driver = webdriver.Chrome("c:\chromedriver.exe")
    #
    #     # 2. 홈택스 접속
    #
    #     #  1) 홈택스로 이동
    #     driver.get('https://www.hometax.go.kr/')
    #     driver.implicitly_wait(10)
    #     driver.maximize_window()
    #
    #     #  2) 로그인화면으로 이동
    #     driver.implicitly_wait(10)
    #     time.sleep(1)
    #     driver.find_element_by_id('textbox81212912').click()
    #     time.sleep(2)
    #     driver.implicitly_wait(10)
    #
    #     #  3) iframe 전환 : 로그인화면은 화면전체가 iframe
    #     iframe = driver.find_element_by_css_selector('#txppIframe')
    #     driver.switch_to.frame(iframe)
    #     driver.implicitly_wait(10)
    #     time.sleep(0.5)
    #
    #     # 공동인증서 추가된 페이지 버튼 클릭
    #     driver.implicitly_wait(10)
    #     driver.find_element_by_css_selector('#anchor22').click()
    #     driver.implicitly_wait(10)
    #
    #     #  3) iframe 전환 : 로그인화면은 화면전체가 iframe
    #     driver.implicitly_wait(10)
    #     iframe = driver.find_element_by_css_selector('#dscert')
    #     driver.switch_to.frame(iframe)
    #     driver.implicitly_wait(10)
    #     time.sleep(0.5)
    #
    #     #  6) 공인인증서 선택
    #     driver.implicitly_wait(10)
    #     driver.find_element_by_css_selector('#row2dataTable').click()
    #     driver.implicitly_wait(3)
    #
    #     #  7) 패스워드 입력
    #     driver.implicitly_wait(3)
    #     passwd = 'djkbg-4107'
    #     driver.find_element_by_id('input_cert_pw').send_keys(passwd)
    #     driver.implicitly_wait(3)
    #
    #     #  8) 확인버튼 클릭
    #     driver.find_element_by_id('btn_confirm_iframe').click()
    #     time.sleep(2)
    #
    #     # 팝업창 닫기
    #     main = driver.window_handles
    #     for handle in main:
    #         if handle != main[0]:
    #             driver.switch_to_window(handle)
    #             driver.close()
    #     sys.exit()
    #
    # else:
    #     print("")
    #     print("응?")
    #     print("")
    #     continue
    # break



