from xtquant.xttrader import XtQuantTraderCallback
from qmtmodel.trade import QmtOrder, QmtTrade
from kafka import KafkaProducer
import logging
import datetime
import sys

logger = logging.getLogger(__name__)


class DefaultXtQuantTraderCallback(XtQuantTraderCallback):
    kafka_client: KafkaProducer = None

    def __init__(self, kafka_client):
        self.kafka_client = kafka_client

    def on_disconnected(self):
        """
        连接断开
        :return:
        """
        logger.info(f'连接断开回调')

    def on_stock_order(self, order):
        """
        委托回报推送
        :param order: XtOrder对象
        :return:
        """
        qmt_order = QmtOrder(order)
        logger.info(order.price_type)
        logger.info(order)
        message = qmt_order.kafka_message()
        self.kafka_client.send('orderCallback', message)
        logger.info(f"委托回调:{order}")

    def on_stock_trade(self, trade):
        """
        成交变动推送
        :param trade: XtTrade对象
        :return:
        """
        qmt_trade = QmtTrade(trade)
        message = qmt_trade.kafka_message()
        self.kafka_client.send('tradeCallback', message)
        logger.info(f"成交回调:{trade}")

    def on_order_error(self, order_error):
        """
        委托失败推送
        :param order_error:XtOrderError 对象
        :return:
        """
        logger.info(order_error)
        logger.info(f"委托报错回调 {order_error.order_remark} {order_error.error_msg}")

    def on_cancel_error(self, cancel_error):
        """
        撤单失败推送
        :param cancel_error: XtCancelError 对象
        :return:
        """
        logger.info(cancel_error)
        logger.info(f"撤单失败推送:{sys._getframe().f_code.co_name}")

    def on_order_stock_async_response(self, response):
        """
        异步下单回报推送
        :param response: XtOrderResponse 对象
        :return:
        """
        logger.info(response)
        logger.info(f"异步委托回调 {response.order_remark}")

    def on_cancel_order_stock_async_response(self, response):
        """
        :param response: XtCancelOrderResponse 对象
        :return:
        """
        logger.info(f"on_cancel_order_stock_async_response:{response}")
        logger.info(response)

    def on_account_status(self, status):
        """
        :param response: XtAccountStatus 对象
        :return:
        """
        logger.info(f"on_account_status:{status}")
        logger.info(status)