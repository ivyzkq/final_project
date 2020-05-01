#source: https://www.youtube.com/watch?v=O5KdYrD6_H4&t=188s


from ebaysdk.finding import Connection 
from bs4 import BeautifulSoup

Keywords ='piano'
api = Connection(appid='IvyZhang-LEGGO-PRD-1bcdef08f-c0149495',config_file=None)
api_request = {'keywords':Keywords, 'outputSelector':'SellerInfo'}

response = api.execute('findItembyKeywords',api_request)
soup = BeautifulSoup(response.content,'lxml')
items = soup.find_all('item')

# input(items[0])
#ebaysdk.exception.ConnectionError
print(items)