from classification.comb5_classification import find_comb5_fig
from rnd_tests.rnd_combs import rnd_comb5

AMOUNT_TESTS = 100
for i in range(AMOUNT_TESTS):
    comb5= rnd_comb5()
    comb5_name, comb5_id = find_comb5_fig(comb5)
    comb5_str =','.join(map(lambda card: str(card.rank) + card.suit, comb5))
    print(f'Comb5: {comb5_str}, comb name: {comb5_name}, comb id: {comb5_id}')
