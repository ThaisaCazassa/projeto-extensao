from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Carrega o arquivo KV que define a interface das telas
Builder.load_file('screens/main.kv')
Builder.load_file('screens/book_entry.kv')

class MainScreen(Screen):
    pass

class BookEntryScreen(Screen):
    pass

class BookApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(BookEntryScreen(name='book_entry'))
        return sm

if __name__ == '__main__':
    BookApp().run()
