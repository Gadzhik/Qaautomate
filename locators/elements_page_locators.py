from selenium.webdriver.common.by import By


class AdminLoginPageLocators:

    # admin page elements
    ADMIN_PAGE_EMAIL_FIELD = (By.XPATH, "//input[@id='email']")
    ADMIN_PAGE_PASSWD_FIELD = (By.XPATH, "//input[@id='password']")
    ADMIN_PAGE_AGREE_CHECKBOX_LOGIN = (By.XPATH, "//input[@id='agree_rules']")
    ADMIN_PAGE_LOGIN_BUTTON = (By.XPATH, "//form[@id='sign-in-form']//*[@class='btn btn-primary']")

    # anna menu elements
    ADMIN_ANNA_MAIN_MENU = (By.XPATH, "//a[text()='Anna']")
    ADMIN_ANNA_DIALOGS = (By.XPATH, "//li[@class='dropdown-submenu active']")
    ADMIN_ANNA_DIALOG_ASSET = (By.XPATH, "//a[text()='Dialog Assets']")

    # dialog-asset page elements
    DIALOG_ASSET_SEARCH_FIELD = (By.XPATH, "//input[@class='input-xlarge']")
    DIALOG_ASSET_HPML_FIELD = (By.XPATH, "//a[text()='Get HPML']")
    #DIALOG_ASSET_GET_SKELETON_SKIN_FIELD = (By.XPATH, "")
    DIALOG_ASSET_GET_BASE_SKIN_FIELD = (By.XPATH, "//a[text()='Get Base Skin Template']")
    DIALOG_ASSET_GET_TASK_SKIN_FIELD = (By.XPATH, "")
    DIALOG_ASSET_RUN_ASSESSMENT_FIELD = (By.XPATH, "")
    DIALOG_ASSET_RUN_COMPASS_FIELD = (By.XPATH, "")


class UserRegisterPageLocators:

    # user register page elements
    GET_STARTED_MAIN_PAGE_BUTTON = (By.XPATH, "//div[@class='first-section_buttons']//button[@id='mainContentStart']")
    GET_STARTED_TODAY_BUTTON = (By.XPATH, "//div[@class='nav d-flex justify-content-center']//button[@class='button "
                                          "blue js-quiz mx-0 first-focus']")
    GENDER_BOX = (By.XPATH, "//span[@id='answer_0']")

    AGE_BOX = (By.XPATH, "//span[@id='answer_3']")

    RACE_BOX = (By.XPATH, "//a[@id='answer_6']")
    NEXT_BUTTON = (By.XPATH, "//button[@class='button bottom js-multi-answer']")

    JOB_BOX = (By.XPATH, "//span[@id='answer_2']")

    RELATIONSHIP_BOX = (By.XPATH, "//span[@id='answer_0']")

    KIDS_BOX = (By.XPATH, "//a[@id='answer_2']")
    KIDS_NEXT_BUTTON = (By.XPATH, "//button[@class='button bottom js-multi-answer']")

    ADVERSITY_BOX = (By.XPATH, "//span[@id='answer_2']")

    CONNECTED_OTHERS_BOX = (By.XPATH, "//span[@id='answer_2']")

    STRESSFUL_SITUATION_BOX = (By.XPATH, "//span[@id='answer_2']")

    EXPERIENCE_OF_MOMENT_BOX = (By.XPATH, "//span[@id='answer_2']")

    MEDITATION_BOX = (By.XPATH, "//span[@id='answer_2']")

    CONDITIONS_BOX = (By.XPATH, "//a[@id='answer_0']")
    CONDITIONS_NEXT_BUTTON = (By.XPATH, "//button[@class='button bottom js-multi-answer']")

    USERNAME_FIELD = (By.XPATH, "//input[@type='text']")

    EMAIL_ADDRESS_FIELD = (By.XPATH, "//input[@type='email']")

    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")

    CONFIRM_PASSWORD_FIELD = (By.XPATH, "//input[@name='cpassword']")

    REGISTER_AGREE_CHECKBOX = (By.XPATH, "//label[@class='terms_box-label']")

    CONTINUE_BUTTON = (By.XPATH, "//button[@class='button orange uppercase js-submit']")

    # create account
    FIRST_NAME_FIELD = (By.XPATH, "//input[@id='first-name-input']")

    LAST_NAME_FIELD = (By.XPATH, "//input[@id='last-name-input']")

    DATE_OF_BIRTH_FIELD = (By.XPATH, "//div[@id='dob-container']")

    CREATE_ACC_CONTINUE_BUTTON = (By.XPATH, "//div[@class='ModalForm_group ModalForm_group-btn flname']")

    # privacy settings
    PRIVATE_MODE_BOX = (By.XPATH, "//div[@class='check aria-radio selected']")

    PRIVATE_CONTINUE_BUTTON = (By.XPATH, "//button[@class='button orange js-continue']")

    # start free track
    START_FREE_TRACK_BUTTON = (By.XPATH, "//a[@class='button orange']")

    # happify work modal
    HOW_HAPPIFY_WORK_SLIDE_BUTTON = (By.XPATH, "//div[@class='intro-slide slide-1 viewed']//button[@class='next "
                                               "js-forward button-back']")

    BASIC_SKILLS_SLIDE_BUTTON = (By.XPATH, "//div[@class='intro-slide slide-2 viewed']//button[@class='next "
                                           "js-forward button-back']")

    EMOTIONAL_WELL_BEING_SLIDE_BUTTON = (By.XPATH, "//button[@class='next js-close button-next']")



