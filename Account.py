from Bank import Bank

class Account(Bank):

    def deposit(self, account_number, amount):
        if not self.check_existing_account(account_number):
            self.accounts[account_number]['Balance'] += amount
        else:
            raise ValueError("Account number doesn't exists")
        
    def wittdraw(self, account_number, amount):
        if not self.check_existing_account(account_number):
            current_balance = self.accounts[account_number]['Balance']
            if current_balance >= amount:
                self.accounts[account_number]['Balance'] -= amount
            else:
                raise ValueError("Account doesn't have sufficient balance")
        else:
            raise ValueError("Account number doesn't exists") 
        
    def check_balance(self, account_number):
        if not self.check_existing_account(account_number):
            return f"Current balance is - {self.accounts[account_number]['Balance']}"
        else:
            raise ValueError("Account number doesn't exists")