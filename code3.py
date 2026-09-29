print("WELCOME\n choose 1 for ENTER YOUR PIN or choose 2 for account creation \n" 
      
"")
list_pin=["6789", "6798", "6879", "6897",
    "6978", "6987", "7689", "7698",
    ]
list_customer=[ "customer1", "customer2", "customer3", "customer4",
    "customer5", "customer6", "customer7", "customer8",
   ]
list_balance= [2000, 7500, 3200, 9000,
    4500, 6800, 2100, 10000,
    ]
m=int(input('Please enter your choice:\t'))
if m==1:

  
   n=input("pin should contain only the digits 6,7,8,9 ")
   
   
   if  len(str(n))==4 and n[0] in "6789" and n[1] in "6789" and n[2] in "6789" and n[3] in "6789":
       found=False
       
       for i in range(len(list_pin)):
           if (n)==list_pin[i]:
              found=True
              
              print("welcome",list_customer[i])
              while True:


                
                choice=int(input("1 to check balance, 2 to deposit, 3  to withdraw ,4 to exit"))

        
                if choice==1:
                   print(list_balance[i],"\n")

                elif choice==2:
                    deposit=int(input("enter amount to deposit"))
                    list_balance[i] =deposit+list_balance[i]
              
              
                    print(list_balance[i],"\n")
                elif choice==3:
              
                    withdraw=int(input("enter the amount to withdraw"))
                    if withdraw>list_balance[i]:
                       print("Insuficient amount")
                    elif withdraw<0:
                       print("error")
                    else:
                       list_balance[i]=list_balance[i]-withdraw
                       print("Here is your money",withdraw)
                       print("now your current amount is ",list_balance[i],"\n")
                elif choice==4:
                    print("Exit ,Thank you have a nice day","\n")
                    break
                else: 
                   print("invalid choice")
       if found==False:
            print("pin Doesn't exist")

   else:               
     print("invalid pin")
           
           
elif m==2:
    
    
    name=input('enter your name')
    list_customer.insert(0,name)
    print("enter four digit pin to login" "\n" "choose only the digits 6,7,8,9 and only once")
   
    while True:
      pin=(input())
      if  len(str(pin))==4 and pin[0] in "6789" and pin[1] in "6789" and pin[2] in "6789" and pin[3] in "6789":
     
       found=False
       for i in range(len(list_pin)):
          if pin==list_pin[i]:
             found=True
             print("pin already exist")
             break
         
       if found==False:
             break     
         
             
    list_pin.insert(0,pin)
    deposit=int(input("enter amount to deposit"))
    list_balance.insert(0,deposit)
    print("Thank you for account creation" "\n" "click 1 for to check balance")
    n=int(input())
    if n==1:
        print(list_balance[0],"\n" "click 4 for exit")
        m=int(input())
        if m==4:
            print("Thank you ")
                   

    else:
       print("invalid pin")
       


       
           
    
    
