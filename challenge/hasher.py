from main import *
from simhash import Simhash
import hashlib
from functools import lru_cache
from heapq import *

def simhash_library(book_list):
    book_string_set = [f'{b.index}' for b in book_list]
    sh = Simhash(book_string_set).value
    return sh

def get_max_heap(num_clusters, libraries, a, b, days_left):
    sorted_libs = libraries[::]
    sorted_libs.sort(key=lambda l: l.simhash)

    # for l in sorted_libs:
    #     print(l.library_index, l.simhash)

    offset = len(sorted_libs)//num_clusters
    clusters = [sorted_libs[x:x+offset] for x in range(0, len(sorted_libs), offset)]

    best_heap = []
    worst_heap = []

    for c in clusters:

        scores = [(-score_library(a, b, lib, days_left), lib) for lib in c]
        scores.sort(key=lambda x: x[0])

        best = scores.pop(0)
        best_heap.append(best)

        worst_heap.extend(scores)
    heapify(best_heap)
    heapify(worst_heap)
    # print(best_heap)

    # print([el[0] for el in best_heap])

    return best_heap, worst_heap

        # print([s[1] for s in scores])

def score_library(a, b, library, days_left):
    # throughput = library.books_per_day/library.days_to_sign
    # overhead = days_left/library.days_to_sign

    return a * throughput(library) + b * overhead(library,days_left)

def throughput(library):
    return library.books_per_day/library.days_to_sign

def overhead(library, days_left):
    return days_left/library.days_to_sign

#O(depth) (depth potete farlo molto piccolo o multiplo di library.books_per:day)
def preview(library, books, depth):
    return sum(itertools.islice(map(lambda x : books[x].value, library.book_list),0,depth))

#O(1)
def reachability(library, days_left):
    return min(len(library.book_list), library.books_per_day*(days_left - library.days_to_sign))
