"""
CWE-242: Use of Inherently Dangerous Function

This template tracks the usage of functions that are considered dangerous regardless
of how they are used and should not be used in code. Using these functions opens a binary
to potential exploitation, mainly via stack overflows.

"""

def apply_constraint(state, expr, init_val, **kwargs):
    addr = state.solver.eval(expr, cast_to=int)
    if state.project.loader.find_section_containing(addr) is not None:
        # Force an unsat error
        state.solver.add(expr==0)
    return


def specify_sinks():
    maps = {'gets': ['n'],
            'atoi': ['n'],
            'atol': ['n'],
            'atoll': ['n'],
            'atof': ['n'],
            'strcat': ['c', 'n'],
            'strcpy': ['c', 'n'],
            'sprintf': ['c', 'n']
            }
    return maps


def specify_sources():
    return {}


def save_results(reports):
    for r in reports:
        with open(f"ArbiterReport_{hex(r.bbl)}", "w") as f:
            f.write("\n".join(str(x) for x in r.bbl_history))
