import requests 
import json
import pandas as pd
from tqdm import tqdm
def getItemShopID(match_id):
    url_search_item = 'https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id={}&newest={0}'
    
    def getItemShopId(data):
        itemId = data['item_basic']['itemid']
        shopId = data['item_basic']['shopid']
        return {
            'itemid':itemId,
            'shopid':shopId
        }
    
    df = []
    for newest in tqdm(range(0,8001,60)):
        data = requests.get(url_search_item.format(match_id,newest)).content
        data = json.loads(data)['items']
        res = list(map(getItemShopId,data))
        df += res
    res = pd.DataFrame(df)
    return res