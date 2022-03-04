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
        plt = [dataset.backtest.plot(**kwargs) for dataset in self.datasets]
        return True

    def optimize(self, **kwargs):
        optimize_args = {"return_heatmap": True, **kwargs}
        heatmaps = []

        for dataset in self.datasets:
            _best_stats, heatmap = dataset.backtest.optimize(**optimize_args)
            heatmaps.append(heatmap)

        return pd.DataFrame(heatmaps)
