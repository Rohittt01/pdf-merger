from PyPDF2 import PdfMerger
import os

pdf_directory = './pdfs'

pdf_merger = PdfMerger()

pdf_files = [files for files in os.listdir(pdf_directory) if files.endswith(".pdf")]

pdf_files.sort()

for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_directory, pdf_file)
    pdf_merger.append(pdf_path)

output_path = "./pom.pdf"
pdf_merger.write(output_path)
pdf_merger.close()