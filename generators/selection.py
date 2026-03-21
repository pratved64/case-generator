from random import Random
    
def weighted_pick(pool: list, rng: Random, weights: list[int] = []):
    if not weights:
        weights = [x.weight for x in pool]
    return rng.choices(pool, weights=weights)[0]