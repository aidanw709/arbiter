"""
CWE-1341: Multiple Releases of Same Resource or Handle

This template tracks the usage of files that can be closed twice

"""
ids = []

def apply_constraint(state, expr, init_val, **kwargs):
    s = state.copy()
    file_id = s.solver.eval(expr, cast_to=int)
    if file_id in ids:
        state.solver.add(False)
    ids.append(file_id)
    return


def specify_sinks():
    maps = {'fclose': ['n']}
    return maps


def specify_sources():
    return {'fopen': 0}


def save_results(reports):
    for r in reports:
        with open(f"ArbiterReport_{hex(r.bbl)}", "w") as f:
            f.write("\n".join(str(x) for x in r.bbl_history))
