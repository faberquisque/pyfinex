from ..api import request

def deposit_withdrawal_movements(key, secret_key, Currency='BTC', **params):
    """ View your past deposits/withdrawals.
    Docs: https://bitfinex.readme.io/v2/reference#movements
    """
    endpoint = f'auth/r/movements/{Currency}/hist'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)

def past_trades_by_order(key, secret_key, Symbol='tBTCUSD', OrderId='', **params):
    """ Get Trades generated by an Order
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-order-trades
    """
    endpoint = f'auth/r/order/{Symbol}:{OrderId}/trades'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)

def past_trades(key, secret_key, Symbol='tBTCUSD', **params):
    """ Get Trades generated by an Order
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-trades-hist
    """
    endpoint = f'auth/r/order/{Symbol}/trades'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)

def past_fundings(key, secret_key, Symbol='fUSD', **params):
    """ Get funding trades
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-funding-trades-hist
    """
    endpoint = f'auth/r/funding/trades/{Symbol}/hist'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)
