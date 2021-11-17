
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


driver = webdriver.Chrome(ChromeDriverManager().install())

def scrape_open_sea(): 
    url = "https://opensea.io/assets/0x7eef591a6cc0403b9652e98e88476fe1bf31ddeb/42"
        
    driver.get(url)
        
        
    floor_price = driver.find_element_by_xpath('.//div[@class="Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf Price--amount"]').text
    floor_price_int = float(floor_price)
    now = datetime.datetime.now()
        
        
    bid_ask_array = []
        
    time.sleep(5)
        
    price_list = driver.find_elements_by_xpath('.//li[@class="Tablereact__TableRow-sc-120fhmz-1 fwzXIM"]/div[@class="Tablereact__TableCellContainer-sc-120fhmz-2 kTLznA"][1]')
        
    for ind in price_list: 
        raw_text = ind.text
        clean_values = float(raw_text.split(" ")[0])
        bid_ask_array.append(clean_values)
            
    data_values = {
        "date": now, 
        "floor price": floor_price_int, 
        "bid ask": bid_ask_array
        }
    return data_values


print(scrape_open_sea())
