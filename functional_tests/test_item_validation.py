from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
   
   def test_cannot_add_empty_list_items(self):
       # Edith goes to the home page and accidentally tries to submit
       # an empty list item. She hits Enter on the empty input box
       self.browser.get(self.live_server_url)                  
       self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
       

       # The home page refreshes, and there is an error message saying
       # that list items cannot be blank
       self.wait_for(lambda:self.assertEqual(
           self.browser.find_element_by_css_selecetor('.has.error').text, "You can't have an empty list item"
       ))

       # Perversely, she now decides to submit a second blank list item

       # She receives a similar warning on the list page

       # And she can correct it by filling some text in
       self.fail("Finish this test!")
