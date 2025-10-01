#!/usr/bin/env python3
import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = None
    if params and params[0] != '':
        try:
            amount = float(params[0])
        except ValueError:
            print("Invalid amount. Please provide a number.")
            sys.exit(1)

    if command == "deposit" and amount is not None:
        try:
            account.deposit(amount)
        except ValueError as e:
            print(e)
            sys.exit(1)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        try:
            success = account.withdraw(amount)
        except ValueError as e:
            print(e)
            sys.exit(1)
        if success:
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
