#1-Import libraries
import openpyxl
import os
import matplotlib.pyplot as plt

#2-Define the File variable
file=os.getcwd()+"/"+os.listdir()[0]

#3-load the .xlsx file
book=openpyxl.load_workbook(file)
sheet=book.active

#4-Define lists for x and y
x=[sheet[i][0].value for i in range(2,20)]
y=[sheet[i][1].value for i in range(2,20)]

#5-Scatter plot the points
plt.scatter(x,y)
plt.xlabel(sheet[1][0].value)
plt.ylabel(sheet[1][1].value)
plt.show()


