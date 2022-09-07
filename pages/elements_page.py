import datetime
import random
import time
from selenium.webdriver.common.action_chains import ActionChains
from locators.elements_page_locators import AdminLoginPageLocators, UserRegisterPageLocators, SiteMainPageOpenLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class AdminLoginPage(BasePage):

    locators = AdminLoginPageLocators()

    def fill_admin_login_fields(self):
        self.element_is_visible(self.locators.ADMIN_PAGE_EMAIL_FIELD).send_keys('gtest@qwerty.com')
        self.element_is_visible(self.locators.ADMIN_PAGE_PASSWD_FIELD).send_keys('password')

        # need make check for checkbox element - checked/unchecked
        # self.element_is_visible(self.locators.ADMIN_PAGE_AGREE_CHECKBOX_LOGIN).click()

        self.element_is_visible(self.locators.ADMIN_PAGE_LOGIN_BUTTON).click()

        # can be deleted - later *************************
        # time.sleep(3)
        # self.element_is_visible(self.locators.ADMIN_ANNA_MAIN_MENU).click()
        # time.sleep(3)
        # self.element_is_visible(self.locators.ADMIN_ANNA_DIALOGS).click()
        # time.sleep(3)

        # actions = ActionChains(self.driver)
        # #actions.build()
        # actions.click(self.locators.ADMIN_ANNA_MAIN_MENU)
        # actions.perform()
        # # time.sleep(3)
        # self.element_is_visible(self.locators.ADMIN_ANNA_DIALOG_ASSET).click()
        # *****************************************


