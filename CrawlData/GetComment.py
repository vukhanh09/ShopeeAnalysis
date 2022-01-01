import json
from urllib.request import urlopen, Request
import requests 
import pandas as pd
from tqdm import tqdm


def get_comment(ItemListID,topic):
    features = ['orderid', 'itemid', 'cmtid', 'ctime', 'rating', 'userid', 'shopid', 
            'comment', 'rating_star', 'status', 'mtime', 'editable', 'opt', 'filter']

    url = 'https://shopee.vn/api/v2/item/get_ratings?filter=1&itemid={}&limit=50&offset={}&shopid={}&type=0'
    
    out_put_data = []
    
    def getFeature(data):
        comment = {}
        comment['orderid'] = data['orderid']
        comment['itemid'] = data['itemid']
        comment['cmtid'] = data['cmtid']
        comment['rating'] = data['rating']
        comment['userid'] = data['userid']
        comment['shopid'] = data['shopid']
        comment['comment'] = data['comment']
        comment['rating_star'] = data['rating_star']
        comment['status'] = data['status']
        comment['orderid'] = data['orderid']
        comment['mtime'] = data['mtime']
        comment['editable'] = data['editable']
        comment['opt'] = data['opt']
        comment['filter'] = data['filter']
        comment['topic'] = str(topic)
        return comment




    for itemid, shopid in tqdm(ItemListID):
        try:
            rep = requests.get(url.format(itemid, 0, shopid)).content
            data = json.loads(rep)['data']
            # rating_total = data['item_rating_summary']['rcount_with_context']
        except:
            print('exception requests: ', itemid, shopid)
            continue


        for offset in range(0, 51, 50):
            try:
                rep = requests.get(url.format(itemid, offset, shopid)).content
                data = json.loads(rep)['data']['ratings']
                data = list(map(getFeature,data))
                
                out_put_data += data
            except:
                print("exception:", itemid, offset, shopid)    
    return out_put_data