import xlsxwriter as xl
import csv
import linecache

rowNo=2
totalLines=0
skipped=0
firstLine=False

#userinput
fileName = input("Enter the CVS filename that you will want to convert :")
try:
    openfile = sv.reader(open(fileName + '.csv',"r"),quotechar='"', delimiter=",",quoting=csv.QUOTE_ALL, skipinitialspace=True)
except FileNotFoundError:
    print('File does not exist, please make sure that the filie is in same directory as this script and run it again')

#if first row of the CSV file contains the column details
containsName = input('Does the first row of the CSV file contain the column name? (y/n): ').lower()
if containsName in ['y', 'yes']:
    columnNames = next(openFile)
    columnLength = len(columnNames)
    print('Rows with column length less than or greater than',columnLength,'will be ignored')
    firstLine = True
else:
    columnNames = []
    columnLength = input('Enter number of columns from the CSV file that you want to import: ')
    print('Rows with column length less than or greater than',columnLength, 'will be ignored')
    print('Enter column names to be entered in the XLS document: ')
    for x in range(1, int(columnLength) + 1):
        cName = input('column name #' + str(x) + ': ')
        columnNames.append(cName)

#userinput the name of xls file
xlFileName = input('Enter the name by which you want the XLS file to be saved: ')
workbook = xl.workbook.Workbook(xlFileName + '.xlsx')
worksheet = workbook.add_worksheet()
cell_format = workbook.add_format({'bold': True})
worksheet.set_row(0, 15, cell_format)
worksheet.write_row('A1', columnNames)

#copy data from CSV to XLS
for row in openFile:
    if firstLine:
        firstLine = False
        continue
    elif not len(row) < int(columnLength) or len(row) > int(columnLength):
        worksheet.write_row('A' + str(rowNo), row)
        rowNo += 1
        totalLines += 1
    else:
        skipped += 1
workbook.close()

#print details
print('Successfully wrote', totalLines, 'line(s) in the XLS')
print('Skipped', skipped, 'line(s) from the CSV due to column length mismatch')
print('Successfully created ' + str(xlFileName) + '.xlsx in the working directory!')
