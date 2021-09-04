class SavedPage:

    def __init__(self, driver):
        self.driver = driver

        self.url = "https://controlc.com/index.php?act=submit"
        self.view_paste_xpath = "//b[contains(text(),'Click here')]"
        self.iframe_box_id = "pasteFrame"



    def click_link_xpath(self):
        print("Clicking link to view saved text")
        self.driver.find_element_by_xpath(self.view_paste_xpath).click()
