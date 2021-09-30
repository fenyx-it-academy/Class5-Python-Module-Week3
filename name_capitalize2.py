def name_check():
  n_list=input("Write your full name splitted with space ' ') : ").split(' ')
  cname=[]
  for i in n_list:
    i=(i).capitalize()
    cname.append(i)
  return (" ".join(cname))
print(name_check())