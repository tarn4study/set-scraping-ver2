from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

url = 'https://www.set.or.th/th/market/product/stock/quote/AAV/financial-statement/company-highlights'

driver.get(url)

data_list = pd.read_html(driver.page_source)

data_list[0].to_excel(r'D:\Project\web scraping\set\AAV.xlsx')

writer = pd.ExcelWriter("AAV.xlsx", engine="openpyxl")
data_list[0].to_excel(writer, sheet_name='Sheet1', index=False)
data_list[1].to_excel(writer, sheet_name='Sheet2', index=False)
writer.close()

driver.close()