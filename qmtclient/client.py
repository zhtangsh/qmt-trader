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
        self.connected = False
        self.path = path
        self.account_number = account_number
        self.callback = callback

    def check_connection(self):
        if self.connected:
            return True
        self.session_id = int(time.time())
        self._account = StockAccount(self.account_number)
        self._trader = XtQuantTrader(self.path, self.session_id)
        self._trader.register_callback(self.callback)
        ok = self._trader.start()
        logger.info(f"start response: {ok}")
        if ok is not None:
            logging.info("trader start failed, not connected")
            return False
        ok = self._trader.connect()
        logger.info(f"connect response: {ok}")
        if ok != 0:
            logging.info("trader connect failed, not connected")
            return False
        ok = self._trader.subscribe(self._account)
        logger.info(f"subscribe response: {ok}")
        if ok != 0:
            logging.info("trader subscribe failed, not connected")
            return False
        self.connected = True
        return True

    def get_account_info(self) -> List[QmtAccountInfo]:
        ok = self.check_connection()
        if not ok:
            raise RuntimeError("qmt client not ready")
        res = self._trader.query_account_infos()
        return [QmtAccountInfo(r) for r in res]

    def get_account_status(self) -> List[QmtAccountStatus]:
        ok = self.check_connection()
        if not ok:
            return []
        res = self._trader.query_account_status()
        return [QmtAccountStatus(r) for r in res]

    def get_stock_asset(self) -> QmtAsset:
        ok = self.check_connection()
        if not ok:
            raise RuntimeError("qmt client not ready")
        asset = self._trader.query_stock_asset(self._account)
        return QmtAsset(asset)

    def get_trader(self) -> XtQuantTrader:
        return self._trader

    def get_account(self) -> StockAccount:
        return self._account

    def get_stock_orders(self, cancelable_only=False) -> List[QmtOrder]:
        ok = self.check_connection()
        if not ok:
            raise RuntimeError("qmt client not ready")
        res = self._trader.query_stock_orders(self._account, cancelable_only=cancelable_only)
        return [QmtOrder(r) for r in res]

    def get_stock_trades(self) -> List[QmtTrade]:
        ok = self.check_connection()
        if not ok:
            raise RuntimeError("qmt client not ready")
        res = self._trader.query_stock_trades(self._account)
        return [QmtTrade(r) for r in res]

    def get_stock_positions(self) -> List[QmtPosition]:
        ok = self.check_connection()
        if not ok:
            raise RuntimeError("qmt client not ready")
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
        ok = self.check_connection()
        if not ok:
            raise RuntimeError("qmt client not ready")
        return self._trader.order_stock(self._account, stock_code, order_type, order_volume, price_type, price,
                                        strategy_name, order_remark)

    def cancel_order_stock(self, order_id):
        ok = self.check_connection()
        if not ok:
            raise RuntimeError("qmt client not ready")
        return self._trader.cancel_order_stock(self._account, order_id)
