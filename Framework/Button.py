from Framework.BaseElement import BaseElement
#Пока не знаю, что сюда писать

class Button(BaseElement):
    def click_the_button(self):
        element = self.find_element()
        element.click()