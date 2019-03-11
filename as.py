import os
import time
clear = lambda :os.system("cls")


a =[["Staff001","pass1"],["user2","pass2"],["user3","pass3"]]
password_pass=True
while password_pass:
    user=input("username ID : ")
    pasw=input("Password : ")
    for i in range(len(a)):
        if user == a[i][0] and pasw == a[i][1]:
            print("\n---Hello :) ---,",a[i][0])
            password_pass=False
            break
    else:
        print("!!! Wrong username please try again !!!")
        time.sleep(1)
        clear()
    

   

print("\n***Welcome to Bus Ticket Online Shop!***")
print("Please Choose Your Destination")
print("\nNo1. Payao ---> Lampang\nNo2. Payao ---> Chiang Rai\nNo3. Payao ---> Chiang Mai")

destination=int(input("Your Destination : "))
if destination ==1:
    print("\n\tPayao to Lampang\n")
    
    print("\t*Status Choise*\n\tNo.001 : Adult\n\tNo.002 : Child\n\tN0.003 : Old\n\tNo.004 : Monk\n")
    
    status=input("Select your Status : ")
    if status == 1:
        print("\tPrice Ticket Payao to Lampang is : %d BATH."%Pao_Lam+adult_seat)

    elif status ==2:
        print("\tPrice Ticket Payao to Lampang is : %d BATH."%Pao_Lam+child_seat)

