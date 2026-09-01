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
         return{
              "income":0.0,
              "expence":0.0,
              "balance":0.0,
         }