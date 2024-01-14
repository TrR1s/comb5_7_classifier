from collections import namedtuple
from enum import Enum
from pckle_tools.pickle_load import load_pickle


path_to_comb_5_dict = str(f"../comb_5_dict.pickle")
comb_5_dict = load_pickle(path_to_comb_5_dict)

Card = namedtuple('Card', ['rank', 'suit'])
suits = ['h', 'c', 'd', 's']
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
class CombType(str, Enum):
    ROYAL_FLUSH = "ROYAL_FLUSH"
    STRAIGHT_FLUSH = 'STRAIGHT_FLUSH'
    FOUR_OF_KIND = 'FOUR_OF_KIND'
    FULL_HOUSE = 'FULL_HOUSE'
    FLUSH = 'FLUSH'
    STRAIGHT = 'STRAIGHT'
    THREE_OF_KIND = 'THREE_OF_KIND'
    TWO_PAIRS = 'TWO_PAIRS'
    ONE_PAIR = 'ONE_PAIR'
    ACE_KING = 'ACE_KING'
    HIGH_CARD = 'HIGH_CARD'


