from match_calculator import MatchCalculator


if __name__ == "__main__":
    wins = int(input("Quantas vitórias seu herói teve?"))
    loses = int(input("E quantas derrotas?"))

    calculator = MatchCalculator()

    hero_level = calculator.calculate(wins, loses)
    winning_balance = calculator.winning_balance

    print(f"O Herói tem de saldo de vitórias {winning_balance} vitórias e está no nível {hero_level}") # noqa
