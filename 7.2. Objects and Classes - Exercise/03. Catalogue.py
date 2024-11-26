class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, letter):
        first_letter_list = [product for product in self.products if product.startswith(letter)]
        return first_letter_list

    def __repr__(self):
        items = f"Items in the {self.name} catalogue:\n"
        items += "\n".join(sorted(self.products))
        return items


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")

print(catalogue.get_by_letter("C"))
print(catalogue)
