class Bank:

    def __init__(self):
        self.accounts = {}

    def open_account(self, account_number, account_holder_details):
        """
        opens account of user
        Parameters:
            account_number : 9 digit number
            account_holder_details : {'Name': 'Rohan', 'Age' : 35, 'Gender': 'Male', 'Balance': 5000}
        """

        # open account
        if self.check_existing_account(account_number):
            self.accounts[account_number] = account_holder_details
            return f"Account open for {account_holder_details['Name']} - {account_number}"
        else:
            raise ValueError(f"The account number {account_number} already exists")
    
    def check_existing_account(self, account_number):
        account_list = list(self.accounts.keys())
        status = True
        if account_number in account_list:
            status = False
        return status
    
    def delete_account(self, account_number):
        if not self.check_existing_account(account_number):
            self.accounts.pop(account_number)
        else:
            raise ValueError("The account doesn't exists")
