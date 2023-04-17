#Incomplete as it is unable to be implimented in arbiter. I didn't realize till 
#some work had been completed that sizeof is not a function. 

def apply_constraint(state, expr, init_val, **kwargs):
    return


def specify_sinks():
    return {'sizeof': ['n']}


def specify_sources():
    return {}


def save_results(reports):
    for r in reports:
        with open(f"ArbiterReport_{hex(r.bbl)}", "w") as f:
            f.write("\n".join(str(x) for x in r.bbl_history))