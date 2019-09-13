#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

memcache={}

def eating_cookies(n, memcache=None):
	if n in memcache:
		return memcache[n]
	if n < 0:
		return -1
	if n <= 1:
		return 1
	if n == 2:
		return 2
	result = int(eating_cookies(n-1, memcache) + eating_cookies(n-2, memcache) + eating_cookies(n-3, memcache)) 
	memcache[n] = result
	return result





# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')