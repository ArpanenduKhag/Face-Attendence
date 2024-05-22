# import module
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO



# user define function
# Scrape the data
def getdata(url):
	r = requests.get(url)
	return r.text

# input by geek
train_name = "12311-Netaji SF Express"

# url
url = "https://www.railyatri.in/live-train-status/"+train_name

# pass the url
# into getdata function
htmldata = getdata(url)
soup = BeautifulSoup(htmldata, 'html.parser')

# traverse the live status from
# this Html code
data = []
for item in soup.find_all('script', type="application/ld+json"):
	data.append(item.get_text())

# convert into dataframe
#df = pd.read_json(data[2])
# Assuming data[2] contains your JSON string
json_string = data[2]
 
# Wrap the JSON string in a StringIO object
json_io = StringIO(json_string)

# Use read_json with the StringIO object
df = pd.read_json(json_io)


# display this column of
# dataframe
print(df["mainEntity"][0]['name'])
print(df["mainEntity"][0]['acceptedAnswer']['text'])
