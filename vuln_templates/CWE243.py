def apply_constraint(state, expr, init_val, **kwargs):
    if state.project.loader.find_symbol("chdir") is None:
        # Force an unsat error
        state.solver.add(expr==0)
    return


def specify_sinks():
    maps = {'fgets': ['n']}
    return maps


def specify_sources():
    checkpoints = {'chroot': 0}
    return checkpoints


def save_results(reports):
    for r in reports:
        with open(f"ArbiterReport_{hex(r.bbl)}", "w") as f:
            f.write("\n".join(str(x) for x in r.bbl_history))