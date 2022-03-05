from signal_backtester.base.base_backtester import (
    BackTestingBackTest,
    BackTestingDataset,
)
from signal_backtester.core.picker import STRATEGIES
from signal_backtester.schemas.models import InputValidatorBase
from signal_backtester.core.operations import prepare_data
import pandas as pd


class SignalBacktester:
    """Signal Baktester moudle
        it uses Backtesting Lib (https://kernc.github.io/backtesting.py/)
        you must have this columns in your dataset
            - Date          (timestamp is prefered)
            - Open
            - High
            - Low
            - Close
            - Volume
            - signal        (1 for sell signal)(2 for buy signal)
        
    
    """

    def __init__(
        self,
        dataset,
        strategy,
        cash,
        commission,
        percent_of_portfolio,
        data_name="data",
        stop_loss=None,
        take_profit=None,
        trailing_stop=None,
        time_frame="5m",
        output_path=".",
    ):
        # validate input fields with a pydantic model
        self.fields = InputValidatorBase(
            cash=cash,
            commission=commission,
            stop_loss=stop_loss,
            take_profit=take_profit,
            trailing_stop=trailing_stop,
            percent_of_portfolio=percent_of_portfolio,
            dataset=dataset,
            strategy=strategy,
            time_frame=time_frame,
        )
        self.data_name = data_name
        self.out_path = output_path

    def read_dataset(self):
        return pd.read_csv(self.fields.dataset)

    def run(self):
        # read dataset and prepare data for backtesting lib
        dataframe = self.read_dataset()
        dataframe = prepare_data(self.fields.time_frame, dataframe)

        # define signal column as an indicator
        def SIGNAL():
            return dataframe.signal

        params = {
            "stop_loss": self.fields.stop_loss,
            "take_profit": self.fields.take_profit,
            "stop_trailing_amount": self.fields.trailing_stop,
            "indicator": SIGNAL,
            "order_report_path": f"{self.out_path}/order_report.csv",
            "percent_of_portfolio": self.fields.percent_of_portfolio,
        }

        datasets = [
            BackTestingDataset(self.data_name, dataframe),
        ]

        backtest = BackTestingBackTest(
            datasets,
            strategy=STRATEGIES.get(self.fields.strategy),
            cash=self.fields.cash,
            commission=self.fields.commission,
            exclusive_orders=True,
            trade_on_close=False,
        )
        
        # final csv report
        report = backtest.run(params=params)
        report_path = f"{self.out_path}/final_report.csv"
        report.to_csv(report_path)
        
        # final html report
        backtest.plot(
            filename=f"{self.out_path}/final_report.html",
            plot_equity=True,
            plot_return=True,
            plot_pl=True,
            plot_volume=True,
            plot_drawdown=True,
            smooth_equity=True,
            relative_equity=True,
            superimpose=True,
            resample=True,
            reverse_indicators=False,
            show_legend=True,
            open_browser=False,
        )
