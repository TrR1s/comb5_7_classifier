from collections import namedtuple

from models_tools.models import Card, comb_5_dict
from models_tools.tools import comb5_to_strkey


def find_comb5_fig(comb5: list[Card | Card]) -> tuple:
    str_key = comb5_to_strkey(comb5)
    try:
        return comb_5_dict[str_key] # comb5_name, comb5_id
    except:
        raise Exception(f"Incorrect comb5 input {comb5} ")

