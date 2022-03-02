from src.base.base_backtester import BackTestingBackTest, BackTestingDataset
from src.core.picker import STRATEGIES


def backtester(dataframe, strategy, cash, commission, percent_of_portfolio,
               data_name='data', stop_loss=None, take_profit=None,
               trailing_stop=None):

    def SIGNAL():
        return dataframe.signal

    params = {
        'stop_loss': stop_loss,
        'take_profit': take_profit,
        'stop_trailing_amount': trailing_stop,
        'indicator': SIGNAL,
        'order_report_path': './order_report.csv',
        'percent_of_portfolio': percent_of_portfolio,
    }

    datasets = [
        BackTestingDataset(data_name, dataframe),
    ]

    backtest = BackTestingBackTest(
        datasets,
        strategy=STRATEGIES.get(strategy),
        cash=cash,
        commission=commission,
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
