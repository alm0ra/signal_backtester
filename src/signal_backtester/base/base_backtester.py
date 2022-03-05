from backtesting import Backtest
import pandas as pd


class BackTestingDataset:
    name = None
    data = None
    backtest = None

    def __init__(self, name, data):
        self.name = name
        self.data = data


class BackTestingBackTest:
    """
        Backtesting class
            written for backtest several dataset on a strategy
            it run engine of backtest on datasets and return a plot
            also you can optimize your strategy.
    """
    datasets = []

    def __init__(self, datasets, strategy, **kwargs):
        for dataset in datasets:
            dataset.backtest = Backtest(dataset.data, strategy=strategy, **kwargs)
        self.datasets = datasets

    def run(self, **kwargs):
        results = [dataset.backtest.run(**kwargs) for dataset in self.datasets]
        dataframe_results = pd.DataFrame(results).transpose()
        return dataframe_results

    def plot(self, **kwargs):
        # plot result with backtesing plot module
        plt = [dataset.backtest.plot(**kwargs) for dataset in self.datasets]
        return True

    def optimize(self, **kwargs):
        """
            optimization module
                for optimizing your strategy and get best result and 
                best config
        """
        optimize_args = {"return_heatmap": True, **kwargs}
        heatmaps = []

        for dataset in self.datasets:
            _best_stats, heatmap = dataset.backtest.optimize(**optimize_args)
            heatmaps.append(heatmap)

        return pd.DataFrame(heatmaps)
