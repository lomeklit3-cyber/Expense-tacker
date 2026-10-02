from datetime import datetime

class UniqueExpenseTracker:
    def __init__(self, monthly_budget):
        self.monthly_budget = monthly_budget
        self.expenses = []
        # Assume 30 days for simplicity
        self.daily_baseline = monthly_budget / 30

    def get_current_status(self):
        total_spent = sum(item["amount"] for item in self.expenses)
        remaining_budget = self.monthly_budget - total_spent
        
        # Unique Concept: Calculate remaining daily spending allowance
        # Assumes day of the month based on expenses recorded so far
        days_passed = max(1, len(set(item["date"] for item in self.expenses)))
        days_remaining = max(1, 30 - days_passed)
        adjusted_daily_limit = remaining_budget / days_remaining

        return total_spent, remaining_budget, adjusted_daily_limit

    def log_expense(self, amount, note):
        today = datetime.now().strftime("%Y-%m-%d")
        self.expenses.append({"amount": amount, "note": note, "date": today})
        print(f"✓ Added ${amount:.2f} for '{note}'")

    def show_dashboard(self):
        total_spent, remaining, daily_limit = self.get_current_status()
        
        print("\n" + "═" * 40)
        print("     🎮 DAILY PACE EXPENSE TRACKER     ")
        print("═" * 40)
        print(f"💰 Total Monthly Budget : ${self.monthly_budget:.2f}")
        print(f"💸 Total Spent So Far   : ${total_spent:.2f}")
        print(f"🏦 Total Remaining      : ${remaining:.2f}")
        print("─" * 40)
        
        # Dynamic advice based on daily allowance
        if daily_limit >= self.daily_baseline:
            status = "🟢 ON TRACK"
            advice = "You're under budget! Your daily allowance has increased."
        elif daily_limit > 0:
            status = "🟡 SLOW DOWN"
            advice = "You spent a bit extra recently. Pull back slightly to recover."
        else:
            status = "🔴 BUDGET EXCEEDED"
            advice = "You have run out of monthly budget!"

        print(f"📊 Status               : {status}")
        print(f"🎯 Safe Daily Limit     : ${daily_limit:.2f} / day")
        print(f"💡 Advice               : {advice}")
        print("═" * 40)

# --- Example Usage ---
if __name__ == "__main__":
    # 1. Set your starting budget for the month
    tracker = UniqueExpenseTracker(monthly_budget=1200)

    # 2. Log a few simple expenses
    tracker.log_expense(15.50, "Morning Coffee & Pastry")
    tracker.log_expense(42.00, "Grocery Run")
    tracker.log_expense(120.00, "Concert Ticket")

    # 3. View your adjusted daily limit and dashboard
    tracker.show_dashboard()
