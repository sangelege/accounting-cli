class Transaction:
    def __init__(self,record_type,amount,note=""):
        if record_type not in ("收入","支出"):
                raise ValueError("类型必须为收入和支出")

        amount =float(amount)
        if amount<=0:
             raise ValueError("金额必须大于0")

        self.type = record_type
        self.amount = float(amount)
        self.note = note

class Ledger :
    def __init__(self):
          self.transactions =[]
    def add(self, transaction):
        self.transactions.append(transaction)

    def list(self):
        return self.transactions.copy()

    def summary(self):
        income = 0.0
        expense = 0.0

        for transaction in self.transactions:
            if transaction.type == "收入":
                income += transaction.amount
            elif transaction.type == "支出":
                expense += transaction.amount

        return {
            "income": income,
            "expense": expense,
            "balance": income - expense,
        }

