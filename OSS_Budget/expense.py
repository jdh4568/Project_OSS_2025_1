
class Expense:
    def __init__(self, date, category, description, amount, impulse):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount
        self.impulse = impulse

    def __str__(self):
        return f"[{self.date}] {self.category} - {self.description}: {self.amount}원 (충동구매: {self.impulse})"