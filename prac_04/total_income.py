"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def main():
    """Display earnings report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        earnings = float(input("Enter earnings for month " + str(month) + ": "))
        incomes.append(earnings)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        earnings = incomes[month - 1]
        total += earnings
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, earnings, total))

main()