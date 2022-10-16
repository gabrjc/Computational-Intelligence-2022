

import random

def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]




import logging


def greedy(N,l):
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


def longest_first(N,l):
    
    goal = set(range(N))
    covered = set()
    solution = list()
    all_lists = sorted(l, key=lambda l: -len(l))
    while goal != covered:
        x = all_lists.pop(0)
        if not set(x) < covered:
            solution.append(x)
            covered |= set(x)

    #print("Bigger First : ", solution)
    logging.info(
        f"Longest first solution for N={N}: w={sum(len(_) for _ in solution)} (bloat={(sum(len(_) for _ in solution)-N)/N*100:.0f}%)"
    )
    logging.debug(f"{solution}")
    

def mixed(N,l):
    
    goal = set(range(N))
    covered = set()
    solution = list()
    all_lists = sorted(l, key=lambda l: len(l))

    while goal != covered:
        if(covered.__len__()/goal.__len__()<0.70):
            x = all_lists.pop(0)
        else:
            x= all_lists.pop()
        
        if not set(x) < covered:
            solution.append(x)
            covered |= set(x)

    #print("Bigger First : ", solution)
    logging.info(
        f"Mixed solution for N={N}: w={sum(len(_) for _ in solution)} (bloat={(sum(len(_) for _ in solution)-N)/N*100:.0f}%)"
    )
    logging.debug(f"{solution}")


def alternate(N,l):
    
    goal = set(range(N))
    covered = set()
    solution = list()
    all_lists = sorted(l, key=lambda l: len(l))
    alt=0
    while goal != covered:
        if(alt==0):
            x = all_lists.pop(0)
            alt=1
        else:
            x= all_lists.pop()
            alt=0
        
        if not set(x) < covered:
            solution.append(x)
            covered |= set(x)
    logging.info(
        f"Alternate solution for N={N}: w={sum(len(_) for _ in solution)} (bloat={(sum(len(_) for _ in solution)-N)/N*100:.0f}%)"
    )
    logging.debug(f"{solution}")





if __name__=="__main__":
    logging.getLogger().setLevel(logging.INFO)
    
    for N in [5, 10, 20, 100, 500, 1000]:
        l = problem(N,42)
        greedy(N,l)
        longest_first(N,l)
        mixed(N,l)
        alternate(N,l)
        print("")
        print("")
