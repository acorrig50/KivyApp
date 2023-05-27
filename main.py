from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

# Layout class
class BoxLayout(BoxLayout):
    # Python code for adding buttons and layouts
    #   Usually only use the .kv file, but it will good to learn
    pass
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
    """

class AnchorLayout(AnchorLayout):
    pass


# The main widget
class MainWidget(Widget):
    pass

# The main class
class Application(App):
    pass
    
    
    
    
# Create an instance of my app class and run it
application = Application()
application.run()
