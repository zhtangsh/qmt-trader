import datetime


class QmtOrder:
    def __init__(self, o):
        self.xquant_object = o
        self.account_id = o.account_id
        self.account_type = o.account_type
        self.order_id = o.order_id
        self.order_remark = o.order_remark
        self.order_status = o.order_status
        self.order_sysid = o.order_sysid
        self.order_status = o.order_status
        self.order_sysid = o.order_sysid
        self.order_time = o.order_time
        self.order_type = o.order_type
        self.order_volume = o.order_volume
        self.price = o.price
        self.price_type = o.price_type
        self.status_msg = o.status_msg
        self.stock_code = o.stock_code
        self.strategy_name = o.strategy_name
        self.traded_price = o.traded_price
        self.traded_volume = o.traded_volume

    def __repr__(self):
        return f"QmtOrder(order_id={self.order_id},order_time={datetime.datetime.fromtimestamp(self.order_time)},stock_code={self.stock_code}," \
               f"order_volume={self.order_volume},price={self.price},traded_price={self.traded_price},traded_volume={self.traded_volume}," \
               f"order_remark={self.order_remark},order_status={self.order_status},order_type={self.order_type},price_type={self.price_type}," \
               f"status_msg={self.status_msg},strategy_name={self.strategy_name})"


class QmtPosition:

    def __init__(self, o):
        self.xquant_object = o
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

    def __repr__(self):
        return f"QmtPosition(stock_code={self.stock_code},open_price={self.open_price},volume={self.volume}," \
               f"yesterday_volume={self.yesterday_volume}," \
               f"market_value={self.market_value},frozen_volume={self.frozen_volume},can_use_volume={self.can_use_volume})"


class QmtTrade:

    def __init__(self, o):
        self.xquant_object = o
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
        self.traded_time = o.traded_time
        self.traded_volume = o.traded_volume

    def __repr__(self):
        return f"QmtTrade(traded_id={self.traded_id},traded_price={self.traded_price},traded_amount={self.traded_amount}," \
               f"traded_volume={self.traded_volume},traded_time={datetime.datetime.fromtimestamp(self.traded_time)})"
