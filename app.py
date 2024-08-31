import json

from flask import Flask
from flask_jsonrpc import JSONRPC
from utils import sys_utils
from qmtclient import QmtClient
from dotenv import load_dotenv
from typing import List, Dict
from qmtmodel import *
from flask.json import JSONEncoder
from kafka import KafkaProducer
from qmtdata import general


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, datetime.date):
                return obj.isoformat()
            elif isinstance(obj, datetime.datetime):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
jsonrpc = JSONRPC(app, "/api", enable_web_browsable_api=True)
ACCOUNT_REF = {}
load_dotenv()


def get_trader(code: str = 'default') -> QmtClient:
    if code not in ACCOUNT_REF:
        path = sys_utils.get_env('QMT_PATH')
        account_number = sys_utils.get_env('QMT_ACCOUNT')
        kafka_url = sys_utils.get_env('KAFKA_URL', '192.168.1.60:9092')
        producer = KafkaProducer(bootstrap_servers=kafka_url, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        ACCOUNT_REF[code] = QmtClient(path, account_number, kafka_client=producer)
    return ACCOUNT_REF[code]


@jsonrpc.method("accountInfo.getAccountStatus")
def get_account_status() -> List[QmtAccountStatus]:
    trader = get_trader()
    res = trader.get_account_status()
    return res


@jsonrpc.method("accountInfo.getAccountInfo")
def get_account_info() -> List[QmtAccountInfo]:
    trader = get_trader()
    res = trader.get_account_info()
    return res


@jsonrpc.method("accountInfo.getStockAsset")
def get_stock_asset() -> QmtAsset:
    trader = get_trader()
    res = trader.get_stock_asset()
    return res


@jsonrpc.method("tradeInfo.getStockOrders")
def get_stock_orders(cancelable_only: bool = False) -> List[QmtOrder]:
    trader = get_trader()
    res = trader.get_stock_orders(cancelable_only=cancelable_only)
    return res


@jsonrpc.method("tradeInfo.getStockTrades")
def get_stock_trades() -> List[QmtTrade]:
    trader = get_trader()
    res = trader.get_stock_trades()
    return res


@jsonrpc.method("tradeInfo.getStockPositions")
def get_stock_positions() -> List[QmtPosition]:
    trader = get_trader()
    res = trader.get_stock_positions()
    return res


@jsonrpc.method("trade.orderStock")
def order_stock(
        stock_code: str,
        order_type: int,
        order_volume: int,
        price_type: int,
        price: float,
        strategy_name: str,
        order_remark: str
) -> int:
    trader = get_trader()
    res = trader.order_stock(stock_code, order_type, order_volume, price_type, price, strategy_name, order_remark)
    return res


@jsonrpc.method("trade.cancel_order_stock")
def cancel_order_stock(
        order_id: int
) -> int:
    trader = get_trader()
    res = trader.cancel_order_stock(order_id)
    return res


@jsonrpc.method("data.live_tick_data")
def live_tick_data(
        order_id_list: List[str]
) -> List[Dict[str, any]]:
    res = general.get_live_tick(order_id_list)
    return res


app.run(host='0.0.0.0', port=6000)
