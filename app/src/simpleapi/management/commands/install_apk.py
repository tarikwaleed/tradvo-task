from django.core.management.base import BaseCommand
from appium import webdriver
import time
from appium.webdriver.webdriver import AppiumOptions

class Command(BaseCommand):
    help = "Install an APK on the Android emulator"

    def handle(self, *args, **kwargs):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Samsung Galaxy S10',  # Use 'adb devices' to check the emulator name
            'app': '/app/apks/test.apk',  # Path inside the container where the APK is located
            'automationName': 'UiAutomator2',
        }

        appium_options = AppiumOptions()
        appium_options.load_capabilities(desired_caps)
        driver = webdriver.Remote('http://android-emulator:4723', options=appium_options)
        time.sleep(10)  # Give some time for the installation to complete

        # Take a screenshot of the initial screen after installation
        screenshot_path = '/app/screenshots/1.png'
        driver.save_screenshot(screenshot_path)

        self.stdout.write(self.style.SUCCESS('APK installed and screenshot taken!'))

        # Close the session
        driver.quit()
