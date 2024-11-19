from fpdf import FPDF
import pandas as pd

dados = pd.read_csv('dados.csv')

titulo = "CERTIFICADO DE PARTICIPAÇÃO"
subtitulo = "Este certificado comprova que"
nome = "Alexandre Sauer"
texto2 = "concluiu com êxito o curso GRATUITO DE PYTHON ministrado por"
texto3 = "PROF. SAUER entre 18/11/2024 a 21/11/2024,"
texto4 = "com carga horária de aproximadamente 08 horas"

for nome in dados['nomecompleto']:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', size=15)
    pdf.image("template.png", x=0, y=0)
    pdf.set_text_color(33,24,136)
    pdf.text(65,95,titulo)
    pdf.text(67,120,subtitulo)
    pdf.text(70,145,nome)
    pdf.text(20,165,texto2)
    pdf.text(20,175,texto3)
    pdf.text(20,185,texto4)
    pdf.output(f"Certificado_{nome}.pdf")

















