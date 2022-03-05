import talib  # notice you can install talib manually
import pandas as pd


def cross_EMA_signals(df, fast_period, slow_period):
    # generate a zero list for signals and we turn it to 1 if we had
    # a sell signal also we turn it to 2 if we had buy signal
    signal = [0] * len(df)

    # calculate fast and slow of exp moving average
    df["fast"] = talib.EMA(df.Close, timeperiod=fast_period)
    df["slow"] = talib.EMA(df.Close, timeperiod=slow_period)
    
    # loop on dataframe and looking for signals
    for idx in range(len(df)):
        if idx > slow_period:
            
            # Condition 1 (buy signal Cross EMA UP)
            if (
                df.iloc[idx - 1].fast < df.iloc[idx - 1].slow
                and df.iloc[idx].fast > df.iloc[idx].slow
            ):
                # buy signal (change signal amount )
                signal[idx] = 2

            
            # Condition 2 (sell signal Cross EMA DOWN)
            if (
                df.iloc[idx - 1].fast > df.iloc[idx - 1].slow
                and df.iloc[idx].fast < df.iloc[idx].slow
            ):
                # sell signal (change signal amount )
                signal[idx] = 1

    # save generated signal time frame
    df["signal"] = signal
    df.to_csv("./final_dataset.csv")



# run
df = pd.read_csv("./data.csv")

if __name__ == "__main__":
    cross_EMA_signals(df, 15, 30)
