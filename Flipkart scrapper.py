import urllib
import urllib.request
from bs4 import BeautifulSoup
import csv

def soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    thepage.close()
    return soupdata

surl = "https://www.flipkart.com/grocery-supermart-store?marketplace=GROCERY&fm=neo%2Fmerchandising&iid=M_fc0a3589-55eb-4985-b88e-49b64d11697f_1_372UD5BXDFYS_MC.CBUR1Q46W5F1&otracker=hp_rich_navigation_1_1.navigationCard.RICH_NAVIGATION_Grocery_CBUR1Q46W5F1&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L0_view-all&cid=CBUR1Q46W5F1"

data_list = []

for record in soup1.findAll("div", {"class": "_1YokD2 _3Mn1Gg"}):
    for record2 in record.findAll("div", {"class": "sg-col-inner"}):
        for record3 in record2.findAll("div", {"class": "_4rR01T"}):
            title = record3.text.replace(',', '..')

        for record4 in record2.findAll("div", {"class": "_30jeq3 _1_WHN1"}):
            price = record4.text.replace(',', '')
        data_list.append([title, price])

for record in soup1.findAll("div", {"class": "s-main-slot s-result-list s-search-results sg-row"}):
    for record2 in record.findAll("div", {"class": "s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t1 puis-include-content-margin puis s-latency-cf-section s-card-border"}):
        for record3 in record2.findAll("span", {"class": "a-size-medium a-color-base a-text-normal"}):
            title = record3.text.replace(',', '..')

        for record4 in record2.findAll("span", {"class": "a-price-whole"}):
            price = record4.text.replace(',', '')
        data_list.append([title, price])

header = ["mobile name", "price"]
file_path = "outline.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data_list)

print("Data written to 'outline.csv' successfully.")

