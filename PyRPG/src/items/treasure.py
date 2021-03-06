"""
Created on 05/apr/2015

Updated 12/11/2016: revised Money class.
        03/12/2016: Money with collections.Counter class

@author: marcello
Issues:
- should be added a method for "subtract" money or not? It may be used add
method.
- evaluate the utility of a function of add/left single type of coin.
"""
from collections import Counter, Iterable
from functools import singledispatch

from items.constants import COIN_WEIGHT, DD_CURRENCIES, GEM_WEIGHT, \
    DD_CURRENCY_EXCHANGE
from items.item import Item

# constants

MONEY_STR = '''\
Money:
Copper: {n[copper]}
Silver: {n[silver]}
Gold: {n[gold]}
Electrum: {n[electrum]}
Platinum: {n[platinum]}
'''


class Money(Item):
    """Base class for money.

    It should be viewed as an amount of money, with all kind of coins counted
    from 0.
    """

    def __init__(self, amount=None,
                 curr: tuple = DD_CURRENCIES,
                 curr_exch: dict = DD_CURRENCY_EXCHANGE,
                 **kwargs):
        """
        amount     -- an iterable with the amount of  of coin.
        curr       -- tuple with matched currencies names (default D&D).
        curr_exch  -- dict with currencies exchange rate in gold (def. D&d)
        kwargs     -- {currency: amount} pairs

        If amount is a {coin, amount} dict, currencies isn't taken into account.
        If amount is None kwargs is used (e.g. gold=10, copper=120)

        Does not check if the amount of coins is negative.
        """
        super().__init__(name='money', weight=0)
        self._curr_exch = curr_exch
        # initialize the Counter amount to 0 counts
        self._amount = Counter({c: 0 for c in curr_exch.keys()})

        # for list, tuple, and dict argument
        if amount:
            if isinstance(amount, (list, tuple)):
                self._amount += Counter({c: v for c, v in zip(curr, amount)})

            elif isinstance(amount, dict):
                self._amount = Counter({c: 0 for c in curr_exch.keys()})
                self._amount += Counter(amount)
            else:
                pass # TODO: raise error?

        # for kwargs specified
        if kwargs:
            # if kwargs's not empty, add currencies amounts
            self._amount += Counter(kwargs)


    @property
    def weight(self) -> float:
        return sum(self._amount.values()) * COIN_WEIGHT


    def coins(self, coin: str = None):
        """Returns the amounts of all or specified type of coins.

        If no coin is specified, it returns a Counter with all coins and
        relative amounts. Otherwise, it returns the number (int) of the
        specified coin.
        """
        if not coin:
            return Counter(self._amount)
        return self._amount[coin]

    @property
    def value(self, exchange: list = DD_CURRENCY_EXCHANGE) -> float:
        """Return the overall value of all coins in gold coins.

        Return a float, since the value could not be an exact multiple of gold
        coins.
        """
        return sum((self._amount[coin]*rate for coin, rate
                    in exchange.items()))
            
    # operators

    def add(self, other: 'Money'):
        """Add another Money object to the caller, merging them.

        The Money object added will be emptied.
        """
        for coin in DD_CURRENCIES:
            self._amount[coin] += other.get_coins()[coin]
            other._amount[coin] = 0

    # inner methods

    def _aggregate_value(self):
        """Return the value of the Money in integer amounts of currencies."""
        pass # TODO: aggregate value

    def __str__(self):
        return MONEY_STR.format(n=self._amount)
        
        
class Gem(Item): # TODO: revisiting Gem class
    '''Class for gem objects.'''
    
    def __init__(self, value: int = 5, descr: str = ''):
        '''For default returns a low value anonym gem.
        
        >>> g = Gem()
        >>> print(g)
        Gem:
        Description: 
        Value: 5
        '''
        super().__init__('gem', GEM_WEIGHT)
        self._value = value
        self._description = descr
        
    def get_description(self):
        '''
        >>> g = Gem(descr='A beautyful gem but stinks')
        >>> g.get_description()
        'A beautyful gem but stinks'
        '''
        return self._description
        
    def get_value(self):
        '''
        >>> g = Gem(value=50)
        >>> g.get_value()
        50
        '''
        return self._value
        
    def __str__(self):
        return 'Gem:\nDescription: {s._description}\nValue: {s._value}'\
                .format(s=self)
       
