
class User:
    def __init__(self,userID,name,email,mobilenumber):
        self.userID=userID
        self.name=name
        self.email=email
        self.mobilenumber=mobilenumber

class Expenses:
    def __init__(self,expensesID,userID,amount,expensetype,participate,share=None):
        self.expensesID=expensesID
        self.userID=userID
        self.amount=amount
        self.expensetype=expensetype
        self.participate=participate
        self.share=share

class ExpensesManger:
    expenses=[]

    def addExpense(self,expense):
        self.expenses.append(expense)

    def getExpensesForUser(self,userID):
        return [expense for expense in self.expenses if userID in expense.participate]
    
    def simplyexpense(self):
        pass

class BalanceManager:
    balances={}

    def updateBalances(self,payer,payee,amount):
        if payer in self.balances:
            self.balances[payer] -= amount

        else:
            self.balances[payer] = -amount

        if payee in self.balances:
            self.balances[payee] += amount

        else:
            self.balances[payee] = amount

    def getBalancesForUser(self,userID):
        return {user: balance for user,balance in self.balances.items() if balance !=0 and user==userID}
    
user1=User('u1','User1','user1@example.com','123456789')
user2=User('u2','User2','user2@example.com','123456789')
user3=User('u3','User3','user3@example.com','123456789')

expenseManager=ExpensesManger()
balanceManager=BalanceManager()

expense1= Expenses('e1','u1',1000,'EQUAL',['u1','u2','u3','u4'])
expenseManager.addExpense(expense1)

for participate in expense1.participate:
    if participate != 'u1':
        balanceManager.updateBalances('u1', participate, expense1.amount / (len(expense1.participate) - 1))

expense2 = Expenses('e2', 'u1', 1250, 'EXACT', ['u1', 'u2', 'u3'], {'u2': 370, 'u3': 880})
expenseManager.addExpense(expense2)

for participate, amount in expense2.share.items():
    balanceManager.updateBalances('u1', participate, amount)

expense3 = Expenses('e3', 'u4', 1200, 'PERCENT', ['u1', 'u2', 'u3', 'u4'], {'u1': 40, 'u2': 20, 'u3': 20, 'u4': 20})
expenseManager.addExpense(expense3)

for participate, percent in expense3.share.items():
    balanceManager.updateBalances(participate, 'u4', (expense3.amount * percent) / 100)

print(balanceManager.getBalancesForUser('u1'))
print(balanceManager.getBalancesForUser('u2'))
print(balanceManager.getBalancesForUser('u3'))
print(balanceManager.getBalancesForUser('u4'))
