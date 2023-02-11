from Framework.BaseElement import BaseElement
#Пока не знаю, что сюда писать

class TextBox(BaseElement):
    def enter_data(self,data):
        element = self.find_element()
        element.click()
        element.send_keys(data)