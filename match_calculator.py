MIN_LEVEL = 0
MAX_LEVEL = 1
CLASS_NAME = 2
LAST_CLASS_LEVEL = -1


class MatchCalculator:
    def __init__(self) -> None:
        self.winning_balance = 0
        self.__levels = [
            [0, 10, "Ferro"],
            [11, 20, "Bronze"],
            [21, 50, "Prata"],
            [51, 80, "Ouro"],
            [81, 90, "Diamante"],
            [91, 100, "Lendário"],
            [101, "_", "Imortal"],
        ]

    def calculate(self, wins_amount: int, lose_amount: int) -> str:
        winning_balance = wins_amount - lose_amount
        self.winning_balance = winning_balance

        if winning_balance >= self.__levels[LAST_CLASS_LEVEL][MIN_LEVEL]:
            return self.__levels[LAST_CLASS_LEVEL][CLASS_NAME]

        for class_level in self.__levels:
            if (
                winning_balance >= class_level[MIN_LEVEL] and
                winning_balance <= class_level[MAX_LEVEL]
            ):
                return class_level[CLASS_NAME]
