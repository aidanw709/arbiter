"""
CWE-789: Memory Allocation with Excessive Size Value

This template attempts to find cases where alloc functions are called and the user
has the ability to influence the value of these variables. This may allow a user to
exhaust memory resources by claiming significant amounts of space on the heap.
"""

import ipdb

def apply_constraint(state, expr, init_val, **kwargs):
    for x in init_val:
        if x.length > expr.length:
            continue
        if x.length < expr.length:
            x = x.zero_extend(expr.length-x.length)
        s1 = state.copy()
        s1.solver.add(expr > x)
        # Check whether we can actually increment the value
        if s1.satisfiable():
            # See if more than 4MB of space can be allocated
            state.solver.add(expr > 0x3D0900)
        else:
            # Unsat the whole thing
            state.solver.add(expr > x)
    return


def specify_sinks():
    maps = {'malloc': ['n'], 'calloc': ['c', 'n'], 'realloc': ['c', 'n'], 'calloc': ['n', 'c']}
    return maps


def specify_sources():
    return {}

def save_results(reports):
    for r in reports:
        with open(f"ArbiterReport_{hex(r.bbl)}", "w") as f:
            f.write("\n".join(str(x) for x in r.bbl_history))
