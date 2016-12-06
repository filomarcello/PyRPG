""" created 07/11/2016
author: marcello
version: 0.1

constants in package items
"""

# money and precious
COIN_WEIGHT = 0.02 # a coin weights 20 grams (0.02 Kilos)
GEM_WEIGHT = 0.04 # a gem weights 40 grams (0.040 Kilos)

DD_CURRENCIES = ('platinum', 'gold', 'electrum', 'silver', 'copper')

# value is in gold coins
# platinum = 5    gold
# gold     = 1    gold
# electrum = 0.5  gold
# silver   = 0.1  gold
# copper   = 0.01 gold
CURRENCIES_EXCHANGE = (5, 1, 0.5, 0.1, 0.01)

DD_CURRENCY_EXCHANGE = {c: e for c, e in
                        zip(DD_CURRENCIES, [5, 1, 0.5, 0.1, 0.01])}