# user register
class UserRegisterPage(BasePage):

    locators = UserRegisterPageLocators()

    def click_started_main_page_button(self):
        self.element_is_visible(self.locators.GET_STARTED_MAIN_PAGE_BUTTON).click()
        time.sleep(3)

    def click_started_today_button(self):
        self.element_is_visible(self.locators.GET_STARTED_TODAY_BUTTON).click()
        time.sleep(3)

    def click_random_gender_radio_box(self):
        self.element_is_visible(self.locators.GENDER_RADIO_BOX).click()
        time.sleep(3)

    def click_age_radio_box(self):
        self.element_is_present(self.locators.AGE_RADIO_BOX).click()
        time.sleep(3)

    # def click_race_box(self):
    #     # self.element_is_visible(self.locators.RACE_BOX).click()
    #     # time.sleep(3)
    #
    #     # item_list = self.elements_are_visible(self.locators.ITEM_TITLE)
    #     # item = item_list[random.randint(1, 5)]
    #     # self.go_to_element(item)
    #     # item.click()
    #
    #     item_list = self.elements_are_visible(self.locators.ITEM_TITLE)
    #     count = 11
    #     while count != 0:
    #         item = item_list[random.randint(1, 5)]
    #         if count > 0:
    #             self.go_to_element(item)
    #             item.click()
    #             print(item)
    #             count -= 1
    #         else:
    #             break

    def click_race_checkbox_items(self):
        item_list = self.elements_are_visible(self.locators.CHECKBOX_ITEM_TITLE)
        count = 8
        while count != 0:
            item = item_list[random.randint(1, 7)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                print(item.text)
                count -= 1
            else:
                break

    def click_next_button(self):
        self.element_is_visible(self.locators.NEXT_BUTTON).click()
        time.sleep(3)

    def click_job_radio_box(self):
        self.element_is_present(self.locators.JOB_RADIO_BOX).click()
        time.sleep(3)

    def click_relationship_radio_box(self):
        self.element_is_present(self.locators.RELATIONSHIP_RADIO_BOX).click()
        time.sleep(3)

    def click_kids_check_box(self):
        item_list = self.elements_are_visible(self.locators.CHECKBOX_ITEM_TITLE)
        count = 6
        while count != 0:
            item = item_list[random.randint(1, 5)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                print(item.text)
                count -= 1
            else:
                break

    def click_kids_next_button(self):
        self.element_is_visible(self.locators.KIDS_NEXT_BUTTON).click()
        time.sleep(3)

    def click_adversity_radio_box(self):
        self.element_is_visible(self.locators.ADVERSITY_RADIO_BOX).click()
        time.sleep(3)

    def click_connected_others_radio_box(self):
        self.element_is_visible(self.locators.CONNECTED_OTHERS_RADIO_BOX).click()
        time.sleep(3)

    def click_stressful_situation_radio_box(self):
        self.element_is_visible(self.locators.STRESSFUL_SITUATION_RADIO_BOX).click()
        time.sleep(3)

    def click_experience_of_moment_radio_box(self):
        self.element_is_visible(self.locators.EXPERIENCE_OF_MOMENT_RADIO_BOX).click()
        time.sleep(3)

    def click_meditation_radio_box(self):
        self.element_is_visible(self.locators.MEDITATION_RADIO_BOX).click()
        time.sleep(3)

    def click_conditions_check_box(self):
        item_list = self.elements_are_present(self.locators.CHECKBOX_ITEM_TITLE)
        count = 6
        while count != 0:
            item = item_list[random.randint(1, 5)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                print(item.text)
                count -= 1
            else:
                break

    def click_conditions_next_button(self):
        self.element_is_visible(self.locators.CONDITIONS_NEXT_BUTTON).click()
        time.sleep(3)

    def enter_user_register_data(self):
        self.element_is_visible(self.locators.USERNAME_FIELD).send_keys("gadzhi")
        self.element_is_visible(self.locators.EMAIL_ADDRESS_FIELD).send_keys(
            "gkurban" + "+lvtest" + dt_str + "@qwerty.com")
        self.element_is_visible(self.locators.PASSWORD_FIELD).send_keys("p@ssw0rD")
        self.element_is_visible(self.locators.CONFIRM_PASSWORD_FIELD).send_keys("p@ssw0rD")
        time.sleep(3)
        self.element_is_visible(self.locators.REGISTER_AGREE_CHECKBOX).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CONTINUE_BUTTON).click()
        time.sleep(7)

    def create_user_account(self):
        self.element_is_visible(self.locators.FIRST_NAME_FIELD).send_keys("gadzhi")
        self.element_is_visible(self.locators.LAST_NAME_FIELD).send_keys("gg")
        time.sleep(3)
        self.element_is_visible(self.locators.MONTH_SELECT_FIELD).click()
        time.sleep(3)
        self.element_is_visible(self.locators.DAY_SELECT_FIELD).click()
        time.sleep(3)
        self.element_is_visible(self.locators.YEAR_SELECT_FIELD).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CREATE_ACC_CONTINUE_BUTTON).click()

    def privacy_settings_data(self):
        self.element_is_visible(self.locators.PRIVATE_MODE_BOX).click()
        self.element_is_visible(self.locators.PRIVATE_CONTINUE_BUTTON).click()

    def start_free_track(self):
        self.element_is_visible(self.locators.START_FREE_TRACK_BUTTON).click()

    def happify_work_modal(self):
        self.element_is_visible(self.locators.HOW_HAPPIFY_WORK_SLIDE_BUTTON).click()
        self.element_is_visible(self.locators.BASIC_SKILLS_SLIDE_BUTTON).click()
        self.element_is_visible(self.locators.EMOTIONAL_WELL_BEING_SLIDE_BUTTON).click()

    # def click_random_element(self):
    #     item_list = self.elements_are_visible(self.locators.GENDER_BOX)
    #     for item in item_list:
    #         print(item.text)


dat_obj = datetime.datetime.now()
dt_str = dat_obj.strftime("%f")


class SiteMainPageOpen(BasePage):

    locators = SiteMainPageOpenLocators()

    def main_page_load_time(self):
        self.element_is_visible(self.locators.HOME_PAGE_LOAD_TIME).click()


