from Framework.BaseElement import BaseElement

# Class for textbox elements
class TextBox(BaseElement):

    def enter_data(self,data):
        # enters values into the textbox
        element = self.find_element()
        element.click()
        element.send_keys(data)
