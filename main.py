from random import Random
from models import Case
from generators.casegen import generate_case
from utils.resolvers import resolve_by_id
from utils.io import save_case, print_case_line

from models import load_config

def main():
    config = load_config("./data/data.json")
    rng = Random(config.seed)

    suspects, solution = generate_case(config, rng)
    case = Case(suspects=suspects, solution=solution)

    resolved_case = resolve_by_id(config, case)

    save_case("output/case.json", resolved_case)
    print_case_line(resolved_case)


if __name__ == "__main__":
    main()