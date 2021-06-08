import time

from appium import webdriver

info = {
    'platformName': 'Android',
    'platformVersion': '7.1.1',
    'deviceName': '127.0.0.1:62001',
    # 获得包名adb shell dumpsys window|findstr mCurrent
    'appPackage': 'com.baidu.homework',
    'appActivity': 'com.baidu.homework.activity.init.InitActivity',
    'noRest': False
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', info)



#定位指定的元素
driver.find_element_by_id('com.baidu.homework:id/iknow_alert_dialog_button2').click()
#跳过权限
time.sleep(1)
driver.find_element_by_id('com.baidu.homework:id/tv_agree_next').click()
#等待6S
time.sleep(1)
#跳过广告
#driver.find_element_by_id('com.baidu.homework:id/adx_splash_skip_text').click()
driver.find_element_by_xpath("//*[@content-desc='跳过']").click()
#跳过注册
time.sleep(1.5)
driver.find_element_by_id('com.baidu.homework:id/common_ui_titlebar_text_view_id').click()
#学生身份
time.sleep(1)
driver.find_element_by_id('com.baidu.homework:id/larci_identity_student').click()
#年级选择
time.sleep(1)
driver.find_element_by_id('android.widget.RadioButton').click()
#完成选择
time.sleep(1)
driver.find_element_by_id('com.baidu.homework:id/larcng_information_entry_completion').click()


#结束进程
#driver.quit()
