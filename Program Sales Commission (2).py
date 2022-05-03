# Author: Jonathan Cherrington
# Date Created: Friday April 30,2022
# Course: ITT103
# Purpose: Program to calculate sales commission in repect to a sales person's class.

answer = str(input("Enter 'y' to calculate commission and 'n' to cancel:"))
if answer=="n":
   print("Transaction cancelled")
   quit()
if answer=="y":
 
  sales_person_num=int(input("Please indicate sales person number:"))
  sales_class=int(input("Please indicate sales class:"))
  sales_amt=int(input("Please state sales amount:"))
  commission_rate=int()

if sales_class== 1:
          if sales_amt <= 1000:
              commission_rate=0.06
          commission= sales_amt*(commission_rate)
          
          if sales_amt >1000 and sales_amt < 2000:
            commission_rate=0.07
            commission= sales_amt*(commission_rate)
          else:
           commission_rate=0.1
           commission= sales_amt*(commission_rate)

elif sales_class== 2:
          if sales_amt < 1000:
           commission_rate=0.04
           commission= sales_amt*(commission_rate)
          else:
              commission_rate=0.06
              commission= sales_amt*(commission_rate)
if sales_class== 3:
    commission_rate=0.045
    commission= sales_amt*(commission_rate)
else:
    print("Class not designated")
print("Commission rate is",commission_rate)
print("Commission is", commission)


    

      
  
