import talib # notice you can install talib manually
import pandas as pd

def cross_EMA_signals(df, fast_period, slow_period):
    """_summary_

    Args:
        df (_type_): _description_
        fast_period (_type_): _description_
        slow_period (_type_): _description_
    """
    signal = [0] * len(df)
    
    df['fast'] = talib.EMA(df.Close, timeperiod=fast_period)
    df['slow'] = talib.EMA(df.Close, timeperiod=slow_period)
    for idx in range(len(df)):
        if idx > slow_period:
            
            if df.iloc[idx - 1].fast < df.iloc[idx - 1].slow and df.iloc[idx].fast > df.iloc[idx].slow:
                # buy signal
                signal[idx] = 2
                
            if df.iloc[idx - 1].fast > df.iloc[idx - 1].slow and df.iloc[idx].fast < df.iloc[idx].slow:
                # sell signal
                signal[idx] = 1
    
    df['signal'] = signal
    df.to_csv('./final_dataset.csv')


df = pd.read_csv('./data.csv')

if __name__ == "__main__":
    cross_EMA_signals(df, 15, 30)