saleTax=0.075   #Tax in florida
tipAmount=0.18  #Tip 18%
print()
print("Thanks for using the restaurant generator by Luis")
print()
foodcost=float(input("Please enter the cost of food:  "))
drinkcost=float(input("Please enter the cost of drink:  "))
print()
costofmeal= foodcost+drinkcost
taxamount=costofmeal*saleTax
tipcalc=(costofmeal+taxamount)*tipAmount
total=costofmeal+taxamount+tipcalc

print("Restaurant Bill")
print("------------------------------")
print(f'Cost of Meal:  $ {costofmeal:.2f}')  
print(f'Tax Amount:    $ {taxamount:.2f}')  
print(f'Tip Amount:    $ {tipcalc:.2f}')  
print("                ----------------")
print(f'Total:         $ {total:.2f}')  
print('thanks for using this program made by luisi')


