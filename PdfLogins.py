import os
import webbrowser
from fpdf import FPDF

class PDFsavedLogins:
    def __init__(self):
        pass

    def generate(self, user_logins_info):
        pdf = FPDF(orientation="P", unit='pt', format='A4')
        pdf.add_page()

        #Title
        pdf.set_font(family='Times', size=24, style="B")
        pdf.cell(w=400, h=40, txt="Saved Logins", border=0, align="C", ln=1)

        pdf.set_font(family='Times', size=18, style="B")
        pdf.cell(w=50, h=40, txt="TYPE", border=0, align="C")
        pdf.cell(w=150, h=40, txt="USERNAME", border=0, align="C")
        pdf.cell(w=150, h=40, txt="PASSWORD", border=0, align="C", ln=1)

        # Convert List to a string
        for i in user_logins_info:
            string = ''
            for element in i:
                string = string + "                " + element
            pdf.cell(w=250, h=40, txt=string, border=0, align="C", ln=1)

        pdf.output('Saved pdf/result1.pdf')

