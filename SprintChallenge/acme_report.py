# Part 4 - Class Report
from random import sample, randint, uniform
from typing import List, Any, Union

from acme import Product

adjectives = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
nouns = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


class Report(Product):

    def __init__(self, num_product=None, products=None, products_set=None):
        super().__init__()

        self.num_product = num_product
        self.products = products
        self.products_set = products_set

    def generate_products(self, num_product=30):
        """Randomly generates total number of unique products"""
        self.products = [' '.join(sample(adjectives, 1) + sample(nouns, 1))
                         for _ in range(num_product)]
        self.products_set = set(self.products)
        self.products = len(self.products_set)

        print("Unique product names:", self.products)

        return

    def inventory_report(self, products):

        avg_price = self.price / products
        print('Average price:', avg_price)

        avg_weight = self.weight / products
        print('Average weight:', avg_weight)

        avg_flammability = self.flammability / products
        print('Average flammability:', avg_flammability)

        return
    pass

    if __name__ == "__main__":
        inventory_report(generate_products())
