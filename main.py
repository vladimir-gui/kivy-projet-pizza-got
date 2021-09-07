from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ObjectProperty
from kivy.uix.widget import Widget
from Data import HttpClient
from models import Pizza
from kivy.uix.behaviors import CoverBehavior
from kivy.uix.floatlayout import FloatLayout

from storage_manager import StorageManager


class PizzaWidget(BoxLayout):
    nom = StringProperty()
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarienne = BooleanProperty()


class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    error_str = StringProperty("")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ---- V1 data en dur
        # self.pizzas = [
        #     Pizza("4 fromages", "chèvre, emmental", 9.5, True),
        #     Pizza("Chorizo", "chorizo, tomate", 9.5, False),
        #     Pizza("Calzone", "fromage, champignon", 9.5, False)
        # ]
        HttpClient().get_pizzas(self.on_server_data, self.on_server_error)

    def on_parent(self, widget, parent):
        pizzas_dict = StorageManager().load_data("pizzas")
        # self.recycleView.data = [pizza.recuperer_dictionnaire_pizzas() for pizza in self.pizzas]
        if pizzas_dict:
            self.recycleView.data = pizzas_dict

    def on_server_data(self, pizzas_dictionnaire):
        self.recycleView.data = pizzas_dictionnaire
        StorageManager().save_data("pizzas", pizzas_dictionnaire)

    def on_server_error(self, error):
        print("erreur" + error)
        self.error_str = "ERREUR : " + error





    # def on_parent(self, widget, parent):
    #     self.recycleView.data = [pizza.recuperer_dictionnaire_pizzas() for pizza in self.pizzas]




class PizzaApp(App):
    pass


PizzaApp().run()


