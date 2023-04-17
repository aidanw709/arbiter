def apply_constraint(state, expr, init_val, **kwargs):
    state.solver.add(expr==0)
    return


def specify_sinks():
    maps = {'getlogin': ['n']}
    return maps


def specify_sources():
    checkpoints = {'fork': 0,
                    'Fork': 0,
                    'vfork': 0}
    return checkpoints


def save_results(reports):
    for r in reports:
        with open(f"ArbiterReport_{hex(r.bbl)}", "w") as f:
            f.write("\n".join(str(x) for x in r.bbl_history))