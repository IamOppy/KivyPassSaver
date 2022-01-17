from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from dataB import DBtable

Builder.load_file('screens.kv')


class LoginScreen(Screen):
    def validate_user(self):
        username_query_ = self.manager.current_screen.ids.username_query.text
        password_query_ = self.manager.current_screen.ids.password_query.text
        if username_query_ and password_query_:
            self.manager.current = "menu_screen"
        else:
            print("Wrong Username/Password")

class MenuScreen(Screen):
    def create_login(self):
        self.manager.current = "save_screen"

    def view_logins(self):
        pass

class SaveScreen(Screen):
    def save_info(self):
        username_Query = self.manager.current_screen.ids.save_username.text
        password_Query = self.manager.current_screen.ids.save_password.text
        website_Query = self.manager.current_screen.ids.save_password.text
        if username_Query and password_Query and website_Query:
                self.save_Login = DBtable(website_Query, username_Query, password_Query)
                self.save_Login.add()
                print('Saved Sucessfully')



class RootWidget(ScreenManager):
    pass



class MainApp(App):
    def build(self):
        return RootWidget()

MainApp().run()