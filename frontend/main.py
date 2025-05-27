# frontend/main.py

import requests
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.app import App

Builder.load_file("screens/home.kv")

class HomeScreen(Screen):
    def fetch_message(self):
        try:
            response = requests.get("http://localhost:8000/")
            if response.status_code == 200:
                data = response.json()
                self.ids.message_label.text = f"Backend says: {data['message']}"
            else:
                self.ids.message_label.text = "Error: Could not reach backend"
        except Exception as e:
            self.ids.message_label.text = f"Error: {str(e)}"

class TopiApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        return sm

if __name__ == "__main__":
    TopiApp().run()
