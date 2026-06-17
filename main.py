from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class WorkoutApp(App):
    def build(self):
        # Mobile screen background color (Dark Theme)
        Window.clearcolor = (0.1, 0.1, 0.1, 1)
        
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # App Title & Welcome Message
        self.label = Label(
            text="🔥 FITNESS BOSS v1.0 🔥\n\nLevel: Beginner\nNext Exercise: Push-ups", 
            font_size='22sp',
            halign='center'
        )
        layout.add_widget(self.label)
        
        # Start Button
        btn_start = Button(
            text="WORKOUT SHURU KAREIN", 
            size_hint=(1, 0.25),
            background_color=(0, 0.7, 0.3, 1),
            font_size='18sp'
        )
        btn_start.bind(on_press=self.start_workout)
        layout.add_widget(btn_start)
        
        return layout

    def start_workout(self, instance):
        self.label.text = "💪 Push-ups Chalu Hai!\n\nSabaash Bhai, Rukna Mat!"

if __name__ == '__main__':
    WorkoutApp().run()
  
