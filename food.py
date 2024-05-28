"""
- 早餐：30g燕麦+50g蛋白饭
- 中餐：200g米饭+1荤
- 后餐：2香蕉+200g牛肉

碳水：180g
蛋白质：100g

- 早餐：30g燕麦+50g蛋白粉
- 中餐：100g米饭+2素+1荤
- 前餐：30g燕麦+50g蛋白粉+加餐
- 后餐：2香蕉+200g牛肉/鸡肉+1肌酸

碳水：150g
蛋白质：120g
"""

from price import price


class food:
    def __init__(self, weight=0) -> None:
        self.weight = weight / 100

    def get(self):
        return (
            self.weight * self.carbon,
            self.weight * self.protein,
            self.weight * self.fat,
            self.weight * self.calories,
            self.weight * self.price,
        )


class nut(food):
    carbon = 0  # 20.3
    protein = 0  # 16.3
    fat = 64.4  # 59.8
    calories = 2929  # 2835
    price = price(52.5, 1100).get_value()  # 62.5元1.1kg

    def __init__(self, weight=0) -> None:
        super().__init__(weight)


class protein_on(food):
    carbon = 0  # 9.9
    protein = 78.9
    fat = 0  # 2.3
    calories = 1595
    price = price(478, 2270).get_value()  # 518元2270g

    def __init__(self, weight=0) -> None:
        super().__init__(weight)


class protein_powerbuff(food):
    carbon = 0  # 9.3
    protein = 80
    fat = 0  # 2
    calories = 1593
    price = price(329, 2270).get_value()  # 518元2270g

    def __init__(self, weight=0) -> None:
        super().__init__(weight)


class oat(food):
    carbon = 65
    protein = 0  # 12
    fat = 0  # 8
    calories = 1701
    price = price(13, 2000).get_value()  # 16元1380g

    def __init__(self, weight=0) -> None:
        super().__init__(weight)


class beef_hm(food):
    carbon = 0  # 1.2
    protein = 23.8
    fat = 5.6
    calories = 632
    price = price(52.8, 500).get_value()

    def __init__(self, weight=0) -> None:
        super().__init__(weight)


class sauce(food):
    carbon = 11.6
    protein = 2.1
    fat = 0
    calories = 233
    price = price(24, 800).get_value()

    def __init__(self, weight=0) -> None:
        super().__init__(weight)


class rice(food):
    carbon = 25.9
    protein = 0  # 2.6
    fat = 0  # 0.3
    calories = 486
    price = 0.5

    def __init__(self, weight=0) -> None:
        super().__init__(weight)

    def get(self):
        return (
            self.weight * self.carbon,
            self.weight * self.protein,
            self.weight * self.fat,
            self.weight * self.calories,
            self.price,
        )


class banana(food):
    # 每个
    carbon = 24
    protein = 0  # 1.3
    fat = 0  # 0.3
    calories = 377
    price = price(27.5, 21 * 65).get_value()

    def __init__(self, weight=0) -> None:
        super().__init__(weight * 65)


class oil(food):
    carbon = 0
    protein = 0
    fat = 100
    calories = 3700
    price = price(95, 2700).get_value()

    def __init__(self, weight=0) -> None:
        super().__init__(weight)


class jisuan(food):
    carbon = 0
    protein = 0
    fat = 0
    calories = 0
    price = price(59, 360).get_value()

    def __init__(self, weight=0) -> None:
        super().__init__(weight)


class tomato(food):
    carbon = 0
    protein = 0
    fat = 0
    calories = 0
    price = price(30, 4.5 * 500).get_value()

    def __init__(self, weight=0) -> None:
        super().__init__(weight)


class egg(food):
    # 每个：
    carbon = 0
    protein = 3.5
    fat = 0
    calories = 0
    price = price(16.5, 30).get_value()

    def __init__(self, weight=0) -> None:
        super().__init__(weight)


# TODO: 补充数据
class vegetable(food):
    carbon = 0
    protein = 0
    fat = 0
    calories = 53
    price = price(8.8, 200).get_value()

    def __init__(self, weight=0) -> None:
        super().__init__(weight)


class chicken(food):
    carbon = 9.1
    protein = 16.7
    fat = 1.4
    calories = 490

    def __init__(self, weight=0) -> None:
        super().__init__(weight)


class blueberry(food):
    carbon = 0
    protein = 0
    fat = 0
    calories = 53

    def __init__(self, weight=0) -> None:
        super().__init__(weight)


class cucumber(food):
    carbon = 0
    protein = 0
    fat = 0
    calories = 53

    def __init__(self, weight=0) -> None:
        super().__init__(weight)


class avocado(food):  # 牛油果
    carbon = 0
    protein = 0
    fat = 0
    calories = 53

    def __init__(self, weight=0) -> None:
        super().__init__(weight)


class corn(food):  # 玉米
    carbon = 0
    protein = 0
    fat = 0
    calories = 53

    def __init__(self, weight=0) -> None:
        super().__init__(weight)


class beef_jd(food):
    carbon = 0
    protein = 0
    fat = 0
    calories = 53

    def __init__(self, weight=0) -> None:
        super().__init__(weight)
