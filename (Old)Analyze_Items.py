import re
php1_lines = []
with open ("new_LaptopList1.md", "rt") as myfile:
    for line in myfile:
        php1_lines.append(line)

#catagorize things in order
line_number = 6000
list_of_results = []
lnlist = 0
arOrder = 0
#might need to change to array of array to better format the list

#add line number (0) and link of product (1)--------------------------------------------------------------------
for line in php1_lines[6000:]:
    line_number +=1
    if line.find('<div class="product-tile-set" data-set-same-height data-pdp-url=') != -1:
        list_of_results.append([line_number,line.rstrip().replace('<div class="product-tile-set" data-set-same-height data-pdp-url=','').strip().strip(">")])
        if lnlist == 0:
            lnlist = line_number

#add name of the product and price in order-------------------------------------------------------------
for line in php1_lines[lnlist:]:
    #add price (2)
    if line.find('<div class="price" id="price') != -1:
        list_of_results[arOrder].extend([re.sub(r'^.+?"DEFAULT">',"", line).replace("</div>","")])
    #add name of the product (3)
    if line.find('<a href="https://www.costco.com/') != -1:
        #print(re.sub(r'^.+?html">',"", line).replace("</a>",""))
        list_of_results[arOrder].extend([re.sub(r'^.+?html">',"", line).replace("</a>","")])
        #temp = line[0:line.find(".product.")]
        #list_of_results[arOrder].extend([re.sub(r'^.+?---',"", temp)])
        #print (re.sub(r'^.+?---',"", temp))
        arOrder +=1
    if len(list_of_results) == arOrder:
        break
        
#end phrase + testing-----------------------------------------------------------------------------------
#print('testing', list_of_results[1][2])

for elem in list_of_results:
    print('line numb = ', elem[0], 'line = ', elem[1], 'price= ', elem[2], 'product name= ', elem[3])

#Note: can not confirm if product = old product exists due to link might change
#Now compatable with computer_list(page1) and Monitor List:
#need to figure out a way to record product catagoryies with more than one page of product
