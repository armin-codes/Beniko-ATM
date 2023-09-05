import time
import os
import tempfile


# Beniko ATM
# written by Armin Samiani!

class ATM:
	# Stats
	def __init__(self, balance=0, interest_rate=0.01):
		self.balance = balance
		self.interest_rate = interest_rate

	# Here is deposit which will give you money!
	def deposit(self, amount):
		print("Processing deposit...")
		time.sleep(1)
		# here's the calculation.
		# v
		self.balance += amount
		# ^
		# And the report.
		print(f"\033[92mDeposit successful. Your new balance is: {self.balance:.2f}$\033[0m")

	# Withdraw that transfers your card money to cash!
	# and prints the amount of money that was transferred to cash in paper.(with printer)
	def withdraw(self, amount):
		print("Processing withdrawal...")
		time.sleep(1)
		# if you are poor , Withdraw will fail
		if amount > self.balance:
			print("\033[91mInsufficient funds.\033[0m")
		else:
			# Calculation
			self.balance -= amount
			# Default Dialog
			print(f"\033[92mWithdrawal successful. Your new balance is: {self.balance:.2f}$\033[0m")

	# Check da balance!
	def check_balance(self):
		print("Checking balance...")
		time.sleep(1)
		# Choices
		print("\nDo you want to:")
		print("1. Show the balance")
		print("2. Print the balance (definitely try it!)")
		print("3. Show and print the balance")
		choice = int(input("Enter your choice: "))
		if choice == 3:
			time.sleep(1)
			# The balance report
			print(f"""
\033[94mYour current balance is: {self.balance:.2f}$\033[0m""")
			# So here is the important part , it prints the balance on paper! be sure to connect your printer
			# Or you can just remove this part of code
			filename = tempfile.mktemp(".txt")
			open(filename, "w").write(f"""Your current balance is: {self.balance:.2f}\n""")
			os.startfile(filename, "print")

		elif choice == 2:
			time.sleep(1)
			# Here is just the default printing where you can remove too!
			filename = tempfile.mktemp(".txt")
			open(filename, "w").write(f"Your current balance is: {self.balance:.2f}\n")
			os.startfile(filename, "print")
		# And finally here is the option 1 that only reports the current balance!
		else:
			print(f"\033[94mYour current balance is: {self.balance:.2f}$\033[0m")

	# Apply interest
	def apply_interest(self):
		print("Applying interest...")
		time.sleep(1)
		# Calculations
		interest = self.balance * self.interest_rate
		self.balance += interest
		# Report
		print(f"\033[92mInterest applied. Your new balance is: {self.balance:.2f}$\033[0m")

	# Transfer money
	def transfer(self, amount, recipient):
		print("Processing transfer...")
		time.sleep(1)
		# if you are poor , transfer will fail
		if amount > self.balance:
			print("\033[91mInsufficient funds.\033[0m")
		else:
			# Calculations
			self.balance -= amount
			recipient.deposit(amount)
			# Report
			print(f"\033[92mTransfer successful. Your new balance is: {self.balance:.2f}$\033[0m")


def main():
	atm1 = ATM()
	atm2 = ATM()
	# The introduction
	while True:
		print("\n\033[1mWelcome to the Beniko's ATM!\033[0m")
		# Choose your card
		print("\033[1m1. Insert Card (Account 1)\033[0m")
		print("\033[1m2. Insert Card (Account 2)\033[0m")
		print("\033[1m3. Exit\033[0m")
		try:
			choice = int(input("Enter your choice: "))
		# if nothing entered say invalid choice. and continues
		except ValueError:
			print("\033[91mInvalid choice. Please enter a valid integer.\033[0m")
			continue
		# here are the choices effects.
		if choice == 1:
			atm = atm1
			recipient = atm2
		elif choice == 2:
			atm = atm2
			recipient = atm1
		elif choice == 3:
			break
		else:
			# if nothing in the list entered say invalid choice. and continues
			print("\033[91mInvalid choice. Please try again.\033[0m")
			continue
		# Choice menu
		while True:
			# The menu
			print("\n\033[1mBeniko ATM Menu\033[0m")
			print("\033[1m1. Deposit\033[0m")
			print("\033[1m2. Withdraw\033[0m")
			print("\033[1m3. Check Balance\033[0m")
			print("\033[1m4. Apply Interest\033[0m")
			print("\033[1m5. Transfer Funds\033[0m")
			print("\033[1m6. Exit\033[0m")
			try:
				choice = int(input("Enter your choice: "))
			# if nothing in the list entered say invalid choice. and continues
			except ValueError:
				print("\033[91mInvalid choice. Please enter a valid integer.\033[0m")
				continue
			# What you gonna do
			if choice == 1:
				amount = float(input("Enter the amount to deposit: "))
				atm.deposit(amount)
			elif choice == 2:
				amount = float(input("Enter the amount to withdraw: "))
				atm.withdraw(amount)
			elif choice == 3:
				atm.check_balance()
			elif choice == 4:
				atm.apply_interest()
			elif choice == 5:
				amount = float(input("Enter the amount to transfer: "))
				atm.transfer(amount, recipient)
			elif choice == 6:
				quit('Pull your card out')
			else:
				# if nothing in the list entered say invalid choice. and continues
				print("\033[91mInvalid choice. Please try again.\033[0m")


if __name__ == "__main__":
	main()
# if you liked this project ,
# Make sure to check my Twitter account and share your thoughts with me!
# https://twitter.com/ArminS56183
