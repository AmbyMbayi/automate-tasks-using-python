import openpyxl
path = 'studentRecords.xlsx'

wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active

# getting the value of the first row first column
cell_obj = sheet_obj.cell(row=1, column=1)
print(cell_obj.value)

# determining the total number of rows

print(sheet_obj.max_row)

# determining the total number of columns
print(sheet_obj.max_column)


# printing column names
max_col = sheet_obj.max_column

for i in range(1, max_col + 1):
    cell_name = sheet_obj.cell(row=1, column=i)
    print(cell_name.value)
