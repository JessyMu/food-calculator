from food import food
from typing import List


class meal:
    fat = 0
    carbon = 0
    protein = 0
    calories = 0
    price = 0

    def __init__(self, *foods: food) -> None:
        self.foods: List[food] = list(foods)
        for nutrition in self.foods:
            carbon, protein, fat, calories, price = nutrition.get()
            self.carbon += carbon
            self.protein += protein
            self.fat += fat
            self.calories += calories
            self.price += price
        self.calories = self.calories / 4.186

    def get_fat(self):
        return self.fat

    def get_protein(self):
        return self.protein

    def get_carbon(self):
        return self.carbon

    def get_calories(self):
        return self.calories

    def get_price(self):
        return self.price

    def _print(self):
        print("*****本餐饮食*****")
        print(f"每餐碳水:{self.get_carbon()}g")
        print(f"每餐蛋白质:{self.get_protein()}g")
        print(f"每餐脂肪:{self.get_fat()}g")
        print(f"每餐热量:{self.get_calories()}kcal")
        print(f"每餐花费:{self.get_price()}元")
        print("*****本餐饮食*****")


class breakfast(meal):
    def __init__(self, **food: food) -> None:
        super().__init__(**food)


class launch(meal):
    def __init__(self, **food: food) -> None:
        super().__init__(**food)


class before(meal):
    def __init__(self, **food: food) -> None:
        super().__init__(**food)


class after(meal):
    def __init__(self, **food: food) -> None:
        super().__init__(**food)
