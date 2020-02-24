import itertools
from collections import defaultdict
import sys

from GreedyPizza import greedy_pizza_yummy

pizza_slices = []

CONSTRAINT = 0

def parse_input(input_file):
    global pizza_slices
    global CONSTRAINT
    with open(input_file) as f:
        lines = f.readlines()
        CONSTRAINT, types = [int(s) for s in lines[0].split()]
        pizza_slices = [int(s) for s in lines[1].split()]


    # while min(pizza_slices) + current_slices <= constraint:



# def not_so_random_pizza(pizza_slices, costraint, target, attempts=69, previous_solution=[]):
#     raise NotImplementedError
#     best_solution = (previous_solution,sum(previous_solution))
#     for attempts in range(attempts):
#         if
#  def correct_pizza():
#      return correct_pizza_slices


def pizza_cutter_solver(pizzas, constraint, scaling_factor = 4):
    constraint = int(constraint/scaling_factor)
    pizzas = list(map(lambda x: round(x / scaling_factor), pizzas))
    print(pizzas, constraint)
    return pizza_solver(pizzas, constraint)

def pizza_solver(pizzas, constraint):

    def optimum(k, slice_limit):
        if k < 0:
            return 0

        if V[k, slice_limit] == -1:
            without_curr = optimum(k-1, slice_limit)
            with_curr = (0 if slice_limit < pizzas[k] else optimum(k-1, slice_limit - pizzas[k]) + pizzas[k])
            V[k, slice_limit] = max(without_curr, with_curr)
        return V[k, slice_limit]

    V = defaultdict(lambda: -1)
    return optimum(len(pizzas)-1, constraint)

#todo fix this
def annealed_pizza(pizzas, init_temp = 100, steps = 100):
    def random_init():
        candidate = []

        return
    return


def pizza_solver_stupid(left_pizzas, slice_count):

    if slice_count >= CONSTRAINT:
        return [], -1

    if len(left_pizzas) == 0:
        return [], 0
    

    new_slices = pizza_slices[left_pizzas[0]]

    idxs1, sl1 = pizza_solver(left_pizzas[1:], slice_count + new_slices)
    idxs2, sl2 = pizza_solver(left_pizzas[1:], slice_count)
    print(sl1,sl2)
    if sl1 >= sl2:
        idxs1.append(left_pizzas[0])
        return idxs1, new_slices + sl1
    else:
        return idxs2, sl2

def test_input(file_name):
    parse_input(file_name)

    return pizza_cutter_solver(pizza_slices, CONSTRAINT, scaling_factor = 10000)


if __name__ == "__main__":
    sys.setrecursionlimit(16000)
    test_files = ['a_example.in', 'b_small.in', 'c_medium.in', 'd_quite_big.in', 'e_also_big.in']

    for test in test_files:
        print(test)
        parse_input(f'in/{test}')
        num, list = greedy_pizza_yummy(pizza_slices, CONSTRAINT)

        with open(f'out/output_{test[0]}.out', 'w') as output:  #todo
            output.write(f'{len(list)}\n')
            for i in list:
                output.write(f'{i} ')
