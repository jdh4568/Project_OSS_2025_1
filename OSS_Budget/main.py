import tkinter as tk
from tkinter import messagebox
from budget import Budget

class BudgetApp:
    def __init__(self, root):
        self.budget = Budget()
        self.root = root
        self.root.title("간단 가계부")

        tk.Label(root, text="카테고리:").grid(row=0, column=0)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=0, column=1)

        tk.Label(root, text="설명:").grid(row=1, column=0)
        self.desc_entry = tk.Entry(root)
        self.desc_entry.grid(row=1, column=1)


        tk.Label(root, text="금액(원):").grid(row=2, column=0)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=2, column=1)


        tk.Button(root, text="지출 추가", command=self.add_expense).grid(row=3, column=0, columnspan=2, pady=5)


        self.listbox = tk.Listbox(root, width=50)
        self.listbox.grid(row=4, column=0, columnspan=2)


        tk.Button(root, text="총 지출 보기", command=self.show_total).grid(row=5, column=0, columnspan=2, pady=5)

    def add_expense(self):
        category = self.category_entry.get()
        desc = self.desc_entry.get()
        try:
            amount = int(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("입력 오류", "금액은 숫자여야 합니다.")
            return

        self.budget.add_expense(category, desc, amount)
        self.update_list()

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for i, e in enumerate(self.budget.expenses, 1):
            self.listbox.insert(tk.END, f"{i}. {e}")

    def show_total(self):
        total = sum(e.amount for e in self.budget.expenses)
        messagebox.showinfo("총 지출", f"총 지출: {total}원")


if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()
