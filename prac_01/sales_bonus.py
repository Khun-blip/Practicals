"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
bonus=sales*10/100
while sales<1000:
    print("If sales are under $1,000, the user gets a 10% bonus. Your bonus is ",bonus)
    break
high_bonus=sales*15/100
while sales>=1000:
    print("If sales are $1,000 or over, the bonus is 15%. Your bonus is ",high_bonus)
    break





