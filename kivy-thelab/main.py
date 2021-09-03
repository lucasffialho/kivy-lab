from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):
    counter = 1
    my_text = StringProperty("1")
    count_enabled = BooleanProperty(False)
    #slider_value_txt = StringProperty("50")
    text_input_str = StringProperty("nada")

    def on_button_click(self):
        print("Button Clicked")
        if self.count_enabled:
            self.counter += 1
            self.my_text = str(self.counter)

    def on_toggle_button_state(self, widget):
        print("toggle state: " + widget.state)
        if widget.state == "normal":
             widget.text = "Liga"
             self.count_enabled = False

        else:
            widget.text = "Desliga"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch:" + str(widget.active))

    def on_text_validate(self,widget):
        self.text_input_str = widget.text


    # def on_slider_value(self, widget):
       # print(str(int(widget.value)))
        #self.slider_value_txt = str(int(widget.value))

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        for i in range(0, 100):
            #size = dp(100) + i*10
            b = Button(text=str(i + 1), size_hint=(None, None), size=(dp(100), dp(100)))  # é i+1 pra nao começar em zero
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
# pass

class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
    """"def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
    """""


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()
