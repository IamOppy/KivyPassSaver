import os
import webbrowser
from fpdf import FPDF

class PDFsavedLogins:
    def __init__(self):
        pass

    def generate(self):
        pdf = FPDF(orientation="P", unit='pt', format='A4')
        pdf.add_page()

        #Title
        pdf.set_font(family='Times', size=24, style="B")
        pdf.cell(w=400, h=40, txt="Saved Logins", border=0, align="C", ln=1)



        pdf.output('Saved pdf/result1.pdf')

obj = PDFsavedLogins()
obj.generate()