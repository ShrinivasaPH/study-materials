fruits_name = input("Enter your fruit name: ")

if fruits_name == 'mango':
  print("This is Mango.")
  type_mango = input("Enter the type of Mango: ")
  if type_mango == 'totapuri':
    print("This is Totapuri Mango")
    t_price = int(input("Enter the price: "))
    if t_price >= 100:
      print("Expensive.")
    else:
      print("Affordable.")
  elif type_mango == 'badam':
    print("This is Badam type Mango")
    b_price = int(input("Enter the price: "))
    if b_price >= 100:
      print("Expensive")
    else:
      print("Affordable")
  else:
    print("This is neigher Totapuri nor badam")
elif fruits_name == 'apple':
  print("This is apple")
  type_apple = input("Enter the type of apple.")
  if type_apple == 'ooty':
    print("This is ooty apple")
    o_price = int(input("Enter the price: "))
    if o_price >= 100:
      print("Expensive")
    else:
      print("Affordable")
  elif type_apple == 'kashmir':
    print("This is kashmir apple")
    k_price = int(input("Enter the price: "))
    if k_price >= 100:
      print("Expensive")
    else:
      print("Affordable")
else:
  print(f"This is neither apple nor mango but {fruits_name}.")