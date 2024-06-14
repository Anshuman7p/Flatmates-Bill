from fpdf import FPDF
import webbrowser

class Bill:
    
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period
        
class Flatmate:
    
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
        
    def pays(self, bill, flatmate2, flatamte3):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house + flatamte3.days_in_house)
        to_pay = bill.amount * weight
        return to_pay
    

class PdfReport:
    
    def __init__(self, filename):
        self.filename = filename
        
    def generator(self, flatmate1, flatmate2, flatmate3, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2, flatmate3), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1, flatmate3), 2))
        flatmate3_pay = str(round(flatmate3.pays(bill, flatmate1, flatmate2), 2))
        
        pdf = FPDF(orientation='portrait', unit='pt', format='A4')
        pdf.add_page()
        
        #add image
        pdf.image("house.png", w=50, h=50)
        
        #insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align="C" , ln=1)
        #insert pdf label and value
        pdf.set_font(family='Times', style='B', size=18)
        pdf.cell(w=300, h=40, txt='Month :', border=0, align="C")
        pdf.cell(w=250, h=40, txt=bill.period, border=0, align="C", ln=1)
        #insert name of first flatmate and his due amount
        pdf.set_font(family='Times', size=16)
        pdf.cell(w=300, h=25, txt=flatmate1.name, border=0, align="C")
        pdf.cell(w=250, h=25, txt=flatmate1_pay, border=0, align="C", ln=1)
        #insert name of second flatmate and his due amount
        pdf.set_font(family='Times', size=16)
        pdf.cell(w=300, h=25, txt=flatmate2.name, border=0, align="C")
        pdf.cell(w=250, h=25, txt=flatmate2_pay, border=0, align="C", ln=1)
        #insert name of third flatmate and his due amount
        pdf.set_font(family='Times', size=16)
        pdf.cell(w=300, h=25, txt=flatmate3.name, border=0, align="C")
        pdf.cell(w=250, h=25, txt=flatmate3_pay, border=0, align="C", ln=1)
        
        pdf.output(self.filename)
        
        webbrowser.open(self.filename)
    
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