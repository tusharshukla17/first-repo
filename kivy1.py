from kivy.metrics import dp
from kivy.uix.pagelayout import PageLayout
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import  BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView


class StackLayoutEx(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(100):
            b = Button(text=str(i+1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)
        

class mainWidget(Widget):
    pass


class GridLayoutEx(GridLayout):
    pass


class AnchorLayoutEx(AnchorLayout):
    pass


class firstProgram(App):
    pass


class ScrollViewEx(ScrollView):
    pass


class BoxLayoutEx(BoxLayout):
    pass
    
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text = "One")
        b2 = Button(text = "Two")
        self.add_widget(b1)
        self.add_widget(b2)
    """



firstProgram().run()

