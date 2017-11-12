def smoothing(delta):
    def smoothing_decorator(func):
        def smoothing_wrapper(value):
            list_results = [func(value - delta), func(value), func(value + delta)]
            average = sum(list_results) / len(list_results)
            return average
        return smoothing_wrapper
    return smoothing_decorator


@smoothing(5)
def doSmthSmooth(x):
    return x


