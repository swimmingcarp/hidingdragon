# -*- coding:utf-8 -*-
# Copyright 2020 carp-project
# Author: Ma Yifang
# Date: 2020/7/31
# File Name: event.py

class Event(object):
    """
    Base class
    """
    pass

class MarketEvent(Event):
    """
    Update from real-time stock market.
    """
    def __init__(self):
        self.type = 'MARKET'

class SignalEvent(Event):
    """
    Generated by Strategy Object, received by Portfolio Object.
    """
    def __init__(self, strategy_id, symbol, date, signal, strength):
        self.strategy_id = strategy_id
        self.type = 'SIGNAL'
        self.stock_symbol = symbol      # a symbol represents one stock
        self.date = date
        self.signal = signal
        self.strength = strength

class OrderEvent(Event):
    """
    Handle order info, including stock symbol, stock price, signal (buy/sell)
    """
    def __init__(self, symbol, order_type, quantity, signal):
        self.type = 'ORDER'
        self.stock_symbol = symbol
        self.order_type = order_type    # order type: long/short, we have only long type in China.
        self.quantity = quantity        # how many shares (100 shares at least)
        self.signal = signal            # signal (buy/sell)

    def print_order():
        print("Order: Symbol %s, Quantity %s, Signal: %s"
              %(self.stock_symbol, self.quantity, self.signal))

class FillEvent(Event):
    """
    More details from trade execution.
    """
    def __init__(self, date, symbol, exchange, quantity, signal, fill_cost, commission=None):
        self.type = 'FILL'
        self.date = date
        self.symbol = symbol
        self.exchange = exchange
        self.quantity = quantity
        self.signal = signal
        self.fill_cost = fill_cost
        self.commission = commission

