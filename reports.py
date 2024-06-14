from fpdf import FPDF
import os
import webbrowser

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
        pdf.image("files/house.png", w=50, h=50)
        
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
        
        os.chdir("files")
        
        pdf.output(self.filename)
        
        webbrowser.open(self.filename)