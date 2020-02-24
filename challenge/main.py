from collections import namedtuple
import os
import hasher
from heapq import *
import dario

Struct = namedtuple('Struct', ['num_books', 'num_libraries', 'days', 'books'])
Book = namedtuple('Book', ['index', 'value'])
Library = namedtuple('Library', ['library_index', 'num_of_books_in_lib', 'days_to_sign', 'books_per_day', 'simhash', 'book_list', 'sorted_book_list'])
Entry = namedtuple('Entry', ['library_index', 'books_sent'])

def parse_input(input_file):
    with open(input_file) as file:
        lines = file.readlines()

        num_books, num_libraries, days = [int(l) for l in lines[0].split()]

        books = [Book(i, int(book)) for i, book in enumerate(lines[1].split())]
        struct = Struct(num_books, num_libraries, days, books)

        # print(struct)

        struct = Struct(num_books, num_libraries, days, books)

        libraries = []

        for i in range(2, len(lines) -1, 2):
            library_index = i // 2 -1

            num_of_books_in_lib, days_to_sign, books_per_day = [int(l) for l in lines[i].split()]

            books_in_lib = [books[int(book)] for book in lines[i+1].split()]

            sorted_books = books_in_lib[::]
            sorted_books.sort(reverse=True, key=lambda x: x.value)

            library = Library(library_index, num_of_books_in_lib, days_to_sign, books_per_day, hasher.simhash_library(books_in_lib), set(books_in_lib), sorted_books)
            libraries.append(library)
            # print(library.book_list)
            # print(library.sorted_book_list)
        return struct, libraries
import random


if __name__ == '__main__':
    input_files = [str(f) for f in os.listdir(os.getcwd() + '/in') if 'txt' in str(f)]
    input_files.sort(key=lambda f: str(f))
    # input_files = input_files[1:2]

    cosebuffe = [1,  random.randint(0, 10),  random.randint(0, 1000),  random.randint(0, 1000),  random.randint(0, 1000),  random.randint(0, 1000)]
    print(input_files)

    for i, f in enumerate(input_files):
        struct, libraries = parse_input(f'in/{f}')

        # avg_sp = average(libraries, lambda l: l.days_to_sign)
        # val = struct.days/avg_sp

        # print("VAL" + val)
        print(f)
        best_heap, worst_heap = hasher.get_max_heap(cosebuffe[i], libraries, random.randint(0, 10), random.randint(0, 10), struct.days)

        days_left = struct.days

        output = []

        taken_books = set()

        while days_left > 0:
            if len(best_heap) > 0:
                bestbest = heappop(best_heap)

                book_set = bestbest[1].book_list.difference(taken_books)
                taken_books.union(book_set)

                output.append((bestbest[1].library_index, len(book_set), book_set))
            elif len(worst_heap) > 0:
                bestworst = heappop(worst_heap)

                book_set = bestworst[1].book_list.difference(taken_books)
                taken_books.union(book_set)

                output.append((bestworst[1].library_index, len(book_set), book_set))
            else:
                break



        # print(len(output))
        entries = []
        for o in output:
            e = Entry(o[0], list(o[2]))
            entries.append(e)
            # print(o[0], o[1])
            # print(' '.join([str(book.index) for book in o[2]]))
        dario.generate_output(f'out/{f[0]}.out', entries)

        print(dario.simulate(struct, libraries, entries))
