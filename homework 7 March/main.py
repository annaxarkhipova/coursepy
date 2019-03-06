

# def fizzbuzz(n):
#     for i in range(1, n + 1):
#         otp = ''
#         if i % 3 and i % 5:
#             otp += 'FizzBuzz'
#         if i % 3:
#             otp += 'Fizz'
#         if i % 5:
#             otp += 'Buzz'
#     # return otp
#


for i in range(1,21):
    j = 'Fizz'*(not i % 3) + 'Buzz'*(not i % 5) or i
    print(j)