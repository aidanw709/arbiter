"""
CWE-1341: Multiple Releases of Same Resource or Handle

This template tracks the usage of sockets that are closed twice

"""
ids = []

def apply_constraint(state, expr, init_val, **kwargs):
    s = state.copy()
    socket_id = s.solver.eval(expr, cast_to=int)
    if socket_id in ids:
        state.solver.add(False)
    ids.append(socket_id)
    return


def specify_sinks():
    maps = {'close': ['n']}
    return maps


def specify_sources():
    return {'accept': 0, 'socket': 0}


def save_results(reports):
    for r in reports:
        with open(f"ArbiterReport_{hex(r.bbl)}", "w") as f:
            f.write("\n".join(str(x) for x in r.bbl_history))
