#!/usr/bin/python

import argparse



def find_max_profit(prices):
  lowest_buy = prices[0]
  highest_sell = prices[1]
  for buy in range(len(prices)-1):
  	if prices[buy] < lowest_buy:
  		lowest_buy = prices[buy]
  		highest_sell = prices[buy +1]
  	for sell in range(buy + 1, len(prices)):
  		if(prices[sell] > highest_sell):
  			highest_sell = prices[sell]

  return highest_sell - lowest_buy


print(find_max_profit([1050, 270, 1540, 3800, 2]))

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))