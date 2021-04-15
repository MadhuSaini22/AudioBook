import pyttsx3
import PyPDF2

speaker = pyttsx3.init()    #create speaker
book = open('Computer Organization & Architecture.pdf','rb')  #open the particular book
pdfReader = PyPDF2.PdfFileReader(book)   #read by using module
pages = pdfReader.numPages  #total number of pages

#read the book upto any page you want
for num in range(7,pages):
    page = pdfReader.getPage(num) #getting the page
    text = page.extractText()   #extracting text
    speaker.say(text)  #call speaker to say text
    speaker.runAndWait()
