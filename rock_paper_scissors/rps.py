#!/usr/bin/python

import sys

import sys

def rock_paper_scissors(n):
  outcomes = []
  choices = ["rock", "paper", "scissors"]

  def get_result(rounds, arr=[]):
    
    if rounds == 0:
      new_outcomes = outcomes.append(arr)
      return new_outcomes 
  
    else:
      for each_choice in choices:
        get_result(rounds -1, arr + [each_choice]) 
  
  get_result(n, [])
  return outcomes


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')