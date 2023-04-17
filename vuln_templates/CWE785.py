

def apply_constraint(state, expr, init_val, **kwargs):
    if expr.size() != 2080:
        state.solver.add(expr==0)
    return


def specify_sinks():
    maps = {'PathAppend': ['n','c']}
    return maps


def specify_sources():
    return {}


def save_results(reports):
    for r in reports:
        with open(f"ArbiterReport_{hex(r.bbl)}", "w") as f:
            f.write("\n".join(str(x) for x in r.bbl_history))