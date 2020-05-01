#guide - finding api 
#https://linuxconfig.org/introduction-to-ebay-api-with-python-the-finding-api-part-2#h3-the-finding-api-calls

from urllib.request import urlopen
import json
import requests
item = 'toy'
apikey = 'IvyZhang-LEGGO-PRD-1bcdef08f-c0149495'
# url = 'svcs.ebay.com/services/search/FindingService/v1/?OPERATION-NAME=findItemsByKeywords&sortOrder=PricePlusShippingLowest&SECURITY-APPBANE='+ apikey + '&RESPONSE-DATA-FORMAT=JSON%keywords=lego'
url = ('http://svcs.ebay.com/services/search/FindingService/v1?\
 ?OPERATION-NAME=findItemsByKeywords\
     &sortOrder=PricePlusShippingLowest\
         &buyerPostalCode=02461&SERVICE-VERSION=1.13.0\
             &SECURITY-APPNAME='+apikey+
             '&RESPONSE-DATA-FORMAT=JSON\
                 &REST-PAYLOAD\
                     &itemFilter(0).name=Condition\
                         &itemFilter(0).value=New\
                             &itemFilter(1).name=MaxPrice\
                                 &itemFilter(1).value=500.0\
                                     &itemFilter(1).paramName=Currency\
                                         &itemFilter(1).paramValue=USD\
                                             &keywords='+item)
                                            
result=requests.get(url)

print(result)

#urllib3.exceptions.ProtocolError
#requests.exceptions.ConnectionError: ('Connection aborted.', 
#   ConnectionResetError(10054, 'An existing connection was forcibly 
#   closed by the remote host', None, 10054, None))

