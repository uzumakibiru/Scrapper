
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import csv

URL="https://store.steampowered.com/"

#Create a webdriver probably chorme using selenium
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)


#Function to return the details of the table row in dictionary
def to_dict(top_seller):
    driver.execute_script("window.scrollBy(0, 1000);")
    name=top_seller.find_element(By.CLASS_NAME,value="_1n_4-zvf0n4aqGEksbgW9N")
    nam=name.text
    try:
        price=top_seller.find_element(By.CSS_SELECTOR,value="._3j4dI1yA7cRfCvK8h406OB")
        pric=price.text
    except NoSuchElementException:
        print("No Such Element found")
        pric="N/A"
    weekly=top_seller.find_element(By.CLASS_NAME,value="xm7JpnZElM9XGF4ruu0Z-")
    weekl=weekly.text
    return {"name":nam,"price":pric,"weekly_appearance":weekl}

#Get Request to the URL
driver.get(URL)
#Get the content of the website through CSS selector
time.sleep(2)
sales_nav=driver.find_element(By.XPATH,value="/html/body/div[1]/div[7]/div[6]/div[3]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[4]/span/a[1]")
sales_nav.click()
top_sale_nav=driver.find_element(By.XPATH,value="/html/body/div[1]/div[7]/div[6]/div[3]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[5]/div/div[1]/a[1]")
top_sale_nav.click()

#Get the top sellers
time.sleep(3)
top_sellers=driver.find_elements(By.CLASS_NAME,"_2-RN6nWOY56sNmcDHu069P")
#Debugging
# for top in top_sellers:
#     time.sleep(3)
#     price=top.find_element(By.CLASS_NAME,value="_3j4dI1yA7cRfCvK8h406OB")
#     print(price.text)
#List of top sellers details in dcitionary form
time.sleep(3)
data=[to_dict(top_seller) for top_seller in top_sellers]

#Saving the data dictionary into csv
with open("steam_top_seller.csv",mode="w",newline="",encoding="utf-8") as file:
    writer= csv.DictWriter(file,fieldnames=["name","price","weekly_appearance"])
    writer.writeheader()
    writer.writerows(data)

#Quit the driver
driver.quit()