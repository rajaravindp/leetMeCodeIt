# Excessive Recursion: Time complexity is O(2**n)
# def fibonacci(n):
#     if n <= 1:
#         return n

#     res =  fibonacci(n-1) + fibonacci(n-2)
#     return res

# print(fibonacci(8))



# Using Memoization: Time Complexity is O(n)
def fib(n, memo= {}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
print(fib(8))



# Loop
# def fibonacci1(n):
#     a = 0
#     b = 1
#     res = 0

#     if n <= 1:
#         return n
#     for i in range(2, n+1):
#         res = a + b
#         a = b
#         b = res
#     return res
# print(fibonacci1(8))