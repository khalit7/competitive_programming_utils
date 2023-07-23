def find_fibo(n):
    '''
    finds the nth fibonacci element in time complexity O(log(n))
    find_fibo(0) = 0
    find_fibo(1) = 1
    find_fibo(2) = 1
    find_fibo(3) = 2

    :param n: index of the element to be found in the fibonacci sequence
    :return: fibonacci element at index n
    '''
    a = (1 + 5**0.5)/2
    b = (1 - 5**0.5)/2

    return (a**n - b**n)//(5**0.5)