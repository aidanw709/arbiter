import json
SYSCALL_TABLE = "syscalls_annotated.json"

"""
CWE-467: Use of Inherently Dangerous Function

This template tracks for null ptrs being passed as arguments which could lead to derefernece of a null ptr. 

"""
def apply_constraint(state, expr, init_val, **kwargs):
    if expr.value is None:
        return 
    return

def parse_syscalls(syscall_table, return_filter=None):
    maps = {}
    checkpoints = {}
    syscalls = {}

    with open(syscall_table) as f:
        syscalls = json.load(f)

    for syscall, s_info in syscalls.items():
        ret = s_info['ret']
        if not ret:
            continue
        if return_filter != None:
            values = ret['values']
            if str(return_filter) not in values or values[str(return_filter)] != 'error':
                continue
        print(f"syscall: {syscall}")
        maps[syscall] = ['r']
        checkpoints[syscall] = 0

    return maps, checkpoints

def specify_sinks():
    maps, _ = parse_syscalls(SYSCALL_TABLE, return_filter=-1)
    return maps


def specify_sources():
    return {}


def save_results(reports):
    for r in reports:
        with open(f"ArbiterReport_{hex(r.bbl)}", "w") as f:
            f.write("\n".join(str(x) for x in r.bbl_history))