from selene import have, command
from demoqa_tests import resource
import allure


class RegistrationPage:

    def __init__(self, browser):
        self.browser = browser
        self.state = browser.element('#state')

    @allure.step('Open demoqa Practice Form')
    def open(self):
        self.browser.open('https://demoqa.com/automation-practice-form')

    @allure.step('Remove banners')
    def remove_banners(self):
        self.browser.driver.execute_script("$('footer').remove()")
        self.browser.driver.execute_script("$('#fixedban').remove()")

    @allure.step('Fill First name {value}')
    def fill_first_name(self, value):
        self.browser.element('#firstName').set(value)

    @allure.step('Fill Last name {value}')
    def fill_last_name(self, value):
        self.browser.element('#lastName').set(value)

    @allure.step('Fill email {value}')
    def fill_email(self, value):
        self.browser.element('#userEmail').set(value)

    @allure.step('Select gender {value}')
    def select_gender(self, value):
        self.browser.element(f'[name=gender][value={value}]+label').click()

    @allure.step('Fill phone number {value}')
    def fill_phone_number(self, value):
        self.browser.element('#userNumber').set(value)

    @allure.step('Fill date of birth {year} {month} {day}')
    def fill_date_of_birth(self, year, month, day):
        self.browser.element('#dateOfBirthInput').click()
        self.browser.element('.react-datepicker__year-select').send_keys(year)
        self.browser.element('.react-datepicker__month-select').send_keys(month)
        self.browser.element(f'.react-datepicker__day--0{day}').click()

    @allure.step('Fill subject {value}')
    def fill_subject(self, value):
        self.browser.element('#subjectsInput').send_keys(value).press_enter()

    @allure.step('Choose hobbie {value}')
    def choose_hobbie(self, value):
        self.browser.all('#hobbiesWrapper .custom-checkbox').element_by(
            have.exact_text(value)
        ).click()

    @allure.step('Select a picture to upload {name}')
    def upload_picture(self, name):
        self.browser.element('#uploadPicture').send_keys(resource.path(name))

    @allure.step('Fill current address {value}')
    def fill_address(self, value):
        self.browser.element('#currentAddress').send_keys(value)

    @allure.step('Fill state {name}')
    def fill_state(self, name):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        self.browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()

    @allure.step('Fill city {name}')
    def fill_city(self, name):
        self.browser.element('#city').click()
        self.browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(name)
        ).click()

    @allure.step('Click Submit')
    def submit(self):
        self.browser.element('#submit').press_enter()

    @allure.step('Registration verification')
    def should_registered_user_with(
        self,
        full_name,
        email,
        gender,
        user_number,
        date_of_birth,
        subjects,
        hobbies,
        picture,
        address,
        state_city,
    ):
        self.browser.all('.table-responsive td:nth-child(2)').should(
            have.exact_texts(
                full_name,
                email,
                gender,
                user_number,
                date_of_birth,
                subjects,
                hobbies,
                picture,
                address,
                state_city,
            )
        )

    # def attach_files(self):
    #     attach.add_html(browser)
    #     attach.add_screenshot(browser)
    #     attach.add_logs(browser)
