from models_tools.models import Card


def comb5_to_strkey(comb5: list[Card | Card]) -> str:
    if len(set(comb5)) != 5:
        raise Exception(f"Incorrect comb5 input {comb5} ")
    rank_list = [card.rank for card in comb5]
    suit_list = [card.suit for card in comb5]
    flush = 'fl' if len(set(suit_list)) == 1 else 'unfl'
    return ','.join(map(str, sorted(rank_list))) + '_' + flush