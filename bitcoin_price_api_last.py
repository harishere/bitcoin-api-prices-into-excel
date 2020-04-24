#This program pulls Bitcoin prices from API URL: https://blockchain.info/ticker in JSON and saves in MS Excel file

#Importing libraries
import requests
from pandas import Series
import pandas as pd

#Initializing Requests
response = requests.get('https://blockchain.info/ticker')
response.raise_for_status()

#Access JSOn content
jsonResponse = response.json()

#Extracting USD Last prices
dict1 ={} #empty dictionary

for n in jsonResponse:
    dict1[n] = jsonResponse[n]['last']


bitcoin_price = Series(dict1) #convert dictionary to Series

print(bitcoin_price) #optional

#Initialize ExcelWriter
#You can change the output directory here 
writer = pd.ExcelWriter(r'C:\Users\Haris\Desktop\Bitcoin_prices_last.xlsx', engine = 'xlsxwriter')

bitcoin_price.to_excel(writer, sheet_name = 'Sheet1')

writer.save()

#Print operation result
print('Excel file created successfully!!')