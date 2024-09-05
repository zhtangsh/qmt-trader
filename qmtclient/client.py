import time

from xtquant.xttrader import XtQuantTrader
from xtquant.xttype import StockAccount
from typing import List
from .callbacks import *
from qmtmodel import *


class QmtClient:

    def __init__(self, path: str, account_number: str, callback=None, kafka_client=None):
        if callback is None:
            callback = DefaultXtQuantTraderCallback(kafka_client)
        self.session_id = int(time.time())
        self._account = StockAccount(account_number)
        self._trader = XtQuantTrader(path, self.session_id)
        self._trader.register_callback(callback)
        self.connected = False

    def check_connection(self):
        if self.connected:
            return
        ok = self._trader.start()
        logger.info(f"start response: {ok}")
        if not ok:
            logging.info("trader start failed, not connected")
            return
        ok = self._trader.connect()
        logger.info(f"connect response: {ok}")
        if not ok:
            logging.info("trader connect failed, not connected")
            return
        ok = self._trader.subscribe(self._account)
        logger.info(f"subscribe response: {ok}")
        if not ok:
            logging.info("trader subscribe failed, not connected")
            return
        self.connected = True

    def get_account_info(self) -> List[QmtAccountInfo]:
        self.check_connection()
        res = self._trader.query_account_infos()
        return [QmtAccountInfo(r) for r in res]

    def get_account_status(self) -> List[QmtAccountStatus]:
        self.check_connection()
        res = self._trader.query_account_status()
        return [QmtAccountStatus(r) for r in res]

    def get_stock_asset(self) -> QmtAsset:
        self.check_connection()
        asset = self._trader.query_stock_asset(self._account)
        return QmtAsset(asset)

    def get_trader(self) -> XtQuantTrader:
        return self._trader

    def get_account(self) -> StockAccount:
        return self._account

    def get_stock_orders(self, cancelable_only=False) -> List[QmtOrder]:
        self.check_connection()
        res = self._trader.query_stock_orders(self._account, cancelable_only=cancelable_only)
        return [QmtOrder(r) for r in res]

    def get_stock_trades(self) -> List[QmtTrade]:
        self.check_connection()
        res = self._trader.query_stock_trades(self._account)
        return [QmtTrade(r) for r in res]

    def get_stock_positions(self) -> List[QmtPosition]:
        self.check_connection()
        res = self._trader.query_stock_positions(self._account)
        return [QmtPosition(r) for r in res]

    def order_stock(self, stock_code, order_type, order_volume, price_type, price, strategy_name,
                    order_remark) -> int:
        """
        :param stock_code: str 证券代码，如'600000.SH'
        :param order_type: int 委托类型
        :param order_volume: int 委托数量，股票以'股'为单位，债券以'张'为单位
        :param price_type: int 报价类型
        :param price: float 委托价格
        :param strategy_name: str 策略名称
        :param order_remark: str 委托备注
        :return:
        """
        self.check_connection()
        return self._trader.order_stock(self._account, stock_code, order_type, order_volume, price_type, price,
                                        strategy_name, order_remark)

    def cancel_order_stock(self, order_id):
        self.check_connection()
        return self._trader.cancel_order_stock(self._account, order_id)
