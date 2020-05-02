#source: timotheus package 
#https://github.com/timotheus/ebaysdk-python/wiki/Finding-API-class

from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

try:
     api = Finding(appid="IvyZhang-LEGGO-PRD-1bcdef08f-c0149495", config_file=None)


     def lookup_item(product):
        '''
        
        product: string of product name. not case sensitive. 
        return offering: a list of dictionary, in order of best keyword match.

        '''
            # print(response.dict())
            # print(item_dict)
        response = api.execute('findItemsAdvanced', {'keywords': product})
        item_dict = response.dict()
        offerings = []
        for item in (item_dict['searchResult']['item']):
            title = item['title']
            price = item['sellingStatus']['convertedCurrentPrice']['value']
            url = item['viewItemURL']
            condition = item['condition']['conditionDisplayName']
            shipping = item['shippingInfo']['shippingType']
            item_info = {'title':title, 'price':price, 'condition':condition, 'shipping':shipping, 'url':url}
            offerings.append(item_info)
        return offerings


    #  def sort_price(product):
    #     '''

    #     product: string of product name. not case sensitive. 
    #     return sorted: a list of dictionary, in order of price(product + shipping if available）cheapest to most expensive.
        
    #     '''
    #     response = api.execute('findItemsAdvanced', {'keywords': product})
    #     item_dict = response.dict()
    #     sorted = []
    #     for item in (item_dict['searchResult']['item']):
    #          title = item['title']
    #          price = item['sellingStatus']['convertedCurrentPrice']['value']
    #          url = item['viewItemURL']
    #          condition = item['condition']['conditionDisplayName']
    #          shipping = item['shippingInfo']['shippingType']
    #          item_info = {'title':title, 'price':price, 'condition':condition, 'shipping':shipping, 'url':url}
    #          sorted.append(item_info)
    #     return sorted

    #  def store(product):
    #      '''
    #      product: string of product name. not case sensitive. 
    #      return store_dict: a dictionary with key = product title and value as a list of attributes.
    #      '''

    #     response = api.execute('findItemsAdvanced', {'keywords': product})
    #     item_dict = response.dict()
    #     store_dict = {}
    #     for item in (item_dict['searchResult']['item']):
    #         title = item['title']
    #         price = item['sellingStatus']['convertedCurrentPrice']['value']
    #         url = item['viewItemURL']
    #         condition = item['condition']['conditionDisplayName']
    #         shipping = item['shippingInfo']['shippingType']
    #         store_dict[title]=[price,condition,shipping,url]
    #     return store_dict
            
     
except ConnectionError as e:
    print(e)


# print(lookup_item('blender'))
# print(sort_price('lego'))
# print(store('bottle'))