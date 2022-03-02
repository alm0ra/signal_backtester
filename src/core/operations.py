import datetime

def time_format_picker(timeframe):
    time_dict = {
        '1d': "%Y-%m-%d",
        '4h': "%Y-%m-%d %H:%M",
        '1h': "%Y-%m-%d %H:%M",
        '30m': "%Y-%m-%d %H:%M",
        '15m': "%Y-%m-%d %H:%M",
        '5m': "%Y-%m-%d %H:%M",
        '1m': "%Y-%m-%d %H:%M",
    }
    return time_dict.get(timeframe, None)


def timestamp_changer(ts, time_format):
    return datetime.datetime.fromtimestamp((ts // 1000)).strftime(time_format)