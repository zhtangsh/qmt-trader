import time

from xtquant.xttrader import XtQuantTrader
from xtquant.xttype import StockAccount

from .callbacks import *
from qmtmodel import *


class QmtClient:

    def __init__(self, path:str, account_number: str, callback=None, ):
        if callback is None:
            callback = DefaultXtQuantTraderCallback()
        self.session_id = int(time.time())
        self._account = StockAccount(account_number)
        self._trader = XtQuantTrader(path, self.session_id)
        self._trader.register_callback(callback)
        self._trader.start()
        self._trader.connect()
        self._trader.subscribe(self._account)

    def get_account_info(self):
        res = self._trader.query_account_infos()
        return [QmtAccountInfo(r) for r in res]

    def get_account_status(self):
        res = self._trader.query_account_status()
        return [QmtAccountStatus(r) for r in res]

    def get_stock_asset(self):
        asset = self._trader.query_stock_asset(self._account)
        return QmtAsset(asset)

    def get_trader(self) -> XtQuantTrader:
        return self._trader

    def get_account(self) -> StockAccount:
        return self._account

    def get_stock_orders(self, cancelable_only=False):
        res = self._trader.query_stock_orders(self._account, cancelable_only=cancelable_only)
        return res

    def get_stock_trades(self):
        return self._trader.query_stock_trades(self._account)

    def get_stock_positions(self):
        return self._trader.query_stock_positions(self._account)

    def order_stock(self, stock_code, order_type, order_volume, price_type, price, strategy_name,
                    order_remark):
        """
        :param trader:
        :param account: StockAccount 资金账号
        :param stock_code: str 证券代码，如'600000.SH'
        :param order_type: int 委托类型
        :param order_volume: int 委托数量，股票以'股'为单位，债券以'张'为单位
        :param price_type: int 报价类型
        :param price: float 委托价格
        :param strategy_name: str 策略名称
        :param order_remark: str 委托备注
        :return:
        """
        return self._trader.order_stock(self._account, stock_code, order_type, order_volume, price_type, price,
                                        strategy_name, order_remark)

    def cancel_order_stock(self, order_id):
        return self._trader.cancel_order_stock(self._account, order_id)
