from pages.homePage import HomePage
from pages.savedPage import SavedPage
from selenium import webdriver
import unittest





class Setup(unittest.TestCase):


    def setUp(self):
        self.PATH = "chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH)

        self.driver.implicitly_wait(10)
        print("Navigate to url")
        self.driver.get("https://controlc.com/")
        self.driver.fullscreen_window()


    def test_navigate_to_webpage(self):
        driver = self.driver
        home_page = HomePage(driver)
        print("Checking title and url of homepage")
        self.assertEqual(driver.title, home_page.TITLE, "title not correct")
        self.assertEqual(driver.current_url, home_page.URL, "home_page url not correct")

    def test_storing_plain_text(self):
        driver = self.driver
        title= "testing title"
        body = "this is the body of the message"
        home_page = HomePage(driver)
        saved_page = SavedPage(driver)
        home_page.enter_title(title)
        home_page.enter_body(body)
        home_page.click_submit_by_css()
        self.assertEqual(driver.current_url, saved_page.url, "saved_page url not correct")
        saved_page.click_link_xpath()
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        text_in_body = driver.find_element_by_tag_name('body').text
        print("verify the save text")
        self.assertEqual(text_in_body, body, "saved body does not have the same text")

    def test_unable_to_save(self):
        driver = self.driver
        title= "testing title"
        body = "this is the body of the message"
        empty_message = "Empty Paste\nWe have detected that you did not enter a paste. Contact us if you believe this is an error."
        home_page = HomePage(driver)
        home_page.enter_title(title)
        home_page.enter_body(body)
        driver.find_element_by_id(home_page.body_textbox_id).clear()
        home_page.click_submit_by_css()
        text_in_body = driver.find_element_by_css_selector(".whiteBG.rounded10.pad10").text
        print("verify message that saved was empty")
        self.assertEqual(text_in_body, empty_message, "error message in saving empty file is not correct")

    def test_functionality_buttons(self):
        driver = self.driver
        home_page = HomePage(driver)
        self.assertEqual(home_page.checking_functionality_bold(),"[tpb][/tpb]")
        self.assertEqual(home_page.checking_functionality_italic(), "[tpi][/tpi]")
        self.assertEqual(home_page.checking_functionality_under_line(), "[tpu][/tpu]")
        self.assertEqual(home_page.checking_functionality_strike(), "[tpstrike][/tpstrike]")
        self.assertEqual(home_page.checking_functionality_wrap_in_code(), "[tpcode][/tpcode]")
        home_page.click_code_syntax()







    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Complete")


if __name__ == '__main__':
    unittest.main()





















