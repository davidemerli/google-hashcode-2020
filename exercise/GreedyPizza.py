def greedy_pizza_yummy(pizza_slices, constraint):
    pizza_slices = [(p, i) for i, p in enumerate(pizza_slices) if p <= constraint]

    current_slices = 0
    list = []

    def fix(pizza_slices, current_slices):
        return [a for a in pizza_slices if a[0] + current_slices <= constraint]

    while len(pizza_slices) != 0:
        pizza = max(pizza_slices, key=lambda x: x[0])

        # print(pizza)
        pizza_slices.remove(pizza)
        if(current_slices + pizza[0] > constraint):
            break

        list.append(pizza[1])

        current_slices = current_slices + pizza[0]
        fix(pizza_slices, current_slices)

    return current_slices, list
