import requests 
import json
import pandas as pd
from tqdm import tqdm
def getItemDetail(ItemShopId,topic):
    url_detail_item = 'https://shopee.vn/api/v4/item/get?itemid={}&shopid={}'
    df = []
    for x in tqdm(range(ItemShopId.shape[0])):
        a,b = ItemShopId.values[x]
        try:
            data = requests.get(url_detail_item.format(a,b)).content
            data = json.loads(data)['data']
            data['topic'] = str(topic)
            df.extend([data])
        except:
            print('Crawl website error')
    return df