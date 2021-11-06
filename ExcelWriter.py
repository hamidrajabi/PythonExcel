#1-Import libraries
from openpyxl import Workbook
import random

#2-Generate random integer data as 20 tuples between (0,100)
data=[(int(random.random()*100),int(random.random()*100)) for i in range(20)]

#3-Initialize excel file
book=Workbook()
sheet=book.active

#4-Define the column names
sheet.append(("Variables","Functions"))

#5-Append data to sheet
for datum in data:
	sheet.append(datum)

#6-Save the ".xlsx" file
book.save("PythonExcel.xlsx")