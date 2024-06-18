import csv


class Account:
    def __init__(self, name, balance, monthly_input, annual_return_rate):
        self.name = name
        self.current_balance = balance
        self.monthly_input = monthly_input
        self.annual_return_rate = annual_return_rate

    def calculate_balance(self, years):
        months = years * 12
        calculated_balance = self.current_balance
        monthly_return_rate = (1 + self.annual_return_rate) ** (1 / 12) - 1

        for _ in range(months):
            calculated_balance += self.monthly_input
            calculated_balance *= 1 + monthly_return_rate

        return calculated_balance


class InvestmentCalculator:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def update_account(self, name, current_balance, monthly_input, annual_return_rate):
        for account in self.accounts:
            if account.name == name:
                account.current_balance = current_balance
                account.monthly_input = monthly_input
                account.annual_return_rate = annual_return_rate
                return True
        return False

    def list_accounts(self):
        # return [account.name for account in self.accounts]
        return [
            (
                f"{account.name} with a current balance of £{account.current_balance:.2f} "
                f"and £{account.monthly_input:.2f} added monthly with an AAR of {account.annual_return_rate:.2%}"
            )
            for account in self.accounts
        ]

    def calculate_total_balance(self, years):
        total_balance = 0

        for account in self.accounts:
            total_balance += account.calculate_balance(years)

        return total_balance

    def save_to_file(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["name", "current_balance", "monthly_input", "annual_return_rate"]
            )
            for account in self.accounts:
                writer.writerow(
                    [
                        account.name,
                        account.current_balance,
                        account.monthly_input,
                        account.annual_return_rate,
                    ]
                )

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                account = Account(
                    row["name"],
                    float(row["current_balance"]),
                    float(row["monthly_input"]),
                    float(row["annual_return_rate"]),
                )
                self.add_account(account)


def main():
    calculator = InvestmentCalculator()

    while True:
        action = input(
            "Enter 'add' to add an account, 'save' to save accounts, 'load' to load accounts, or 'done' to finish: "
        ).lower()

        if action.lower() == "done":
            break
        elif action == "add":
            name = input("Enter the name of the account: ")
            current_balance = float(input(f"Enter current balance for {name}: "))
            monthly_input = float(input(f"Enter monthly input for {name}: "))
            annual_return_rate = float(
                input(f"Enter annual return rate (as a decimal for {name}: ")
            )

            account = Account(name, current_balance, monthly_input, annual_return_rate)
            calculator.add_account(account)
        elif action == "update":
            accounts = calculator.list_accounts()
            print(accounts)
            if not accounts:
                print("No accounts to update.")
                continue
            print("Existing accounts:")
            for i, account_info in enumerate(accounts, start=1):
                print(f"{i}. {account_info}")
            choice = int(input("Enter the number of the account you want to update: "))
            account_to_update = calculator.accounts[choice - 1]
            name = account_to_update.name
            current_balance = float(
                input(f"Enter updated current balance for {name}: ")
            )
            monthly_input = float(input(f"Enter updated monthly input for {name}: "))
            annual_return_rate = float(
                input(f"Enter updated annual return rate (as a decimal for {name}: ")
            )

        elif action == "save":
            accounts = "data\processed\investment_accounts.csv"
            calculator.save_to_file(accounts)
            print("Accounts saved")
        elif action == "load":
            accounts = "data\processed\investment_accounts.csv"
            calculator.load_from_file(accounts)
            print("Accounts loaded")
        else:
            print("That action is invalid. Please try again.")
    years = int(input("Enter the number of years you plan to keep this investment: "))
    total_calculated_balance = calculator.calculate_total_balance(years)
    print(
        f"Your total predicted balance after {years} years is: £{total_calculated_balance:.2f}"
    )


if __name__ == "__main__":
    main()
