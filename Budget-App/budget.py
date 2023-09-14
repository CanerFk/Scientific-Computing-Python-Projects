class Category:
    def __init__(self, category):
        self.category = category
        self.ledger =[]

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount":amount, "description":description})
    
    def get_balance(self):
        return sum(float(item["amount"]) for item in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount,"description":description})
            return True
        return False
    
    def transfer(self, amount, budgetCategory):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budgetCategory.category}")
            budgetCategory.deposit(amount, f"Transfer from {self.category}")
            return True
        return False
       
    def __str__(self):
        output = f"{self.category.center(30, '*')}\n"
        output += "\n".join(f"{item['description'][:23]:23}{item['amount']:7.2f}" for item in self.ledger)
        output += f"\nTotal: {self.get_balance():.2f}"
        return output

def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spent = [(c.category, sum(item['amount'] for item in c.ledger if item['amount'] < 0)) for c in categories]
    spentTotal = sum(spent_item[1] for spent_item in spent)
    spentPercentages = [(cat, (spent / spentTotal) * 100) for cat, spent in spent]

    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for spentCategory, spent_percentage in spentPercentages:
            if spent_percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(c.category) for c in categories)
    for i in range(max_len):
        chart += "     "
        for cat in categories:
            if i < len(cat.category):
                chart += cat.category[i] + "  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"

    return chart

