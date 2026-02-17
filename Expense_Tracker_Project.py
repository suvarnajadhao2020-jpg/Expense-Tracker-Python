#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
from datetime import datetime


# In[2]:


class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date


# In[3]:


def save_expense(expense):
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([expense.amount, expense.category, expense.date])


# In[4]:


def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = datetime.now().strftime("%Y-%m-%d")

    expense = Expense(amount, category, date)
    save_expense(expense)
    print("Expense added successfully!")


# In[5]:


def view_expenses():
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


# In[6]:


# Function to view expenses by month
def view_monthly_expenses():
    month = input("Enter month (MM format, e.g., 02): ")
    total = 0

    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            expense_date = row[2]  # Date column
            expense_month = expense_date.split("-")[1]

            if expense_month == month:
                print(row)
                total += float(row[0])

    print("Total spending for month:", total)


# In[9]:


while True:
    print("\n1. Add Expense")
    print("2. View All Expenses")
    print("3. View Monthly Expenses")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_monthly_expenses()
    elif choice == "4":
        break
    else:
        print("Invalid choice")


# In[ ]:


1

