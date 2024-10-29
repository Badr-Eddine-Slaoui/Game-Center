"""
    This file contain all the custom types for all the games
"""


from typing import List, Tuple, Dict

#Global types
Option = Tuple[str,str,str]
Score = Dict[str,int]
Nums = List[int]
Strs = List[str]

#Dice Roller types
Dice = Tuple[str,str,str,str,str]

#Tic Tac Toe types
Screen = list[str]
Spots = Dict[int,list[int]]