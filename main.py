#source: timotheus package 
#https://github.com/timotheus/ebaysdk-python/wiki/Finding-API-class

from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError


# class Offer:
#     ''' 
#     storing info for one product offering
#     '''
#     def __init__(self,title,price,condition,shipping,url):
#         self.title = title
#         self.price = price
#         self.condition = condition
#         self.shipping = shipping
#         self.url = url
    
#     def __str__(self):
#         return f'{self.title} \nprice: {self.price} \nis a {self.condition} product \nshipping type is: {self.shipping} \nproduct url: {self.url}'

def lookup_item(product):
    try:
        api = Finding(appid="IvyZhang-LEGGO-PRD-1bcdef08f-c0149495", config_file=None)
        response = api.execute('findItemsAdvanced', {'keywords': product},)

        # print(response.dict())
        item_dict = response.dict()
        # print(item_dict)
        
        #to print each offering 
        offerings = []
        for item in (item_dict['searchResult']['item']):
            title = item['title']
            price = item['sellingStatus']['convertedCurrentPrice']['value']
            url = item['viewItemURL']
            condition = item['condition']['conditionDisplayName']
            shipping = item['shippingInfo']['shippingType']
            item_info = condition + ' product: ' + title + '   Price in USD: '+ price + '   Shipping cost: ' + shipping + '   visit product page: ' + url + '.' 
            offerings.append(item_info)
        return offerings
        
        #plus sorting api 
        # print('STARTING NEW')
        # response = api.execute('findItemsAdvanced', {'keywords': 'lego white house'},{'sortOrder': 'PricePlusShippingLowest'})
        # item_dict = response.dict()
        # for item in (item_dict['searchResult']['item']):
        #     title = item['title']
        #     price = item['sellingStatus']['convertedCurrentPrice']['value']
        #     url = item['viewItemURL']
        #     condition = item['condition']['conditionDisplayName']
        #     shipping = item['shippingInfo']['shippingType']
        #     print(title + ' \n' + price + ' \n' + url + ' ' + '\nitem condition is:' + condition + '\nshipping type:' + shipping)
        #     print('')

        #to store list of offerings into a dictionary 
        # offerings = {}
        # for item in (item_dict['searchResult']['item']):
        #     title = item['title']
        #     price = item['sellingStatus']['convertedCurrentPrice']['value']
        #     url = item['viewItemURL']
        #     condition = item['condition']['conditionDisplayName']
        #     shipping = item['shippingInfo']['shippingType']
        #     offerings[title]=[price,condition,shipping,url]
        # print(offerings)
            


    except ConnectionError as e:
        print(e)
        return(e.response.dict())

# lookup_item('blender')