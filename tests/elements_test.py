import os
import time

import requests

from pages.elements_page import AdminLoginPage, UserRegisterPage, SiteMainPageOpen


class TestElementsOnPage:

    class TestAdminLoginPage:
        def test_admin_login(self, driver):
            admin_login_page = AdminLoginPage(driver, os.getenv('PAGE_URL') or 'https://some-page.com')
            admin_login_page.open()
            admin_login_page.fill_admin_login_fields()
            time.sleep(5)

    class TestUserRegister:
        def test_user_register_assessment(self, driver):
            user_register_assessment = UserRegisterPage(driver, os.getenv('PAGE_URL') or 'https://some.site.com')
            user_register_assessment.open()
            user_register_assessment.click_started_main_page_button()
            user_register_assessment.click_started_today_button()
            user_register_assessment.click_random_gender_radio_box()
            user_register_assessment.click_age_radio_box()
            user_register_assessment.click_race_checkbox_items()
            user_register_assessment.click_next_button()
            user_register_assessment.click_job_radio_box()
            user_register_assessment.click_relationship_radio_box()
            user_register_assessment.click_kids_check_box()
            user_register_assessment.click_kids_next_button()
            user_register_assessment.click_adversity_radio_box()
            user_register_assessment.click_connected_others_radio_box()
            user_register_assessment.click_stressful_situation_radio_box()
            user_register_assessment.click_experience_of_moment_radio_box()
            user_register_assessment.click_meditation_radio_box()
            user_register_assessment.click_conditions_check_box()
            user_register_assessment.click_conditions_next_button()
            user_register_assessment.enter_user_register_data()
            user_register_assessment.create_user_account()
            user_register_assessment.privacy_settings_data()
            time.sleep(5)

    class TestMainPageLoadTime:
        # TC 2104 v.9088
        def test_main_page_load_time(self, driver):

            page_load_speed = requests.get("https://qwer.ty.com").elapsed.total_seconds()
            print(page_load_speed)



