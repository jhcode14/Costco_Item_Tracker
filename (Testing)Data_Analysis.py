"""
This is the ongoing work for second way to analyze html file as inconsistancies of HTML code found in costco.com
Which the coding line for price is sometimes in a line after my line.find(###) and sometimes the same line
"""
import re
from ItemData import ItemData
import requests

#Item According Array
Data = [ItemData]

def loadAndAnalysis(link):
    HEADERS = {'user-agent': ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0')}
    #  HEADER INFORMATION: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0
    http = requests.get(link,timeout=5, headers=HEADERS)
    if http.status_code == 200:
        print('Success')
    elif http.status_code == 404:
        print('fail')
    else:
        print("didnt work at all")
    filename = "html_temp.md"
    file_object = open(filename,"w+")
    file_object.write(http.text)
    file_object.close

    php1_lines = []
    with open (filename, "rt") as myfile:
        for line in myfile:
            php1_lines.append(line)

    #catagorize things in order
    line_number = 6000
    temp_list = []

    lnlist = 0
    arOrder = -1
    title = ""
    price_line = False
    for line in php1_lines:
        if line.find("<title>") != -1:
            title = line.rstrip().strip("<title>").strip("| Costco</title>").strip()

    #store type (0) line number (1) and link of product (2) in temporory list due to complications with sorting everything at once
    countIndex = 0
    for line in php1_lines[6000:]:
        line_number +=1
        if line.find('<div class="product-tile-set" data-set-same-height data-pdp-url=') != -1:
            temp_list.append([title,line_number,line.rstrip().replace('<div class="product-tile-set" data-set-same-height data-pdp-url=','').strip().strip(">").strip('"').strip('" item-index="'+str(countIndex))])
            countIndex += 1
            print (line)
            if lnlist == 0:
                lnlist = line_number

    #add name and price of the product to temp array
    #would be great to add spec later
    countIndex = 0
    c2 = 0
    print(len(temp_list))
    for line in php1_lines[lnlist:]:
        #add price (3) price go after name (4)->(3)
        if price_line:
            price_line = False
            arOrder +=1
            if len(temp_list) == arOrder:
                break
            temp_list[arOrder].extend([line.strip()])
            countIndex+=1
            print(str(countIndex)+line)
            
            
        elif line.find('<div class="price" id="price') != -1:
            price_line = True
        else:
            pass
            #Old way to dectect price (without price_line variable)
            #temp_list[arOrder].extend([re.sub(r'^.+?"DEFAULT">',"", line).replace("</div>","")])
        #add name of the product (4)
        #(OLD)if line.find('<a href="https://www.costco.com/') != -1:
        if line.find('<div class="product-tile-set" data-set-same-height data-pdp-url="https://www.costco.com/') != -1:
            #temp_list[arOrder].extend([re.sub(r'^.+?html">',"", line).replace("</a>","")])
            temp_list[arOrder].extend([line[:line.find('.html"')].replace("---"," ").replace('<div class="product-tile-set" data-set-same-height data-pdp-url="https://www.costco.com/','')])
            
            c2+=1
            #print(str(c2)+line)
            print(c2)
            
            
            

    for elem in temp_list:
        #For testing
        #print('type = ', elem[0], 'line numb = ', elem[1], 'link = ', elem[2], 'price= ', elem[3], 'product name= ', elem[4])
        print('type = ', elem[0])
        print( 'line numb = ', elem[1])
        print( 'link = ', elem[2])
        print( 'price= ', elem[3])
        print( 'product name= ', elem[4])
        print("--------------------------------------------------------------------------------")
        Data.append(ItemData(elem[0], elem[4], elem[3], elem[2]))

def getTitle():
    return Data[1].getType
def getData():
    return Data


#for testing
link = "https://www.costco.com/desktops-servers.html"
loadAndAnalysis(link)