from body import body
from month import month


class evaluator:
    def __init__(self, body: body, recipe: month) -> None:
        self.body = body
        self.recipe = recipe
        self.carbon = [body.get_carbon(), recipe.get_carbon()]
        self.protein = [body.get_protein(), recipe.get_protein()]
        self.fat = [body.get_fat(), recipe.get_fat()]
        self.calories = [body.get_calories(), recipe.get_calories()]
        pass

    def rate_nutrition(self, nutrition):
        return (nutrition[0] / self.body.get_weight()) - (
            nutrition[1] / self.body.get_weight()
        )

    def isEnough_nutrition(self, nutrition):
        return (
            "不足"
            if self.rate_nutrition(nutrition) > 0.2
            else "过量" if self.rate_nutrition(nutrition) < -0.2 else "合适"
        )

    def rate_calories(self, calories):
        return calories[0] - calories[1]

    def isEnough_calories(self, calories):
        return (
            "不足"
            if self.rate_calories(calories) > 300
            else "过量" if self.rate_calories(calories) < 150 else "合适"
        )

    def _print(self):
        print("*****饮食分析*****")
        print(
            f"碳水:{self.isEnough_nutrition(self.carbon)} (理论：{self.body.get_carbon()}g 实际{self.recipe.get_carbon()}g)"
        )
        print(
            f"蛋白质:{self.isEnough_nutrition(self.protein)} (理论：{self.body.get_protein()}g 实际{self.recipe.get_protein()}g)"
        )
        print(
            f"脂肪:{self.isEnough_nutrition(self.fat)} (理论：{self.body.get_fat()}g 实际{self.recipe.get_fat()}g)"
        )
        print(
            f"热量:{self.isEnough_calories(self.calories)} (上限：{self.body.get_calories()}kcal 实际{self.recipe.get_calories()}kcal)"
        )
        print("*****饮食分析*****")
