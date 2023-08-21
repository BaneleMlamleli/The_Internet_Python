from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from toolium.driver_wrapper import DriverWrapper
from hamcrest import assert_that, equal_to

class ABTestingDomain(PageObject):
    
    # def init_page_elements(self):
    #     self.clickHref = Link(By.XPATH, "//a[normalize-space()='A/B Testing']")
    #     self.redirectedSuccessfully = Text(By.XPATH, "//h3[normalize-space()='A/B Test Control']")
    
    # FIXME: The browser launches but the website does not get opened   
    def home_page(self):
        """
        Making sure we're on the home page
        """
        print("inside home_page method")
        self.driver.get(''.format(self.config.get('Test', 'url')))
        # self.driver.get("https://the-internet.kineticskunk.co.za/")
        self.driver.implicitly_wait(10) # seconds
        return self
    
    # FIXME: As a result of the website not being opened, program is unable to locate the element
    def click_link(self, ab_testing):
        print("inside the click_link method")
        # self.clickHref.click()
        self.driver.find_element(By.XPATH, f"//a[normalize-space()='{ab_testing}']").click()
        return self
    
    def redirect(self):
        print("inside the redirect method")
        # self.redirectedSuccessfully.is_displayed()
        self.driver.find_element(By.XPATH, "//h3[normalize-space()='A/B Test Control']").is_displayed()
        return self
        
        # assert_that(self.redirectedSuccessfully, equal_to(True), "Error. Check if page redirected correctly or if element exist")
        