from models import *

def get_trait(config: GeneratorConfig, id: int) -> Trait:
    for tr in config.trait_pool:
        if tr.id == id:
            return tr
    
    raise ValueError("ID not found in trait pool")

def get_secret(config: GeneratorConfig, id: int) -> Secret:
    for sc in config.secret_pool:
        if sc.id == id:
            return sc
    
    raise ValueError("ID not found in secret pool")


def resolve_by_id(config: GeneratorConfig, case: Case) -> Case:
    for suspect in case.suspects:
        # traits
        for i in range(len(suspect.traits)):
            updated = get_trait(config, suspect.traits[i])
            suspect.traits[i] = updated
            
        # secrets
        for i in range(len(suspect.secrets)):
            updated = get_secret(config, suspect.secrets[i])
            suspect.secrets[i] = updated
            
    for i in range(len(case.solution.motive.traits_affinity)):
        updated = get_trait(config, case.solution.motive.traits_affinity[i])
        case.solution.motive.traits_affinity[i] = updated
        
    return case 