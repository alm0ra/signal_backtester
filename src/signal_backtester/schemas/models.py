from pydantic import BaseModel, Field, root_validator
from typing import Union
from typing_extensions import Literal
import pandas as pd



class InputValidatorBase(BaseModel):
    cash: int = Field(gt=0)
    commission: float = Field(gt=0, lt=0.1)
    stop_loss: float = Field(gt=0)
    take_profit: float = Field(gt=0)
    trailing_stop: float = Field(gt=0)
    percent_of_portfolio: int = Field(gt=0, lt=100)
    dataset: str
    strategy: Union[
        Literal["two_side_sl_tp_reversed"],
        Literal["two_side_sl_trailing_reversed"],
        Literal["one_side_sell_sl_tp"],
        Literal["one_side_buy_sl_tp"],
        Literal["one_side_buy_sl_trailing"],
        Literal["one_side_sell_sl_trailing"],
    ]

    time_frame: Union[
        Literal["1m"],
        Literal["5m"],
        Literal["15m"],
        Literal["30m"],
        Literal["1h"],
        Literal["4h"],
        Literal["1d"],
    ]

    @root_validator(pre=True)
    def do_validation(cls, values):
        try:
            df = pd.read_csv(values["dataset"])
            
            available_columns = ["Date","Open","High","Low","Close","Volume","signal"]
            
            for column in available_columns:
                if column not in df.columns:
                    raise ValueError(f"[dataset must contain {column} column]")

        except FileNotFoundError:
            raise ValueError("[dataset] file Does not exist")

        return values
