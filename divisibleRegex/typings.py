from typing import Set, List, Dict, Tuple

AlphabetT = Set[str]
StatesT = List[str]
InitialT = str
FinalsT = Set[str]
TransitionsT = Dict[str, Dict[str, str]]
FsmT = Tuple[AlphabetT, StatesT, InitialT, FinalsT, TransitionsT, TransitionsT]
