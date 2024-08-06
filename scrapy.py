import csv
import urllib
import json 
from zenrows import ZenRowsClient
from bs4 import BeautifulSoup

Url = 'https://www.scrapingcourse.com/button-click'
apikey = '<YOUR_ZENROWS_API_KEY>'
js_instructions = []

# Append Javascript functions to js_instructions array
# Simulate clicking "load more" button 3 times for 48 product result display
for i in range(5):
    js_instructions.append({"wait": 3000},)
    js_instructions.append({"evaluate": "document.getElementById('load-more-btn').click();"},)

params = {
    'url': url,
    'apikey': apikey,
    'js_render':'true',
    'js_instructions':urllib.parse.quote(json.dumps(js_instructions)),
    'Premium_proxy': 'true' # provide anonymity layer to web scraping activity
}

client = ZenRowsClient("<YOUR_ZENROWS_API_KEY>")
Response = client.get(url, params=params)
# store data of each product
products = []
soup = BeautifulSoup(response.text, "html.parser")
# Loop through occurrences with an attribute "product-item"
for item in soup.find_all("div", attrs={"class", "product-item"}):
    href = item.contents[1].get("href")
    product_name = item.contents[1].find(class_='product-name').text
    product_price = item.contents[1].find(class_='product-price').text.replace('$', '')
    products.append([product_name, product_price, href])
# Sort the list according to the highest price
Products = sorted(products, key=lambda x:float(x[1], reverse=True

# Specify the file name for the CSV file
file_name = "products.csv"

# Field names (headers)
field_names = ["Product Name", "Price", "Link"]

# Open the file in write mode
with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file) 
    writer.writerow(field_names)
    # Save first non duplicate 48 products
    for data in products[:48]:
        # Write the data to the CSV file
        writer.writerow(data)

print(f"Data successfully exported to CSV file '{file_name}'.")
 
params = {
    'url': url,
    'apikey': apikey,
    'js_render':'true'
}

# Loop through the first 5 items in the Products list
for product in products[:5]:
    url = product[2]
    response = client.get(url, params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    for item in soup.find_all('div', attrs={'class': 'product_meta'}):
        sku = item.contents[1].find(class_='sku').text

    description = soup.select('.woocommerce-Tabs-panel')[0]
    desc = description.contents[3].text
    # Append to the already existing products list
    products[products.index(product)].extend([sku, desc])
# New csv file
file_name = "products_extra_data.csv"

# Field names (headers)
field_names = ["Product Name", "Price", "Link", "SKU", "Description"]

# Open the file in write mode
with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file) 
    writer.writerow(field_names)
    # Save the first non duplicate 48 products
    for word in products[:48]:
        # Write the data to the CSV file
        writer.writerow(word)

print(f"CSV file '{file_name}' created successfully.")
