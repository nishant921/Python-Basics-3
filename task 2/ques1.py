#Problem 1: Write a program that will give you in hand monthly CTC after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
# CTC(Lakhs) : Tax(%)
# Below 5 : 0%
# 5-10 : 10%
# 10-20 : 20%
# aboove 20 : 30%

#CTC (cost to company- package a company give in one year)
# HRA (House Rent Allowance)
# DA (Dearness Allowance)
# PF (Provident Fund)


CTC=float(input("Enter Your Anual CTC : "))

HRA=CTC*(10/100)
DA=CTC*(5/100)
PF=CTC*(3/100)

if CTC<500000:
    tax=0

elif CTC>=500000 and CTC<1000000:
    tax=CTC*(10/100)

elif CTC>=1000000 and CTC<2000000:
    tax=CTC*(20/100)

else:
    tax=CTC*(30/100)

IN_hand_ctc=CTC-HRA-DA-PF-tax
monthly_salary=IN_hand_ctc/12
print("YOUR IN HAND CTC : ",IN_hand_ctc)
print("YOUR IN HAND Monthly Salary : ",monthly_salary)