class price:
    def __init__(self, cost, weight) -> None:
        self.value = cost / weight * 100

    def get_value(self):
        return self.value
