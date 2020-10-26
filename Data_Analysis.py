import re
from ItemData import ItemData
import requests

#setup values
Data = [ItemData]


def loadAndAnalysis(link):
    HEADERS = {'user-agent': ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0')}
    #  Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0
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
    arOrder = 0
    title = ""

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
            if lnlist == 0:
                lnlist = line_number

    #add name and price of the product to temp array
    #would be great to add spec later
    for line in php1_lines[lnlist:]:
        #add price (3)
        if line.find('<div class="price" id="price') != -1:
            temp_list[arOrder].extend([re.sub(r'^.+?"DEFAULT">',"", line).replace("</div>","")])
        #add name of the product (4)
        if line.find('<a href="https://www.costco.com/') != -1:
            temp_list[arOrder].extend([re.sub(r'^.+?html">',"", line).replace("</a>","")])
            arOrder +=1
            if len(temp_list) == arOrder:
                break
        
    #print('testing', list_of_results[1][2])

    for elem in temp_list:
        #print('type = ', elem[0], 'line numb = ', elem[1], 'link = ', elem[2], 'price= ', elem[3], 'product name= ', elem[4])
        #print("--------------------------------------------------------------------------------")
        Data.append(ItemData(elem[0], elem[4], elem[3], elem[2]))

def getTitle():
    return Data[1].getType
def getData():
    return Data