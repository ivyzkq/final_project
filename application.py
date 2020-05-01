#register ebay API 
# https://www.youtube.com/watch?v=tYhajCmmpNk 


import datetime
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection as Finding

try:
    api = Finding(appid="9950a566-b82d-4256-b3a0-aa9092665189", config_file=None)
    response = api.execute('findItemsAdvanced', {'keywords': 'toy'})
    print(response.dict())
except ConnectionError as e:
    print(e)
    print(e.response.dict())



