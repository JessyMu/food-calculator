from meal import meal
from typing import List


class month:
    def get_fat(self):
        return sum(diet.get_fat() for diet in self.daily_diets)

    def get_protein(self):
        return sum(diet.get_protein() for diet in self.daily_diets)

    def get_carbon(self):
        return sum(diet.get_carbon() for diet in self.daily_diets)

    def get_calories(self):
        return sum(diet.get_calories() for diet in self.daily_diets)

    def get_price(self):
        return sum(diet.get_price() for diet in self.daily_diets)

    def __init__(self, *diets: meal) -> None:
        self.daily_diets: List[meal] = list(diets)

    def _print(self):
        print("*****本月饮食*****")
        print(f"每日碳水:{self.get_carbon()}g")
        print(f"每日蛋白质:{self.get_protein()}g")
        print(f"每日脂肪:{self.get_fat()}g")
        print(f"每日热量:{self.get_calories()}kcal")
        print(f"每日消费:{self.get_price()}元")
        print("*****本月饮食*****")
        [self._print_meal(index) for index, _ in enumerate(self.daily_diets)]

    def _print_meal(self, index):
        print(f"*****第{index+1}餐饮食*****")
        print(f"第{index+1}餐碳水:{self.daily_diets[index].get_carbon()}g")
        print(f"第{index+1}餐蛋白质:{self.daily_diets[index].get_protein()}g")
        print(f"第{index+1}餐脂肪:{self.daily_diets[index].get_fat()}g")
        print(f"第{index+1}餐热量:{self.daily_diets[index].get_calories()}kcal")
        print(f"第{index+1}餐消费:{self.daily_diets[index].get_price()}元")
        print(f"*****第{index+1}餐饮食*****")
