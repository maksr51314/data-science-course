#try схема горнера

def polinom(coefficients):
    def polinom_wrapper(x):
        sum = 0
        for index, coef in enumerate(coefficients):
            val = coef * x ** (len(coefficients) - 1 - index)
            sum += val

        return sum
    return polinom_wrapper



res = polinom([1, 2, 3])(2)

print(res)
