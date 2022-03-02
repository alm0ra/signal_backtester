from src.base.base_backtester import BackTestingBackTest, BackTestingDataset
from src.core.picker import STRATEGIES
from schemas.models import InputValidatorBase
import pandas as pd


class SignalBacktester:
    """Backtest of signals 
    
    """
    def __init__(self, dataset, strategy, cash, commission, percent_of_portfolio, data_name='data', stop_loss=None, take_profit=None,
               trailing_stop=None, time_frame='5m'):
        
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
    
    def read_dataset(self):
        return pd.read_csv(self.fields.dataset)
    
    def run(self):
        
        dataframe = self.read_dataset()
        
        def SIGNAL():
            return dataframe.signal

        params = {
            'stop_loss': self.fields.stop_loss,
            'take_profit': self.fields.take_profit,
            'stop_trailing_amount': self.fields.trailing_stop,
            'indicator': SIGNAL,
            'order_report_path': './order_report.csv',
            'percent_of_portfolio': self.fields.percent_of_portfolio,
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

        report = backtest.run(params=params)
        report_path ='./final_report.csv'
        report.to_csv(report_path)

        backtest.plot(
            filename='./final_report.html',
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
            open_browser=False
        )

