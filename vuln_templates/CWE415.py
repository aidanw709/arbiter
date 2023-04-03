"""
CWE-415: Double Free

This template tracks the usage of pointers that have been double freed

"""
ptrs = []

def apply_constraint(state, expr, init_val, **kwargs):
    s = state.copy()
    input_ptr = s.solver.eval(expr, cast_to=int)
    if input_ptr in ptrs:
        state.solver.add(False)
    ptrs.append(input_ptr)
    return


def specify_sinks():
    maps = {'free': ['n']}
    return maps


def specify_sources():
    return {'malloc': 0, 'calloc': 0, 'realloc': 0}


def save_results(reports):
    for r in reports:
        with open(f"ArbiterReport_{hex(r.bbl)}", "w") as f:
            f.write("\n".join(str(x) for x in r.bbl_history))
