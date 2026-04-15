from Account import Account

accIns = Account()


account_number = 123456789
account_holder_details = {'Name':'Rohan', 'Age':25, 'Gender': 'Male', 'Balance': 10000}
print(accIns.open_account(account_number, account_holder_details))

account_number = 123456788
account_holder_details = {'Name':'Sohan', 'Age':25, 'Gender': 'Male', 'Balance': 5000}
print(accIns.open_account(account_number, account_holder_details))
print(accIns.accounts)

accIns.deposit(123456788, 10000)
print(accIns.check_balance(123456788))