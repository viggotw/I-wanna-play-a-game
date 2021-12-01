from pydantic import BaseModel, Field
from typing import List, Optional

class GameLogGlobalContestant(BaseModel):
    ''' Model used in tournament, containing game stats for a single contestant '''
    num_matches: int = 0
    score: int = 0
    wins: int = 0
    draw: int = 0
    loss: int = 0

class GameLogGlobal(BaseModel):
    ''' Model used in tournament, containing game stats for all contestants '''
    contestants: List[GameLogGlobalContestant]
    