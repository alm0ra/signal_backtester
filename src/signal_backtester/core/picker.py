from signal_backtester.strategies.one_sided import *
from signal_backtester.strategies.two_sided import *

STRATEGIES = {
    # two-sided strategies
    'two_side_sl_tp_reversed': TwoSidedSlTpReverse,

    # stop trailing
    'two_side_sl_trailing_reversed': TwoSidedSlTrailingReverse,


    # one-sided strategies
    'one_side_buy_sl_tp': BuyOneSidedSlTpCloseOpposite,
    'one_side_sell_sl_tp': SellOneSidedSlTpCloseOpposite,

    # stop-trailing
    'one_side_buy_sl_trailing': BuyOneSidedSlTrailingCloseOpposite,
    'one_side_sell_sl_trailing': SellOneSidedSlTrailingCloseOpposite,
}

