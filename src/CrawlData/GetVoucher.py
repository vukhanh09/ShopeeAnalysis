import json
from urllib.request import urlopen, Request
import requests 
import pandas as pd
from tqdm import tqdm


def getVoucher(ItemShopId,topic):
    url_voucher = 'https://shopee.vn/api/v4/pdp/get_shipping?itemid={}&shopid={}'
    df = []

    def getFeature(data):
        voucher = {}
        voucher['in_country'] = data['ungrouped_channel_infos']
        voucher['foreign'] = data['grouped_channel_infos_by_service_type']

        voucher['topic'] = str(topic)
        return voucher

    for x in tqdm(range(ItemShopId.shape[0])):
        a,b = ItemShopId.values[x]
        try:
            data = requests.get(url_voucher.format(a,b)).content
            data = json.loads(data)['data']
            data = getFeature(data)

            df.extend([data])
        except :
            print('Crawl website error')
    return df