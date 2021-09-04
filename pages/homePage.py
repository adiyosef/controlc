class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.URL = "https://controlc.com/"
        self.TITLE = "ControlC Pastebin - The easiest way to host your text"
        self.title_textbox_id = "paste_title"
        self.body_textbox_id = "input_text"
        self.submit_buttom_css = "input.btn.btn-primary"
        self.code_syntax_id = "codeSyntax"




    def enter_title(self, title):
        print("Entering title text")
        self.driver.find_element_by_id(self.title_textbox_id).clear()
        self.driver.find_element_by_id(self.title_textbox_id).send_keys(title)

    def enter_body(self, body):
        print("Entering body text")
        self.driver.find_element_by_id(self.body_textbox_id).clear()
        self.driver.find_element_by_id(self.body_textbox_id).send_keys(body)

    def click_submit_by_css(self):
        print("Clicking submit button")
        self.driver.find_element_by_css_selector(self.submit_buttom_css).click()



    def checking_functionality_bold(self):
        print("Clicking the bold button")
        self.driver.find_element_by_id(self.body_textbox_id).clear()
        self.driver.find_element_by_css_selector(".cursor:nth-child(1)").click()
        value =(self.driver.find_element_by_id(self.body_textbox_id).get_attribute("value"))
        return value


    def checking_functionality_italic(self):
        print("Clicking the italic button")
        self.driver.find_element_by_id(self.body_textbox_id).clear()
        self.driver.find_element_by_css_selector(".cursor:nth-child(2)").click()
        value =(self.driver.find_element_by_id(self.body_textbox_id).get_attribute("value"))
        return value

    def checking_functionality_under_line(self):
        print("Clicking the under_line button")
        self.driver.find_element_by_id(self.body_textbox_id).clear()
        self.driver.find_element_by_css_selector(".cursor:nth-child(3)").click()
        value =(self.driver.find_element_by_id(self.body_textbox_id).get_attribute("value"))
        return value

    def checking_functionality_strike(self):
        print("Clicking the strike button")
        self.driver.find_element_by_id(self.body_textbox_id).clear()
        self.driver.find_element_by_css_selector(".cursor:nth-child(4)").click()
        value =(self.driver.find_element_by_id(self.body_textbox_id).get_attribute("value"))
        return value


    def checking_functionality_wrap_in_code(self):
        print("Clicking the wrap_in_code button")
        self.driver.find_element_by_id(self.body_textbox_id).clear()
        self.driver.find_element_by_css_selector(".cursor:nth-child(6)").click()
        value =(self.driver.find_element_by_id(self.body_textbox_id).get_attribute("value"))
        return value

    def click_code_syntax(self):
        print("Clicking the Enable code highlighting button")
        self.driver.find_element_by_id(self.code_syntax_id).click()




