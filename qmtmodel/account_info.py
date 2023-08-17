class QmtAccountInfo:

    def __init__(self, o):
        self.xquant_object = o
        self.account_id = o.account_id
        self.account_type = o.account_type
        self.broker_id = o.broker_id
        self.broker_name = o.broker_id
        self.broker_type = o.broker_type
        self.login_status = o.login_status
        self.m_nAccountType = o.m_nAccountType
        self.m_nBrokerType = o.m_nBrokerType
        self.m_nProductID = o.m_nProductID
        self.m_nStatus = o.m_nStatus
        self.m_strAccountID = o.m_strAccountID
        self.m_strBrokerID = o.m_strBrokerID
        self.m_strBrokerName = o.m_strBrokerName
        self.m_strProductCode = o.m_strProductCode
        self.m_strProductName = o.m_strProductName
        self.platform_id = o.platform_id
        self.product_code = o.product_code
        self.product_id = o.product_id
        self.product_name = o.product_name

    def get_account_number(self):
        return self.account_id

    def __repr__(self) -> str:
        return f"QmtAccountInfo(account_id:{self.account_id})"


class QmtAccountStatus:

    def __init__(self, o):
        self.xquant_object = o
        self.account_id = o.account_id
        self.account_type = o.account_type
        self.m_nAccountType = o.m_nAccountType
        self.m_nStatus = o.m_nStatus
        self.m_strAccountID = o.m_strAccountID
        self.status = o.status

    def get_account_number(self):
        return self.account_id

    def __repr__(self) -> str:
        return f"QmtAccountStatus(account_id:{self.account_id})"


class QmtAsset:

    def __init__(self, o):
        self.xquant_object = o
        self.account_id = o.account_id
        self.account_type = o.account_type
        self.cash = o.cash
        self.frozen_cash = o.frozen_cash
        self.market_value = o.market_value
        self.total_asset = o.total_asset

    def get_account_number(self):
        return self.account_id

    def __repr__(self) -> str:
        return f"QmtAsset(account_id:{self.account_id},cash:{self.cash},frozen_cash:{self.frozen_cash},market_value:{self.market_value},total_asset:{self.total_asset})"
