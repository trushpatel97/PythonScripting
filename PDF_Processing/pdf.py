import PyPDF2

with open('dummy.pdf','rb') as file:#we have to read binary else it wont be able to with makes sure to close files once done with statements
	reader = PyPDF2.PdfFileReader(file)
	page = reader.getPage(0)
	print(page.rotateCounterClockwise(90))
	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page)
	with open('tilt.pdf','wb') as new_file:
		writer.write(new_file)