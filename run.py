print("hello World")
import requests

HEADERS = {'user-agent': ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0')}
# Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0


http = requests.get('https://www.costco.com/pc-laptops.html',timeout=5, headers=HEADERS)

if http.status_code == 200:
    print('Success')
elif http.status_code == 404:
    print('fail')
else:
    print("didnt work at all")

file_object = open("computer_List.md","w+")
file_object.write(http.text)
file_object.close
print('done')

