from classification.comb7_classification import find_best_comb5_in_comb7
from rnd_tests.rnd_combs import rnd_comb7

AMOUNT_TESTS = 100
for i in range(AMOUNT_TESTS):
    comb7= rnd_comb7()
    comb5_name, comb5_id, comb5 = find_best_comb5_in_comb7(comb7)
    comb7_str =','.join(map(lambda card: str(card.rank) + card.suit, comb7))
    comb5_str =','.join(map(lambda card: str(card.rank) + card.suit, comb5))
    print(f'Comb7: {comb7_str} \n best comb5: {comb5_str}, comb name: {comb5_name}, comb id: {comb5_id}')
