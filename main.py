from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.textinput import TextInput
Builder.load_file('madhuram.kv')
import csv


class Registration(Widget):
    f_name = ObjectProperty(None)
    l_name = ObjectProperty(None)
    age = ObjectProperty(None)
    mobile = ObjectProperty(None)
    address = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(Registration, self).__init__(**kwargs)
        self.first_name = ''
        self.last_name = ''
        self.age = ''
        self.mobile_number = ''
        self.address = ''

    def clear_field(self):
        self.first_name_input.text = ''
        self.last_name_input.text = ''
        self.age_input.text = ''
        self.mobile_input.text = ''
        self.address_input.text = ''

    def submit(self):
        self.first_name = self.first_name_input.text
        self.last_name = self.last_name_input.text
        self.age = self.age_input.text
        self.mobile_number = self.mobile_input.text
        self.address = self.address_input.text
        print([self.first_name , self.last_name , self.age, self.mobile_number, self.address])

        db_line = [self.first_name, self.last_name, self.age, self.mobile_number, self.address]
        self.clear_field()
        with open('database.csv', 'a') as db:
            db_open = csv.writer(db)
            db_open.writerow(db_line)


    def cancel(self):
        print("Cancelled")

class MadhuramApp(App):
    def build(self):
        return Registration()

    #def input(self):
     #   self.first_name = self.root.ids.f_name.text


# if __name__ == '__main.py__':
MadhuramApp().run()
