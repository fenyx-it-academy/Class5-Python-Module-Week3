"""This func ensures that the first and last names of people begin with a
capital letter in their passports. For example, 
alison heck should be capitalised correctly as Alison Heck."""

#to capitalize the given full name appropriately.
# capitalize() method converts first letter of words to a capital letter
def name_check():
  n_list=input("Write your full name splitted with space ' ') : ").split(' ')
  name=(n_list[0]).capitalize()
  surname=(n_list[1]).capitalize() 
  fullname=[name,surname]
  Cap_f_n_=(" ".join(fullname))
  return(Cap_f_n_)

print(name_check())