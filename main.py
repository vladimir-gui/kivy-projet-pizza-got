from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import *
from models import Pizza


class PizzaWidget(BoxLayout):
    nom = StringProperty()
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarienne = BooleanProperty()


class MainWidget(BoxLayout):
    recycleView = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pizzas = [
            Pizza("4 fromages", "chèvre, emmental", 9.5, True),
            Pizza("Chorizo", "chorizo, tomate", 9.5, False),
            Pizza("Calzone", "fromage, champignon", 9.5, False)
        ]

    def on_parent(self, widget, parent):
        self.recycleView.data = [pizza.recuperer_dictionnaire_pizzas() for pizza in self.pizzas]


class PizzaApp(App):
    pass


PizzaApp().run()


