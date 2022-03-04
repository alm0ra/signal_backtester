from backtesting import Strategy
from abc import abstractmethod
import pandas as pd


class BacktestingBaseStrategy(Strategy):
    def init(self):
        super().init()
        self.order_csv_report = None
        self.dataframe_count = len(self.data)

    def log(self, txt):
        print(txt)

    def save_trades(self, closed_trades):

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
        for trade in closed_trades:
            pl_pct = trade.pl_pct * 100
            pl_pct_round = round(pl_pct, 2)
            dict = {
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
                dict["side"] = "BUY"
            if trade.is_short:
                dict["side"] = "SELL"

            if trade.tp == trade.exit_price:
                dict["status"] = "TP trigger"
            elif trade.sl == trade.exit_price:
                dict["status"] = "SL trigger"
            else:
                dict["status"] = "closed"

            self.order_csv_report = self.order_csv_report.append(
                dict, ignore_index=True
            )

        self.order_csv_report.to_csv(self.order_report_path, index=False)

    def next(self):
        super().next()
        if self.data._Data__i > self.dataframe_count - 1:
            self.stop()

    @abstractmethod
    def stop(self):
        pass
