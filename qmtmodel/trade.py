import datetime
from dataclasses import dataclass


@dataclass
class QmtOrder:
    account_id: str
    account_type: int
    order_id: int
    order_remark: str
    order_status: int
    order_sysid: str
    order_status: str
    order_time: datetime.datetime
    order_type: int
    order_volume: float
    price: float
    price_type: str
    stock_code: str
    status_msg: str
    strategy_name: str
    traded_price: float
    traded_volume: float

    def __init__(self, o):
        self.account_id = o.account_id
        self.account_type = o.account_type
        self.order_id = o.order_id
        self.order_remark = o.order_remark
        self.order_status = o.order_status
        self.order_sysid = o.order_sysid
        self.order_status = o.order_status
        self.order_time = datetime.datetime.fromtimestamp(o.order_time)
        self.order_type = o.order_type
        self.order_volume = o.order_volume
        self.price = o.price
        self.price_type = o.price_type
        self.status_msg = o.status_msg
        self.stock_code = o.stock_code
        self.strategy_name = o.strategy_name
        self.traded_price = o.traded_price
        self.traded_volume = o.traded_volume


@dataclass
class QmtPosition:
    account_id: str
    account_type: int
    can_use_volume: float
    frozen_volume: float
    market_value: float
    on_road_volume: float
    open_price: float
    stock_code: str
    volume: float
    yesterday_volume: float

    def __init__(self, o):
        self.account_id = o.account_id
        self.account_type = o.account_type
        self.can_use_volume = o.can_use_volume
        self.frozen_volume = o.frozen_volume
        self.market_value = o.market_value
        self.on_road_volume = o.on_road_volume
        self.open_price = o.open_price
        self.stock_code = o.stock_code
        self.volume = o.volume
        self.yesterday_volume = o.yesterday_volume


@dataclass
class QmtTrade:
    account_id: str
    account_type: int
    order_remark: str
    order_sysid: str
    order_type: int
    stock_code: str
    strategy_name: str
    traded_amount: float
    traded_id: str
    traded_price: float
    traded_time: datetime.datetime
    traded_volume: float

    def __init__(self, o):
        self.account_id = o.account_id
        self.account_type = o.account_type
        self.order_id = o.order_id
        self.order_remark = o.order_remark
        self.order_sysid = o.order_sysid
        self.order_type = o.order_type
        self.stock_code = o.stock_code
        self.strategy_name = o.strategy_name
        self.traded_amount = o.traded_amount
        self.traded_id = o.traded_id
        self.traded_price = o.traded_price
        self.traded_time = datetime.datetime.fromtimestamp(o.traded_time)
        self.traded_volume = o.traded_volume