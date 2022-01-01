import json
from urllib.request import urlopen, Request


def get_comment(ItemListID, timeout=10):
    features = ['orderid', 'itemid', 'cmtid', 'ctime', 'rating', 'userid', 'shopid', 
            'comment', 'rating_star', 'status', 'mtime', 'editable', 'opt', 'filter']

    url = 'https://shopee.vn/api/v2/item/get_ratings?filter=0&flag=0&itemid={}&limit=6&offset={}&shopid={}&type=0'
    
    out_put_data = []
    
    for itemid, shopid in ItemListID:
        try:
            rep = Request(url.format(itemid, 0, shopid), headers={'User-Agent': 'Mozilla/5.0'})
            page = urlopen(rep, timeout=timeout).read()
            data = json.loads(page)
            rating_total = data['data']['item_rating_summary']['rating_total']
        except:
            print('exception requests: ', itemid, shopid)
            continue


        for offset in range(0, rating_total, 6):

            try:
                rep = Request(url.format(itemid, offset, shopid), headers={'User-Agent': 'Mozilla/5.0'})
                page = urlopen(rep, timeout=timeout).read()
                data = json.loads(page)

                for cmt in data['data']['ratings']:
                    comment = {}
                    for ft in features:
                        comment[ft] = cmt[ft]
                    out_put_data.append(comment)

            except:
                print("exception:", itemid, offset, shopid)

    
    return out_put_data
