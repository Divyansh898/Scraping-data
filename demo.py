import bs4
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
link='https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29'
page = requests.get(link)
page.content
soup = bs(page.content, 'html.parser')
products=[]              
prices=[]                
ratings=[]
name=soup.find('div',class_="_4rR01T")
name.text
rating=soup.find('div',class_="_3LWZlK")
rating.text
price=soup.find('div',class_='_30jeq3 _1_WHN1')
price.text
for data in soup.findAll('div',class_='_3pLy-c row'):
        names=data.find('div', attrs={'class':'_4rR01T'})
        price=data.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
        rating=data.find('div', attrs={'class':'_3LWZlK'})
        products.append(names.text) 
        prices.append(price.text) 
        ratings.append(rating.text)   
df=pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
df.head(10)
