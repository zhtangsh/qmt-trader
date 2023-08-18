from dotenv import load_dotenv

import xtquant.xtconstant  as xtconstant
from qmtclient import *
from utils import sys_utils

if __name__ == '__main__':
    load_dotenv()
    path = sys_utils.get_env('QMT_PATH')
    account_number = sys_utils.get_env('QMT_ACCOUNT')
    qmt_client = QmtClient(path, account_number)
    account_list = qmt_client.get_account_info()
    print(account_list)
    account_status_list = qmt_client.get_account_status()
    print(account_status_list)
    asset_list = qmt_client.get_stock_asset()
    print(asset_list)
    order = qmt_client.get_stock_orders(cancelable_only=False)
    print(order)
    trades = qmt_client.get_stock_trades()
    print(trades)
    positions = qmt_client.get_stock_positions()
    print(positions)
    stock_code = '600519.SH'
    order_type = xtconstant.STOCK_BUY
    order_volume = 100
    price_type = xtconstant.FIX_PRICE
    price = 1000
    strategy_name = '测试策略'
    order_remark = '测试'
    # order_id = qmt_client.order_stock(stock_code, order_type, order_volume, price_type, price, strategy_name,order_remark)
    # print(order_id)
