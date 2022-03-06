from backtesting import Strategy
from abc import abstractmethod
import pandas as pd


class BacktestingBaseStrategy(Strategy):
    """
    Base Strategy class
        it prepare a final report of orders by 'save_trades' module
            a csv report contain of some information of each trade
            will prepare here
        also it determines when strategy stops and how many candle
         pass from next() function
    """

    def init(self):
        super().init()
        self.order_csv_report = None
        self.dataframe_count = len(self.data)

    def save_trades(self, closed_trades):
        # make a dataframe
        self.order_csv_report = pd.DataFrame(
            columns=[
                "entry_price",
                "entry_time",
                "exit_price",
                "exit_time",
                "side",
                "pl",
                "pl_pct",
                "size",
                "value",
                "status",
            ]
        )
        # append information od each trades
        for trade in closed_trades:
            pl_pct = trade.pl_pct * 100
            pl_pct_round = round(pl_pct, 2)
            order_report = {
                "entry_price": trade.entry_price,
                "entry_time": trade.entry_time,
                "exit_price": trade.exit_price,
                "exit_time": trade.exit_time,
                "pl": trade.pl,
                "pl_pct": str(pl_pct_round) + " %",
                "size": trade.size,
                "value": trade.value,
            }
            if trade.is_long:
                order_report["side"] = "BUY"
            if trade.is_short:
                order_report["side"] = "SELL"

            if trade.tp == trade.exit_price:
                order_report["status"] = "TP trigger"
            elif trade.sl == trade.exit_price:
                order_report["status"] = "SL trigger"
            else:
                order_report["status"] = "closed"

            self.order_csv_report = self.order_csv_report.append(
                order_report, ignore_index=True
            )
        # make an out put
        self.order_csv_report.to_csv(self.order_report_path, index=False)

    def next(self):
        super().next()
        if self.data._Data__i > self.dataframe_count - 1:
            self.stop()

    @abstractmethod
    def stop(self):
        # this method call when backtest is finished
        pass
