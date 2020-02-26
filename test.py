"""
Qxf2: Example script to run one test against ATP_WTA app using Appium
The test will navigate to ATP Singles Rankings list and confirm that Novak
Djokovic is the top player listed and get his personal details from a table.

"""
import unittest, time, os
from appium import webdriver
from time import sleep


class Android_ATP_WTA(unittest.TestCase):
    "Class to run tests against the Phone dialer app"

    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'fda96ada'
        # Since the app is already installed launching it using package and activity name
        desired_caps['appPackage'] = 'com.android.dialer'
        desired_caps['appActivity'] = 'com.android.dialer.TwelveKeyDialer'
        # Adding appWait Activity since the activity name changes as the focus shifts to the ATP WTA app's first page
        desired_caps['appWaitActivity'] = 'com.android.dialer.TwelveKeyDialer'
        self.driver = webdriver.Remote('http://localhost:4722/wd/hub', desired_caps)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_atp_wta(self):
        pass


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_ATP_WTA)
    unittest.TextTestRunner(verbosity=2).run(suite)