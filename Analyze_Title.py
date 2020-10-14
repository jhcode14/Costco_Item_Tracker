#import xlwt
#from datetime import date
#from ItemData import *

php1_lines = []
with open ("Monitor List.md", "rt") as myfile:
    for line in myfile:
        php1_lines.append(line)

#catagorize things in order
line_number = 0
list_of_results = []
#might need to change to array of array to better format the list

for line in php1_lines:
    line_number +=1
    if line.find("<title>") != -1:
        list_of_results.append((line_number,line.rstrip().strip("<title>").strip("| Costco</title>").strip()))
for elem in list_of_results:
    print('line numb = ', elem[0], 'line = ', elem[1])


"""
wb = xlwt.Workbook()
newsheet = wb.add_sheet(list_of_results[0][1])
wb.save(str(date.today()))



for line in php1_lines:
    line_number +=1
    if line.find("<title>") != -1:
        list_of_results.append((line_number,line.rstrip().strip("<title>").strip("| Costco</title>").strip()))
print('ms1')
for elem in list_of_results:
    print('line numb = ', elem[0], 'line = ', elem[1])
    print('ms2')
print('ms3')

.replace("<title>","")
"""