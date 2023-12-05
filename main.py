from fpdf import FPDF
import pandas as pd


df = pd.read_csv("topics.csv")


pdf = FPDF(orientation="P", unit="mm", format="A4")

for index, row in df.iterrows():
    topic = row["Topic"]
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=15)
    pdf.cell(w=0, h=10, txt=topic, align="L", ln=1)
    pdf.set_text_color(100, 100, 100)
    pdf.line(10, 19, 200, 19)

pdf.output("output.pdf")