from signal_backtester import SignalBacktester


dataset_address = "./sample_dataset.csv"

backtest = SignalBacktester(
    dataset=dataset_address,
    strategy="two_side_sl_tp_reversed",
    cash=1000,
    commission=0.0005,
    percent_of_portfolio=99,
    stop_loss=1,
    take_profit=10,
    trailing_stop=3,
    time_frame="30m",
)

backtest.run()
