"""This func ensures that the first and last names of people begin with a
capital letter in their passports. For example, 
alison heck should be capitalised correctly as Alison Heck."""


#Given a full name, the task is to capitalize the full name appropriately.
def name_check():
  nr_list=[n for n in input("Avoiding repeating(split with a space ' ')  :").split(' ')]
  #given full name(splitted with" ") will directly go in list(nrlist).
  name=(''.join(nr_list[0])).capitalize()
  surname=(''.join(nr_list[1])).capitalize()
  #due to capitalize() method,we convert first letter of each words to a capital letter.
  print(name,surname)

name_check()
