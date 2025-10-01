class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize the account with an optional initial balance."""
        self.__account_balance = float(initial_balance)

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__account_balance += amount

    def withdraw(self, amount):
        """Attempt to withdraw amount. Return True on success, False if insufficient funds."""
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            raise ValueError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def display_balance(self):
        """Print the current balance in a friendly format."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
