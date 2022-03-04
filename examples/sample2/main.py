from signal_backtester import SignalBacktester



dataset_address = "./final_dataset.csv"

backtest = SignalBacktester(dataset=dataset_address,
                            strategy='two_side_sl_tp_reversed',
                            cash=100000,
                            commission=0.0005,
                            percent_of_portfolio=99,
                            stop_loss=1,
                            take_profit=2,
                            trailing_stop=3,
                            output_path='./result'     # path of result files
                            )

backtest.run()
