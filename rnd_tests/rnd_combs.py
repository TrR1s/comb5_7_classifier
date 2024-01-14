from models_tools.models import Card, suits, ranks
import random


def rnd_card() -> Card:
    rnd_suit = random.choice(suits)
    rnd_rank = random.choice(ranks)
    return Card(rnd_rank,rnd_suit)

def rnd_comb5() -> list[Card|Card]:
    comb5=[]
    while(len(comb5) != 5):
        curr_card = rnd_card()
        if curr_card not in comb5:
            comb5.append(curr_card)
    return comb5

def rnd_comb7() -> list[Card|Card]:
    comb7=[]
    while(len(comb7) != 7):
        curr_card = rnd_card()
        if curr_card not in comb7:
            comb7.append(curr_card)
    return comb7
