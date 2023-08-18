from dataclasses import dataclass


@dataclass
class QmtAccountInfo:
    account_id: str
    account_type: int
    broker_id: int
    broker_name: str
    broker_type: int
    login_status: str
    platform_id: int
    product_code: str
    product_id: str
    product_name: str

    def __init__(self, o):
        self.account_id = o.account_id
        self.account_type = o.account_type
        self.broker_id = o.broker_id
        self.broker_name = o.broker_id
        self.broker_type = o.broker_type
        self.login_status = o.login_status
        self.platform_id = o.platform_id
        self.product_code = o.product_code
        self.product_id = o.product_id
        self.product_name = o.product_name

    def get_account_number(self):
        return self.account_id

    def __repr__(self) -> str:
        return f"QmtAccountInfo(account_id:{self.account_id})"


@dataclass
class QmtAccountStatus:
    account_id: str
    account_type: int
    status: int

    def __init__(self, o):
        self.account_id = o.account_id
        self.account_type = o.account_type
        self.status = o.status


@dataclass
class QmtAsset:
    account_id: str
    account_type: str
    cash: float
    frozen_cash: float
    market_value: float
    total_asset: float

    def __init__(self, o):
        self.account_id = o.account_id
        self.account_type = o.account_type
        self.cash = o.cash
        self.frozen_cash = o.frozen_cash
        self.market_value = o.market_value
        self.total_asset = o.total_asset
