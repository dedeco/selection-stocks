import itertools
import operator


def selectStock(saving, currentValue, futureValue):
    result = list(map(operator.sub, futureValue, currentValue))
    for idx, _ in enumerate(result):
        if result[idx] < 0:
            del currentValue[idx]
            del futureValue[idx]
            del result[idx]
    #print(currentValue, futureValue)
    max_profit = 0
    array_s = {k: v for k, v in sorted(enumerate(currentValue), key=lambda x: x[1])}
    for i in range(1, len(currentValue)):
        stop = True
        for itens, idx in zip(itertools.combinations(array_s.values(), i), itertools.combinations(array_s.keys(), i)):
            if sum(itens) <= saving:
                profit = sum([result[i] for i in idx])
                if profit > max_profit:
                    max_profit = profit
                stop = False
        if stop:
            break
    return max_profit

