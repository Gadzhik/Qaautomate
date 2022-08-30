import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains
from locators.elements_page_locators import AdminLoginPageLocators, UserRegisterPageLocators
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

    def fill_user_register_fields(self):
        time.sleep(3)
        self.element_is_visible(self.locators.GET_STARTED_MAIN_PAGE_BUTTON).click()
        time.sleep(3)
        self.element_is_visible(self.locators.GET_STARTED_TODAY_BUTTON).click()
        time.sleep(3)
        self.element_is_visible(self.locators.GENDER_BOX).click()
        time.sleep(3)
        self.element_is_visible(self.locators.AGE_BOX).click()
        time.sleep(3)
        self.element_is_visible(self.locators.RACE_BOX).click()
        time.sleep(3)
        self.element_is_visible(self.locators.NEXT_BUTTON).click()
        time.sleep(3)
        self.element_is_visible(self.locators.JOB_BOX).click()
        time.sleep(3)
        self.element_is_visible(self.locators.RELATIONSHIP_BOX).click()
        time.sleep(3)
        self.element_is_visible(self.locators.KIDS_BOX).click()
        time.sleep(3)
        self.element_is_visible(self.locators.KIDS_NEXT_BUTTON).click()
        time.sleep(3)
        self.element_is_visible(self.locators.ADVERSITY_BOX).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CONNECTED_OTHERS_BOX).click()
        time.sleep(3)
        self.element_is_visible(self.locators.STRESSFUL_SITUATION_BOX).click()
        time.sleep(3)
        self.element_is_visible(self.locators.EXPERIENCE_OF_MOMENT_BOX).click()
        time.sleep(3)
        self.element_is_visible(self.locators.MEDITATION_BOX).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CONDITIONS_BOX).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CONDITIONS_NEXT_BUTTON).click()
        time.sleep(3)

        self.element_is_visible(self.locators.USERNAME_FIELD).send_keys("gadzhi")
        self.element_is_visible(self.locators.EMAIL_ADDRESS_FIELD).send_keys(
            "gtest" + dt_str + "@qwerty.com")
        self.element_is_visible(self.locators.PASSWORD_FIELD).send_keys("password")
        self.element_is_visible(self.locators.CONFIRM_PASSWORD_FIELD).send_keys("password")
        time.sleep(3)
        self.element_is_visible(self.locators.REGISTER_AGREE_CHECKBOX).click()
        time.sleep(3)
        self.element_is_visible(self.locators.CONTINUE_BUTTON).click()


dat_obj = datetime.datetime.now()
dt_str = dat_obj.strftime("%f")
