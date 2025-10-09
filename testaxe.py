# # # Function to check if a number is prime
# def is_prime(num):
# 	if num <= 1:
# 		return False
# 	for i in range(2, int(num**0.5)+1):
# 		if num % i == 0:
# 			return False
# 	return True
# # # Function to find prime numbers in the given interval
# # def find_primes(start, end):
# # 	primes = [num for num in range(2, end + 1) if is_prime(num)]
# # 	return primes
# #
# # # Read start value
# # start = int(input())
# #
# # # Read end value
# # end = int(input())
# #
# # # Find prime numbers
# # prime_numbers = find_primes(start, end)
# #
# # # Print the count of prime numbers
# # # print(f"{len(prime_numbers)}")
# #
# # # Print the prime numbers
# # # print(*prime_numbers)
# #
# print('hahah: ',is_prime(5))
#
# print('test axe')


#### axe 2

#
# def countIntegers(n, val, arr):
# 	smaller = sum(1 for num in arr if num < val)
# 	equal = sum(1 for num in arr if num == val)
# 	greater = sum(1 for num in arr if num > val)
# 	return [smaller, equal, greater]
#
#
# result = countIntegers(n, val, arr)
# print(result)




# def calculateRunningTotal(n, list_of_numbers):
#     to_list = list(str(list_of_numbers))
#
#     i = 0
#     total = 1
#     while i < len(to_list):
#         print(to_list[i])
#         total = total * int(to_list[i])
#         i = i + 1
#
#     if total %2 !=0:
#         return total
#
#     return sum(to_list)
# if __name__ == "__main__":
# 	n = int(input())
# 	list_of_numbers = list(map(int, input().split()))
# 	result = calculateRunningTotal(n, list_of_numbers)
# 	print(result)


# print(calculateRunningTotal(3,579))



# Candidate function
def hash(key, MAX_SIZE):
	# Write your code here
    hash_val = 1
    for idx, ch in enumerate(key, start=1):
        # pow(..., MOD) keeps the intermediate result small
        hash_val = (hash_val * pow(ord(ch), idx, MAX_SIZE)) % MAX_SIZE
    return hash_val


# # Get input from stdin
# key = input()
# MAX_SIZE = int(input())
#
# # Call candidate function
# result = hash(key, MAX_SIZE)

# Print result
print(hash('hello', 20))







