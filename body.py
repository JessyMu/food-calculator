class body:
    def __init__(self, age, height, weight, distribution, addition=0) -> None:
        self.age = age
        self.height = height
        self.weight = weight
        self.carbon_rate, self.protein_rate, self.fat_rate = distribution
        self.addition = addition
        pass

    def get_weight(self):
        return self.weight

    def get_calories(self):
        # 66+(13.7× 体重(kg))+(5×身高(cm)) – (6.8×年龄(岁))
        self.calories = (
            66
            + (13.7 * self.weight)
            + (5 * self.height)
            - (6.8 * self.age)
            + self.addition
        )
        return self.calories

    def get_carbon(self):
        return self.weight * self.carbon_rate

    def get_protein(self):
        return self.weight * self.protein_rate

    def get_fat(self):
        return self.weight * self.fat_rate

    def _print(self):
        print("*****饮食计划*****")
        print(f"碳水:{self.get_carbon()}g")
        print(f"蛋白质:{self.get_protein()}g")
        print(f"脂肪:{self.get_fat()}g")
        print(f"热量:{self.get_calories()}kcal")
        print("*****饮食计划*****")
