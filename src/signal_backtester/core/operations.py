import datetime
import pandas as pd


def time_format_picker(timeframe):
    """
    format of time for each time frame for
    changing time from timestamp
    """
    time_dict = {
        "1d": "%Y-%m-%d",
        "4h": "%Y-%m-%d %H:%M",
        "1h": "%Y-%m-%d %H:%M",
        "30m": "%Y-%m-%d %H:%M",
        "15m": "%Y-%m-%d %H:%M",
        "5m": "%Y-%m-%d %H:%M",
        "1m": "%Y-%m-%d %H:%M",
    }
    return time_dict.get(timeframe, None)


def timestamp_changer(ts, time_format):
    # change timestamp to time format
    return datetime.datetime.fromtimestamp((ts // 1000)).strftime(time_format)


def prepare_data(time_frame, data_frame_signal):
    # change format of Date from timestamp to usual mode
    time_format = time_format_picker(time_frame)
    data_frame_signal["Date"] = pd.to_datetime(
        [timestamp_changer(ts, time_format) for ts in data_frame_signal["Date"]]
    )
    # make Date column as index because Backtesting give Date as index
    data_frame_signal = data_frame_signal.set_index("Date")

    return data_frame_signal
