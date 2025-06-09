# frontend/main.py

import requests  # for fetching data from FastAPI backend
from datetime import datetime  # for checking current hour
from kivy.app import App  # base app class
from kivy.lang import Builder  # loads .kv layout file
from kivy.uix.screenmanager import ScreenManager, Screen  # for switching between screens
from kivy.core.window import Window  # to define window size 
from kivy.uix.floatlayout import FloatLayout
import pytz # for timezone
from kivy.clock import Clock

from core.gradient_bg import GradientBackground

# Set initial window size (desktop only — won't affect Raspberry Pi fullscreen)
Window.size = (800, 480)

# Load the visual layout from KV file
Builder.load_file("screens/home.kv")

# Define your main screen (logic/controller for the home UI)
class HomeScreen(Screen):
    def on_enter(self):
        Clock.schedule_interval(self.update_datetime,1)

    def update_datetime(self, dt):
        # Define the US Central timezone
        central = pytz.timezone("US/Central")
        now = datetime.now(central)

        # Format time like "9:00 AM", no seconds, no leading zero on hour
        current_time = now.strftime("%I:%M %p").lstrip("0")
        current_date = now.strftime("%A, %B %d, %Y")

        # Update UI
        self.ids.time_label.text = current_time
        self.ids.date_label.text = current_date

    def fetch_message(self):
        """
        When user presses 'Connect to Backend', this fetches a message from FastAPI.
        """
        try:
            response = requests.get("http://localhost:8000/")
            if response.status_code == 200:
                data = response.json()
                self.ids.message_label.text = f"Backend says: {data['message']}"
            else:
                self.ids.message_label.text = "Error: Could not reach backend"
        except Exception as e:
            self.ids.message_label.text = f"Error: {str(e)}"

# This is the main application class
class TopiApp(App):
    def build(self):
        layout = FloatLayout()

        gradient = GradientBackground()
        layout.add_widget(gradient)

        # Initialize screen manager and add the home screen
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        layout.add_widget(sm)

        return layout

# This tells Python to run the app if the script is executed directly
if __name__ == "__main__":
    TopiApp().run()
