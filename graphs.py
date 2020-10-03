import matplotlib.pyplot as plt
import numpy as np
import csv

incomes = []
loans = []

with open('finance_data_2019.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        incomes.append(float(row['income']) * 1000.)
        loans.append(float(row['loan_amount']))

par = np.polyfit(incomes, loans, 1, full=True)
slope = par[0][0]
intercept = par[0][1]

xl = [min(incomes), max(incomes)]
yl = [slope*xx + intercept for xx in xl]

plt.scatter(incomes, loans)
plt.plot(xl, yl, '-r')

plt.title("Loan Amount vs. Income in 2019")
plt.xlabel("Income ($)")
plt.ylabel("Loan Amount ($)")
plt.show()
