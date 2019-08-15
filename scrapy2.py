'''a simple python script to scrape emails from any website and other website linked to then  prints out on terminal emails found and website it was gotten from
and also option to download and save as csv file'''

import requests
from bs4 import BeautifulSoup
import re
import csv
from time import sleep

print("email scraper by fredcode\nc'2019")
url = input(" type a website:")
mails = []

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = [n.get('href') for n in soup.find_all('a')]
links.append(url)

def get_emails(l):   
    for _link in l:
        print("pls wait.... running code")
        if(_link.startswith("http") or _link.startswith("www")):
            data = requests.get(_link)
            _emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)
            if _emails:  # removing duplicates
                _emails = list(dict.fromkeys(_emails))
                mails.append((_emails, _link))     


get_emails(links)  # run code to print out
if len(mails) == 0:
    print("no emails found")
    sleep(5)
    exit()
print(mails)

#extra feature  to save to a csv file
ask_user = input("Do you want to save results to a csv file?\nReply with yes or no: ")
u_data=ask_user.lower()

if u_data == "yes":
    print("saving you file ......")
    name = url.split("//")
    csv_file = open(name[-1].replace(".com/","ES"), 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Emails","Link"])
    for i in mails:
        emails= ",".join(i[0])
        link = i[-1]
        csv_writer.writerow([emails,link])
    print("file downloaded")
    csv_file.close()
else:
    exit()




'''coded by fredcode - github[fredcodee]'''
