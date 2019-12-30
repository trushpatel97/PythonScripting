import PyPDF2
import sys

inputs = sys.argv[1:]#getting the arugments passed after the python  file call

def pdf_combiner(pdf_list):#creating a function
	merger = PyPDF2.PdfFileMerger()#calling function to merge pdfs
	for pdf in pdf_list:#get every pdf in the pdf list
		print(pdf)#prints the pdf
		merger.append(pdf)#aapends the pdf to the file merger
	merger.write('super.pdf')#merger writes all files into one

pdf_combiner(inputs)