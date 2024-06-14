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
        pdf.cell(w=300, h=40, txt='Month- :', border=0, align="C")
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
    
    
    
the_bill = Bill(amount= 1500, period= 'May 2024')
rohit = Flatmate(name='Rohit', days_in_house= 12)
ruzul = Flatmate(name='Ruzul', days_in_house=25)
anshuman = Flatmate(name= 'Anshuman', days_in_house=31)

print("Rohit pays: ",rohit.pays(bill=the_bill, flatmate2=ruzul, flatamte3=anshuman))
print("Ruzul pays: ",ruzul.pays(bill=the_bill, flatmate2=rohit, flatamte3=anshuman))
print("Anshuman pays: ",anshuman.pays(bill=the_bill, flatmate2=rohit, flatamte3=ruzul))

pdf_report= PdfReport(filename='May2024Bill.pdf')
pdf_report.generator(flatmate1=rohit, flatmate2=ruzul, flatmate3=anshuman, bill=the_bill)