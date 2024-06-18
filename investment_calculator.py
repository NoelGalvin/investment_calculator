class Account:
    def __init__(self, name, balance, monthly_input, annual_return_rate):
        self.name = name
        self.balance = balance
        self.monthly_input = monthly_input
        self.annual_return_rate = annual_return_rate

    def predict_balance(self, years):
        months = years * 12
        predicted_balance = self.balance
        monthly_return_rate = (1 + self.annual_return_rate) ** (1 / 12) - 1

        for _ in range(months):
            predicted_balance += self.monthly_input
            predicted_balance *= 1 + monthly_return_rate

        return predicted_balance


class InvestmentCalculator:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def predict_total_balance(self, years):
        total_balance = 0

        for account in self.accounts:
            total_balance += account.predict_balance(years)

        return total_balance


def main():
    calculator = InvestmentCalculator()

    while True:
        name = input("Enter account name (or 'done' to finish): ")
        if name.lower() == "done":
            break
        balance = float(input(f"Enter current balance for {name}: "))
        monthly_input = float(input(f"Enter monthly input for {name}: "))
        annual_return_rate = float(
            input(f"Enter annual return rate (as a decimal for {name}: ")
        )

        account = Account(name, balance, monthly_input, annual_return_rate)
        calculator.add_account(account)

    years = int(input("Enter the number of years you plan to keep this investment: "))
    total_predicted_balance = calculator.predict_total_balance(years)
    print(
        f"Your total predicted balance after {years} years is: £{total_predicted_balance:.2f}"
    )


if __name__ == "__main__":
    main()
