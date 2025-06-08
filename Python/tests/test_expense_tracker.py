import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from ExpenseTracker import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = ExpenseTracker()
        # Add some initial expenses
        self.tracker.add_expense("2025-05-20", 45.90, "Groceries", "Fruits and veggies")
        self.tracker.add_expense("2025-05-21", 10.00, "Transportation", "Bus fare")
        self.tracker.add_expense("2025-05-22", 25.50, "Dining Out", "Lunch with friends")
        self.tracker.add_expense("2025-05-23", 100.00, "Shopping", "Clothes")
        self.tracker.add_expense("2025-05-24", 15.00, "Groceries", "Snacks")
        self.tracker.add_expense("2025-05-25", 0.00, "Misc", "Free sample")

    def test_add_expense_valid(self):
        result = self.tracker.add_expense("2025-06-01", 20.00, "Books", "Python book")
        self.assertTrue(result)
        self.assertEqual(len(self.tracker.expenses), 7)

    def test_add_expense_invalid_date(self):
        result = self.tracker.add_expense("2025-13-01", 20.00, "Books", "Invalid date")
        self.assertFalse(result)
        self.assertEqual(len(self.tracker.expenses), 6)

    def test_add_expense_negative_amount(self):
        # Should allow negative (refunds), but let's check
        result = self.tracker.add_expense("2025-06-02", -5.00, "Refund", "Returned item")
        self.assertTrue(result)
        self.assertEqual(self.tracker.expenses[-1]['amount'], -5.00)

    def test_filter_by_category(self):
        groceries = self.tracker.filter_expenses(category="Groceries")
        self.assertEqual(len(groceries), 2)
        for exp in groceries:
            self.assertEqual(exp['category'], "Groceries")

    def test_filter_by_date_range(self):
        filtered = self.tracker.filter_expenses(start_date="2025-05-21", end_date="2025-05-23")
        self.assertEqual(len(filtered), 3)
        self.assertTrue(all("2025-05-21" <= exp['date'].strftime("%Y-%m-%d") <= "2025-05-23" for exp in filtered))

    def test_filter_by_category_and_date(self):
        filtered = self.tracker.filter_expenses(start_date="2025-05-20", end_date="2025-05-24", category="Groceries")
        self.assertEqual(len(filtered), 2)

    def test_summary(self):
        summary = self.tracker.get_summary()
        self.assertAlmostEqual(summary['categories']['Groceries'], 60.90)
        self.assertAlmostEqual(summary['total'], 196.40)

    def test_empty_tracker(self):
        empty = ExpenseTracker()
        self.assertEqual(empty.get_summary()['total'], 0.0)
        self.assertEqual(empty.filter_expenses(), [])

if __name__ == "__main__":
    unittest.main()
