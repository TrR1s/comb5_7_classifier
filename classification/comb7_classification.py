from classification.comb5_classification import find_comb5_fig
import itertools
from models_tools.models import Card


def find_best_comb5_in_comb7(comb7: list[Card | Card]) -> tuple:
    if len(set(comb7)) != 7:
        raise Exception(f"Incorrect comb5 input {comb7} ")
    comb7_n = list(range(7))  # [0,1,2,3,4,5,6]
    comb5_frm_7_list = list(
        itertools.combinations(comb7_n, 5))  # [(0, 1, 2, 3, 4), (0, 1, 2, 3, 5), (0, 1, 2, 3, 6), (0, 1, 2, 4, 5),...

    best_comb5_id = -1
    best_comb_fig = ()
    for curr_comb5_n in comb5_frm_7_list:
        comb5 = [comb7[i] for i in curr_comb5_n]
        comb5_name, comb5_id = find_comb5_fig(comb5)
        if comb5_id>best_comb5_id:
            best_comb5_id = comb5_id
            best_comb_fig = (comb5_name,comb5_id,comb5)
    return best_comb_fig # comb5_name,comb5_id,comb5
