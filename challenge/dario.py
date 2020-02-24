from collections import namedtuple
Entry = namedtuple('Entry', ['library_index', 'books_sent'])

def simulate(struct, libraries, solution):
    num_reg, score, curr_reg = 0, 0, libraries[solution[0].library_index]
    reg_days_rem, signup_end = curr_reg.days_to_sign, False
    sent = set()

    for day in range(struct.days):
        #print("Day " + str(day))
        #add books
        if not signup_end:
            reg_days_rem -= 1
            #print("Registration of " + str(solution[num_reg].library_index) + " in " + str(reg_days_rem) + " days")

        for lib in solution[0:num_reg]:
            for i in range(libraries[lib.library_index].books_per_day):
                if len(lib.books_sent) > 0:
                    #print("Scanned book " + str(lib.books_sent[0]) + " from lib " + str(lib.library_index)
                        #+ " already scanned= " + str(lib.books_sent[0] in sent))
                    sent.add(lib.books_sent.pop(0).index)
                else:
                    break
            #OPTIMIZE: mark as finished

        if reg_days_rem == 0:

            if not signup_end:
                #print("Registered: " + str(solution[num_reg].library_index))
                num_reg += 1
            signup_end = num_reg == len(solution)
            if not signup_end:
                curr_reg = libraries[solution[num_reg].library_index]
                reg_days_rem = curr_reg.days_to_sign

    return sum(map(lambda x: struct.books[x].value,sent))

def generate_output(filename,solution):
    with open(filename,"w") as f:
        f.write(str(len(solution)) + "\n")
        for lib in solution:
            f.write(str(lib.library_index) + " " + str(len(lib.books_sent)) + "\n")
            for book in lib.books_sent:
                f.write(str(book.index) + " ")
            f.write("\n")
