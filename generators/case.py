from random import Random
from faker import Faker
from models import *
from generators.selection import weighted_pick

def affinity_weight(config: GeneratorConfig, suspect: Suspect, M: float = 12.0):
    adjusted = [x.weight for x in config.motive_pool]
    aff = []
    for motive in config.motive_pool:
        diff_ls = list(set(motive.traits_affinity) - set(suspect.traits))
        score = 1 - (len(diff_ls) / len(motive.traits_affinity))
        mul = 1 + (score * (M - 1))
        aff.append(mul * motive.weight)
        print(f"Traits Matching: {score:0.2f} | Multiplier: {mul:0.2f} | Updated Weight: {mul * motive.weight:0.2f}")  
    
    return aff


def generate_case(config: GeneratorConfig, rng: Random) -> tuple[list[Suspect], Solution]:
    suspects = []
    fake = Faker()
    for i in range(config.suspect_count):
        
        num_traits = rng.randint(1, 3)
        selected_traits = [x.id for x in rng.sample(config.trait_pool, num_traits)]
        
        num_secrets = rng.randint(1, 3)
        selected_secrets = [x.id for x in rng.sample(config.secret_pool, num_secrets)]
        
        suspects.append(Suspect(id=i, name=fake.name(), traits=selected_traits, secrets=selected_secrets))
    
    selected_victim, selected_culprit = rng.sample(range(0, config.suspect_count), 2)

    updated_weights = affinity_weight(config, suspects[selected_culprit])
    selected_motive = weighted_pick(config.motive_pool, rng, weights=updated_weights)
    suspects[selected_culprit].motive = selected_motive
    
    # DEBUG SECTION
    # max_idx = updated_weights.index(max(updated_weights))
    # if selected_motive == config.motive_pool[max_idx]:
    #     count += 1
    #     print("Selected top motive")
    # else:
    #     print("Selected motive:", config.motive_pool.index(selected_motive))
    
    selected_weapon = weighted_pick(config.weapon_pool, rng)
    sol = Solution(culpritID=selected_culprit, victimID=selected_victim, motive=selected_motive, weapon=selected_weapon)
    
    return suspects, sol
