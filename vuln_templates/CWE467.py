#TODO Impliment

def apply_constraint(state, expr, init_val, **kwargs):
    return


def specify_sinks():
    maps = {'sizeof': ['n']}
    return maps


def specify_sources():
    checkpoints = {}
    return checkpoints


def save_results(reports):
    for r in reports:
        with open(f"ArbiterReport_{hex(r.bbl)}", "w") as f:
            f.write("\n".join(str(x) for x in r.bbl_history))