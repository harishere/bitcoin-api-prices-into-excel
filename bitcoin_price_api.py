#This program pulls Bitcoin prices from API URL: https://blockchain.info/ticker in JSON and saves in MS Excel file

#Importing libraries
import requests
import pandas as pd

#Initializing Requests
response = requests.get('https://blockchain.info/ticker')
response.raise_for_status()

#Access JSOn content
jsonResponse = response.json()

bitcoin_price = DataFrame(jsonResponse)

#Initialize ExcelWriter
#You can change the output directory here 
writer = pd.ExcelWriter(r'C:\Users\Haris\Desktop\Bitcoin_prices.xlsx', engine = 'xlsxwriter')

bitcoin_price.to_excel(writer, sheet_name = 'Sheet1')
writer.save()

#Print operation result
print('Excel file created successfully!!')

