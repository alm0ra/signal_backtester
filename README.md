![Alt text](logo.png)
![GitHub top language](https://img.shields.io/github/languages/top/xibalbas/signal_backtester)
![GitHub repo size](https://img.shields.io/github/repo-size/xibalbas/signal_backtester)
![PyPI](https://img.shields.io/pypi/v/signal-backtester)

# Signal Backtester
 a small repo Based on  [Backtesting](https://pypi.org/project/Backtesting/) Lib .  
 easiest way to backtest your generated signal

# Quick Start



## installation
```bash
pip install signal-backtester
```

## Usage
```python
from signal_backtester import SignalBacktester

# address of your dataset file 
# columns should include "Open, High, Low, Close, Volume, signal"

backtest = SignalBacktester(
                dataset="/home/xibalbas/sample.csv",
                strategy='two_side_sl_tp_reversed',
                cash=1000,
                commission=0.0005,  # equal 0.05 %
                percent_of_portfolio=99,
                stop_loss=1,
                take_profit=10,
                trailing_stop=3,    # if you are using trailing stop
                time_frame='30m', 
                output_path='.'     # path of result files
            )

backtest.run()
```

# strategy

available strategy to use are :

- `two_side_sl_tp_reversed`
- `two_side_sl_trailing_reversed`
- `one_side_buy_sl_tp`
- `one_side_sell_sl_tp`
- `one_side_buy_sl_trailing`
- `one_side_sell_sl_trailing`


# dataset structure
your data set structure should be like this table 

your buy signals should generate as 2
and your sell signals should generate as 1


you must have this columns in your dataset 
- Date
- Open
- High
- Low
- Close
- Volume
- signal

![Alt text](sample_dataset.png)