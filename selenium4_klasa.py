class LoginPage:
    def __init__(self, ddriver, user, passwd, login_button):
        self.ddriver = ddriver
        self. username_field = user
        self.password_field = passwd
        self.login_button = login_button

    def open(self):
        self.ddriver.get('http://www.saucedemo.com')

    def enter_username(self, username_data):
        field = self.ddriver.find_element('id', self.username_field)
        field.clear()
        field.send_keys(username_data)

    def enter_password(self, password_data):
        field = self.ddriver.find_element('id', self.password_field)
        field.clear()
        field.send_keys(password_data)

    def click_login_button(self):
        button = self.ddriver.find_element('id', self.login_button)
        button.click()
