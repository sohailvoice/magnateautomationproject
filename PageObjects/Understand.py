from pdf2docx import converter
pdf_file="Python Paractice Assigment 2.pdf"
docx_file ='Python Paractice Assigment 2.pdf'
cv = converter(pdf_file)
cv.convert(docx_file)
cv.close()