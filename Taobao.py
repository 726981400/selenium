#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2018/09/05
# 淘宝秒杀脚本，扫码登录版
import os
from selenium import webdriver
# from seleniumrequests import Chrome
import datetime
import time


# d = os.path.dirname(__file__)
# abspath = os.path.abspath(d)
#
# driver = webdriver.Chrome()
# driver.maximize_window()


def login(driver):
    # 打开淘宝登录页，并进行扫码登录
    driver.get("https://www.taobao.com")
    time.sleep(3)
    if driver.find_element_by_link_text("亲，请登录"):
        driver.find_element_by_link_text("亲，请登录").click()
    print("当前url为：",driver.current_url)

    print("请在30秒内完成扫码")
    time.sleep(30)
    print("当前url为：", driver.current_url)

    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)

    if driver.find_element_by_id("J_SelectAll1"):
        driver.find_element_by_id("J_SelectAll1").click()

    time.sleep(3)
    print("当前url为：", driver.current_url)
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S:%f'))


def buy(driver,buytime):
    print("当前url为：", driver.current_url)
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print("当前时间" + now)
        # 对比时间，时间到的话就点击结算
        if now > buytime:
            try:
                # 点击结算按钮
                if driver.find_element_by_id("J_Go"):
                    driver.find_element_by_id("J_Go").click()
                    # driver.forward()
                hands = driver.window_handles  # 获取所有的句柄
                driver.switch_to.window(hands[-1])  # 直接获取hands这个list数据里面最后1个hand的值,切换到最后一个窗口
                # driver.post('https://buy.tmall.com/order/confirm_order.htm?spm=a1z0d.6639537.0.0.undefined')
                # js ='document.getElementByClass("go-btn").[0].click();'
                # driver.execute_scrtip(js)
                try:
                    driver.find_element_by_link_text('提交订单').click()
                    print('提交订单成功')
                    break
                except:
                    print('提交订单失败')

                #hands = driver.window_handles  # 获取所有的句柄

                #driver.switch_to.window(hands[-1])  # 直接获取hands这个list数据里面最后1个hand的值,切换到最后一个窗口
                # driver.find_element_by_css_selector("submitOrder-container .go-btn").click()

            except:
                time.sleep(0.1)
        print(now)
        time.sleep(0.1)


def main():
    times = input("请输入抢购时间：")
    d = os.path.dirname(__file__)
    abspath = os.path.abspath(d)

    driver = webdriver.Chrome()
    driver.maximize_window()

    login(driver)
    buy(driver,times)

if __name__ == "__main__":
    # times = "2020-06-05 12:00:00.000000"
    # # 时间格式："2018-09-06 11:20:00.000000"
    # login()
    # buy(times)
    main()