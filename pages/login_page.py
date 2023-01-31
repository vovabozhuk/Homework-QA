from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    expected_title = 'Scouts panel - sign in'

    def get_page_title(self, url):
        return self.driver.title

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password_field(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title
