from dotenv import load_dotenv

from qmtclient import *
from utils import sys_utils

if __name__ == '__main__':
    load_dotenv()
    path = sys_utils.get_env('QMT_PATH')
    account_number = sys_utils.get_env('QMT_ACCOUNT')
    qmt_client = QmtClient(path,account_number)
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
