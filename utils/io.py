import json
from models import Case

def save_case(path: str, case: Case):
    with open(path, "w") as f:
        json.dump(case.model_dump(), f, indent=4)


def print_case_line(case: Case):
    victim = case.suspects[case.solution.victimID].name
    culprit = case.suspects[case.solution.culpritID].name
    weapon = case.solution.weapon.name
    motive = case.solution.motive.name

    print(f"{culprit} killed {victim} with {weapon} for {motive}")