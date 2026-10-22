from scipy.stats import binom, geom

# Free throws: n = 10 shots, p = 0.7
print(round(binom.pmf(7, 10, 0.7), 4))      # P(X = 7)
print(round(binom.sf(7, 10, 0.7), 4))       # P(X > 7), that is, P(X >= 8)
print(binom.mean(10, 0.7), round(binom.std(10, 0.7), 3))

# Rare cards: p = 1/8 per pack
print(round(geom.pmf(3, 0.125), 4))         # first rare card in pack 3
print(round(geom.sf(10, 0.125), 4))         # P(X > 10): none in 10 packs
print(geom.mean(0.125), round(geom.std(0.125), 2))
