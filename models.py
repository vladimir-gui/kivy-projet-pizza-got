
class Pizza:
    nom = ""
    ingredients = ""
    prix = 0.0
    vegetarienne = False

    def __init__(self, nom, ingredients, prix, vegetarienne):
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix
        self.vegetarienne = vegetarienne


    def recuperer_dictionnaire_pizzas(self):
        dictionnaire_pizzas = {"nom":self.nom, "ingredients":self.ingredients,
        "prix":self.prix, "vegetarienne": self.vegetarienne}
        return dictionnaire_pizzas
