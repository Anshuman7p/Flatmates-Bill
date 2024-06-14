from flat import Bill, Flatmate
from reports import PdfReport 

    
amount = float(input("Enter your bill amount here:"))
period = input("Enter the Month of your Bill (ex: April 2024):")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill period? "))

name2 = input("What is the name of your First Flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))

name3 = input("What is the name of your Second Flatmate? ")
days_in_house3 = int(input(f"How many days did {name3} stay in the house during the bill period? "))

    
the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)
flatmate3 = Flatmate(name3, days_in_house3)

print(f"{flatmate1.name} pays: ",flatmate1.pays(the_bill, flatmate2, flatmate3))
print(f"{flatmate2.name} pays: ",flatmate2.pays(the_bill, flatmate1, flatmate3))
print(f"{flatmate3.name} pays: ",flatmate3.pays(the_bill, flatmate1, flatmate2))

pdf_report= PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generator(flatmate1, flatmate2, flatmate3, the_bill)