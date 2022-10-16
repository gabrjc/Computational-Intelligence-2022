import logging
import random

def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]

def greedy(N,l):
    #made by Assignement
    goal = set(range(N))
    covered = set()
    solution = list()
    all_lists = sorted(l, key=lambda l: len(l))
    while goal != covered:
        x = all_lists.pop(0)
        if not set(x) < covered:
            solution.append(x)
            covered |= set(x)
    
    #print("Gready solution : ", solution)
    logging.info(
        f"Greedy solution for N={N}: w={sum(len(_) for _ in solution)} (bloat={(sum(len(_) for _ in solution)-N)/N*100:.0f}%)"
    )
    logging.debug(f"{solution}")
    print("")



def subset_len(N, sets):



    goal = set(range(0, N))
    all_list_sets = [set(x) for x in sets]

    
    all = set()
    for s in all_list_sets:
            for e in s:
                all.add(e)
    
    if all != goal:        
        print("Problem not resolvable")
        return None

    covered = set()
    solution = list()  
    while covered != goal:
        subset = max(all_list_sets, key=lambda s: len(s - covered)/len(s))
        solution.append(subset)
        covered |= subset
    
    logging.info(
        f"Subset_len solution for N={N}: w={sum(len(_) for _ in solution)} (bloat={(sum(len(_) for _ in solution)-N)/N*100:.0f}%)"
    )
    logging.debug(f"{solution}")
    print("")


def len_intersection_ratio(N, sets):

    goal = set(range(0, N))
    all_list_sets = [set(x) for x in sets]
    all = set()

    for s in all_list_sets:
            for e in s:
                all.add(e)
    
    if all != goal:
        print("Problem not resolvable")
        return None

    covered = set()
    solution = list()
    while covered != goal:
        subset = max(all_list_sets, key=lambda s: len(s - covered) / (len(s.intersection(covered))+1))
        solution.append(subset)
        covered |= subset
    
    logging.info(
        f"Len_intersection ratio solution for N={N}: w={sum(len(_) for _ in solution)} (bloat={(sum(len(_) for _ in solution)-N)/N*100:.0f}%)"
    )
    logging.debug(f"{solution}")
    print("")


if __name__=="__main__":
    logging.getLogger().setLevel(logging.INFO)
    A=[5, 10, 20, 100, 500, 1000, 2500, 5000]
    B=[10]
    
    for N in A:
        
        l = problem(N,42)
        greedy(N,l)
        subset_len(N,l)
        len_intersection_ratio(N,l)
        print("")
        print("")