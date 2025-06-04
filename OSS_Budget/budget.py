import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.game_limit = None

    def set_game_limit(self, amount):
            self.game_limit = amount
            print(f"게임 과금 한도가 {amount}원으로 설정되었습니다.\n")

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")
        if category == "게임 과금":
            game_total = sum(e.amount for e in self.expenses if e.category == "게임 과금")
            if self.game_limit is not None and game_total > self.game_limit:
                print("!게임 과금 한도를 초과했습니다!")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

