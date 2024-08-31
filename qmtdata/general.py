from xtquant import xtdata
from typing import List, Dict


def get_live_tick(stock_code_list: List[str]) -> List[Dict[str, any]]:
    dat = xtdata.get_full_tick(stock_code_list)
    res = []
    for k, v in dat.items():
        tmp = {
            'stock_code': k,
            'datetime': v['timetag'],
            'last': v['lastPrice'],
            'open': v['open'],
            'high': v['high'],
            'low': v['low'],
            'volume': v['volume'],
            'a1': v['askPrice'][0],
            'a2': v['askPrice'][1],
            'a3': v['askPrice'][2],
            'a4': v['askPrice'][3],
            'a5': v['askPrice'][4],
            'a1_v': v['askVol'][0],
            'a2_v': v['askVol'][1],
            'a3_v': v['askVol'][2],
            'a4_v': v['askVol'][3],
            'a5_v': v['askVol'][4],
            'b1': v['bidPrice'][0],
            'b2': v['bidPrice'][1],
            'b3': v['bidPrice'][2],
            'b4': v['bidPrice'][3],
            'b5': v['bidPrice'][4],
            'b1_v': v['bidVol'][0],
            'b2_v': v['bidVol'][1],
            'b3_v': v['bidVol'][2],
            'b4_v': v['bidVol'][3],
            'b5_v': v['bidVol'][4],
        }
        res.append(tmp)
    return res


"""调用入口"""
if __name__ == '__main__':
    stock_list = ['113519.SH', '123113.SZ', '128108.SZ']
    dat = get_live_tick(stock_list)
    print(dat)
