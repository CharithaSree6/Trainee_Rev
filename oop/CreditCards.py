from BankDetails import BankDetails

class CreditCards(BankDetails):
    def __init__(self, custid, cname, bal, creaditscore,status):
        super().__init__(custid, cname, bal)
        self.creditscore = creaditscore
        self.status = status

    def welcome_message(self):
        print(f'welcome to SBI,{self.cname}')

    def display_cc_details(self):
        print(f'{self.creditscore} - {self.status}')
