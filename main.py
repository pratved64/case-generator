from random import Random
from models import Case
from generators.case import generate_case
from generators.schedule import generate_schedule, subset_rooms
from utils.resolvers import resolve_by_id
from utils.io import save_case, print_case_line

from models import load_config

def main():
    config = load_config("./data/data.json")
    rng = Random(config.seed)

    suspects, solution = generate_case(config, rng)
    selected_rooms = subset_rooms(config, 5, rng)
    case = Case(suspects=suspects, solution=solution, rooms=selected_rooms, slot_count=config.slot_count)
    
    for suspect in case.suspects:
        suspect.schedule = generate_schedule(suspect, selected_rooms, config, rng)
        
    

    resolved_case = resolve_by_id(config, case)
    save_case("output/case.json", resolved_case)
    print_case_line(resolved_case)


if __name__ == "__main__":
    main()