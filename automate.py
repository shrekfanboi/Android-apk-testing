from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
class ATG:
    desired_cap = {
    "platformName": "android",
    "appActivity": "com.atg.world.activity.SplashActivity",
    "appWaitDuration": "5000",
    "appExecTimeout": "50000",
    "uiautomator2ServerLaunchTimeout": "50000",
    "uiautomator2ServerInstallTimeout": "50000",
    "appPackage": "com.ATG.World",
    "deviceName": "emulator-5554",
    "driver": "http://localhost:4723/wd/hub",
    'autoGrantPermissions': "true",
    'autoDismissAlerts':"true",
    "autoAcceptAlerts": "true",
}
    def __init__(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', ATG.desired_cap)

    def test_LoginWithRightCredential(self):
        get_started = self.driver.find_element_by_id("com.ATG.World:id/getStartedTv")
        get_started.click()
        self.driver.implicitly_wait(5)
        loggin = self.driver.find_element_by_id("com.ATG.World:id/login_email")
        loggin.click()
        email = self.driver.find_element_by_id("com.ATG.World:id/email")
        email.send_keys("wiz_saurabh@rediffmail.com")
        password = self.driver.find_element_by_id("com.ATG.World:id/password")
        password.send_keys("Pass@123")
        signin = self.driver.find_element_by_id("com.ATG.World:id/email_sign_in_button")
        signin.click()
        print("test_LoginWithRightCredential passed")
    
    def test_PostImageFromCamera(self):
        TouchAction(self.driver).tap(x=521, y=1642).perform()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.ATG.World:id/image_fab_clicked").click()
        self.driver.find_elements_by_id("android:id/text1")[1].click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_accessibility_id("Shutter").click()
        self.driver.find_element_by_accessibility_id("Done").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.ATG.World:id/layout_select_group_container").click()
        self.driver.find_elements_by_id("com.ATG.World:id/group_tv")[0].click()
        self.driver.find_element_by_id("com.ATG.World:id/layout_group_list_done").click()
        self.driver.find_element_by_id("com.ATG.World:id/postCaption").send_keys("automation_test")
        self.driver.find_element_by_id("com.ATG.World:id/toolbar_post_action").click()


if __name__ == "__main__":
    test = ATG()
    test.test_LoginWithRightCredential()
    #clear popups now
    input('Y/N')
    test.test_PostImageFromCamera()
