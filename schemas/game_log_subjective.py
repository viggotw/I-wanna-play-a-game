from pydantic import BaseModel, Field
from typing import List, Literal, Optional

class GameLogIndividual(BaseModel):
    ''' Model used between tournament and every unique contestant '''
    score: int
    previous_result: Literal['win', 'lose', 'draw', None]
    previous_moves: List[object]

class GameLogSubjective(BaseModel):
    ''' Model used between tournament and every unique contestant '''
    me: GameLogIndividual
    opponents: List[GameLogIndividual]