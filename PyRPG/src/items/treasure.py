'''
Created on 05/apr/2015

@author: marcello
'''

from items.item import Item

#constants
COIN_WEIGHT = 0.02 # a coin weights 20 grams (0.02 Kilos)

DD_CURRENCIES = ['platinum', 'gold', 'electrum', 'silver', 'copper']

# value is in gold coins
# platinum = 5    gold
# gold     = 1    gold
# electrum = 0.5  gold
# silver   = 0.1  gold
# copper   = 0.01 gold
DD_CURRENCY_EXCHANGE = {c: e for c, e in 
                        zip(DD_CURRENCIES, [5, 1, 0.5, 0.1, 0.01])} 

class Money(Item):
    '''Base class for money.
    
    It should be viewed as an amount of money, with all kind of coins counted
    from 0 to Inf.
    '''
    
    def __init__(self, amount: dict = {'copper': 1}):
        '''Amount is a dict with type of coin as key and number as value.
        
        >>> m = Money(amount={'copper': 25, 'silver': 2})
        >>> print(m)
        Money:
        Copper: 25
        Silver: 2
        Gold: 0
        Electrum: 0
        Platinum: 0
        
        Does not check if the amount of coins is negative.
        '''
        super().__init__(name='money', weight=sum(amount.values())*COIN_WEIGHT)
        self._amount = {coin: amount.get(coin, 0) for coin in DD_CURRENCIES}
        
    def __str__(self):
        return "Money:\nCopper: {n[copper]}\nSilver: {n[silver]}" \
            "\nGold: {n[gold]}\nElectrum: {n[electrum]}\n" \
            "Platinum: {n[platinum]}".format(n=self._amount)
            
    def add(self, other: 'Money'):
        '''Add another money object to the caller, merging them.
        
        All coins of the Money object added WILL BE SET TO ZERO.
        >>> m1 = Money({'copper': 50, 'silver': 5})
        >>> m2 = Money({'silver': 10, 'gold': 3})
        >>> m1.add(m2)
        >>> print(m1)
        Money:
        Copper: 50
        Silver: 15
        Gold: 3
        Electrum: 0
        Platinum: 0
        >>> print(m2)
        Money:
        Copper: 0
        Silver: 0
        Gold: 0
        Electrum: 0
        Platinum: 0
        '''
        for coin in DD_CURRENCIES:
            self._amount[coin] += other.get_coins()[coin]
            other._amount[coin] = 0
            
    
    def get_coins(self, coin: str = None):
        '''Returns a dict with the amounts of all or specified typer of coins.
        
        If no coin is specified, it returns a dict with all coins and relative
        amounts. Otherwise, it returns the number of the specified coin.
        >>> m = Money({'copper': 20, 'silver': 2, 'gold': 1})
        >>> m.get_coins() == m._amount
        True
        >>> m.get_coins('silver')
        2
        '''
        if not coin:
            return dict(self._amount)
        
        return self._amount[coin]
    
    def get_value(self):
        '''Return the overall value of all coins in gold coins.
        
        TODO TEST
        '''
        pass        
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
        