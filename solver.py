from timeit import timeit
from time import time

def load(filename):
    """
    load sudoku from filename
    returns a sudoku
    """
    pass

def show(sudoku):
    """
    pretty prints the sudoku
    for example:
    _ _ _   3 _ 8   _ 7 _
    3 _ _   7 1 _   _ _ 4
    6 _ _   _ 4 _   _ _ _

    1 _ _   _ _ _   6 3 _
    2 _ 6   _ _ _   5 _ 8
    _ 5 3   _ _ _   _ _ 7

    _ _ _   _ 8 _   _ _ 1
    7 _ _   _ 6 4   _ _ 5
    _ 1 _   2 _ 7   _ _ _
    """
    pass

def candidates(sudoku, x, y):
    """
    returns a list of possibilities at x, y of sudoku
    i.e. [1,4,6] if the only possibilities left are 1, 4, and 6
    """
    pass

def solve_rule(sudoku):
    """
    solves the sudoku using a rule-based approach
    returns a solved sudoku
    """
    pass

def solve_dfs_it(sudoku):
    """
    solves the sudoku using an iterative DFS approach
    returns a solved sudoku
    """
    pass

def solve_dfs_rec(sudoku):
    """
    solves the sudoku using a recursive DFS approach
    returns a solved sudoku
    """
    pass

def solve_dfs_gen(sudoku):
    """
    solves the sudoku using an iterative DFS approach
        using Python generators]
    returns a solved sudoku
    """
    pass

def benchmark(filename):
    """
    time execution times of all solvers
    prints the time taken per run in ms
    """

    # all the to be timed solvers
    solvers = ["solve_rule", "solve_dfs_it", "solve_dfs_rec", "solve_dfs_gen"]

    # all imports required to run the code
    imports = ["load"] + solvers

    # setup code, to be run before every solve
    setup = f"from __main__ import {','.join(imports)}\n"\
          + f"sudoku = load(\"{filename}\")"

    # benchmark every solver
    for solver in solvers:
        number_of_trials = 0
        time_taken = 0
        time_limit = 2

        # benchmark for roughly time_limit seconds
        start = time()
        while time() - start < time_limit:
            time_taken += timeit(f"{solver}(sudoku)", setup = setup, number = 1)
            number_of_trials += 1

        print(f"{solver}: {time_taken * 1000 / number_of_trials:.{5}f}ms")

if __name__ == "__main__":
    #benchmark("easy/puzzle1.sudoku")
    pass
