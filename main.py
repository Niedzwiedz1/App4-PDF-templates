from fpdf import FPDF
import pandas as pd


df = pd.read_csv("topics.csv")


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    topic = row["Topic"]
    pages = row["Pages"]
    pdf.add_page()

# Set header style
    pdf.set_font(family="Times", style="B", size=15)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=topic, align="L", ln=1)
    pdf.line(10, 19, 200, 19)

# Set footer style
    pdf.ln(265)
    pdf.set_font(family="Times", style="B", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=topic, align="R")
    for i in range(pages-1):
        pdf.add_page()

# Set footer style
        pdf.ln(275)
        pdf.set_font(family="Times", style="B", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=topic, align="R")


pdf.output("output.pdf")
