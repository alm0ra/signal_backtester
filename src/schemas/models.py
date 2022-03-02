from pydantic import BaseModel, Field, root_validator
from typing import Union
from typing_extensions import Literal

class InputValidatorBase(BaseModel):
    cash: int = Field(gt=0)
    commission : float = Field(gt=0, lt=0.1)
    stoploss: float = Field(gt=0)
    take_profit: float = Field(gt=0)
    trailing_stop: float = Field(gt=0)
    percent_of_portfolio: int = Field(gt=0, lt=100)
    strategy_name:str
    title:str
    description:str
    dataset:str
    time_frame : Union[
        Literal["1m"],
        Literal["5m"],
        Literal["15m"],
        Literal["30m"],
        Literal["45m"],
        Literal["1h"],
        Literal["2h"],
        Literal["3h"],
        Literal["4h"],
        Literal["8h"],
        Literal["1d"],
        Literal["2d"],
        Literal["4d"],
        Literal["8d"],
        Literal["1w"],
        Literal["2w"],
        Literal["1M"],
    ]
    @root_validator(pre=True)
    def do_validation(cls, values):
        # TODO do validation of dataset feild
        # TODO check if dataset exist
        # TODO read dataset and check if has this columns 
        # Date Open High Low Close Volume Signal
        pass