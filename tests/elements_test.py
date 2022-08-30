import os
import time
from pages.elements_page import AdminLoginPage, UserRegisterPage


class TestElementsOnPage:

    class TestAdminLoginPage:
        def test_admin_login(self, driver):
            admin_login_page = AdminLoginPage(driver, os.getenv('PAGE_URL') or 'https://some-page.com')
            admin_login_page.open()
            admin_login_page.fill_admin_login_fields()
            time.sleep(5)

    class TestUserRegister:
        def test_user_register_assessment(self, driver):
            user_register_assessment = UserRegisterPage(driver, os.getenv('PAGE_URL') or 'https://some-page.com')
            user_register_assessment.open()
            user_register_assessment.fill_user_register_fields()
            #time.sleep(5)
            #assert 'Happify: Science-Based Activities and Games' in driver.title



# Lesson 235.2



