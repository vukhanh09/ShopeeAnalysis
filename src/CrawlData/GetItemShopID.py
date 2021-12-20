import requests 
import json
import pandas as pd
from tqdm import tqdm
def getItemShopID(match_id,newest):
    url_search_item = 'https://shopee.vn/api/v4/search/search_items?by=relevancy&limit=60&match_id={}&newest={}'
    
    def getItemShopId(data):
        itemId = data['item_basic']['itemid']
        shopId = data['item_basic']['shopid']
        return {
            'itemid':itemId,
            'shopid':shopId
        }
    
    try:
        data = requests.get(url_search_item.format(match_id,newest)).content
        data = json.loads(data)['items']
        res = list(map(getItemShopId,data))
        return pd.DataFrame(res)
    except:
        print(f"An exception occurred with match_id {match_id} and newest {newest} ")
    # res = pd.DataFrame(df)
    # return res