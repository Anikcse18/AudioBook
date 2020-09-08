#must download pyttsx3 and PyPDF2 packeg in your Pc
import pyttsx3
import PyPDF2

book = open("Book.pdf",'rb')
pdf_reader = PyPDF2.PdfFileReader(book)
pages = pdf_reader.numPages


for i in range(5,pages):
    helper = pyttsx3.init()
    page = pdf_reader.getPage(i)
    text = page.extractText()
    helper.say(text)
    helper.runAndWait()

