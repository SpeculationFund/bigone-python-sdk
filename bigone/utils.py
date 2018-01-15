import os
import uuid
import urllib2
import json


class Client():
    headers = {"Accept" : "application/json"}
    default_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    base_url = 'https://api.big.one/'
    apis = {
        'accounts': 'accounts',
        'account': 'accounts/%s',
        'markets': 'markets',
        'market': 'markets/%s',
        'market_book': 'markets/%s/book',
        'market_trades': 'markets/%s/trades',
        'trades': 'trades?market={}&limit={}&offset={}',
        'orders': 'orders?market={}&limit={}&offset={}',
        'order': 'orders/{}',
        'withdrawals': 'withdrawals?currency={}%limit={}&offset={}',
        'deposits': 'deposits?currency={}%limit={}&offset={}',
    }

    def __init__(self, api_key, user_agent=None):
        self.headers['Authorization'] = 'Bearer %s' % api_key
        self.headers['User-Agent'] = user_agent or self.default_agent
        self.headers['Big-Device-Id'] = str(uuid.uuid1())

    def _fire(self, url):
        url = os.path.join(self.base_url, url)
        req = urllib2.Request(url, headers=self.headers)
        res = urllib2.urlopen(req)
        if res.code != 200:
            raise Exception('request failed with error code %d' % res.code)
        content = json.loads(res.read())
        return content

    def get_accounts(self):
        url = self.apis.get('accounts')
        data = self._fire(url)['data']
        return data

    def get_account(self, account):
        url = self.apis.get('account') % account.upper()
        data = self._fire(url)['data']
        return data

    def get_markets(self):
        url = self.apis.get('markets')
        data = self._fire(url)['data']
        return data

    def get_market(self, market):
        url = self.apis.get('market') % market.upper()
        data = self._fire(url)['data']
        return data

    def get_market_book(self, market):
        url = self.apis.get('market_book') % market.upper()
        data = self._fire(url)['data']
        return data

    def get_market_trades(self, market):
        url = self.apis.get('market_trades') % market.upper()
        data = self._fire(url)['data']
        return data

    def get_trades(self, market, limit=10, offset=0):
        url = self.apis.get('trades').format(market.upper(), limit, offset)
        data = self._fire(url)['data']
        return data

    def get_orders(self, market, limit=10, offset=0):
        url = self.apis.get('orders').format(market.upper(), limit, offset)
        data = self._fire(url)['data']
        return data

    def get_order(self, id):
        url = self.apis.get('order').format(id)
        data = self._fire(url)['data']
        return data

    def get_withdrawals(self, currency, limit=10, offset=0):
        url = self.apis.get('withdrawals').format(currency, limit, offset)
        data = self._fire(url)['data']
        return data

    def get_deposits(self, currency, limit=10, offset=0):
        url = self.apis.get('deposits').format(currency, limit, offset)
        data = self._fire(url)['data']
        return data
