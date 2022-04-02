import os, datetime

bookname = "   ***ABC Kirana Store Udhar Khata book***"
print(bookname)

while True:
    buyersKhatas = os.listdir("data\\")
    choose = input("""_________________________________________
What to do?
    [1]. work with exixting buyers' khata
    [2]. add new buyer khata
>>>""")

    if choose == "1":
        if len(buyersKhatas) == 0:
            print("Book is empty! No buyer khatas are added yet")
        else:
            n = 1
            print(f"{(' ') * 4}Accounts{(' ') * 12}date created")

            for buyerName in buyersKhatas:
                with open(f"data\\{buyerName}") as f:
                    khata = f.read()
                    dateCreated = khata[12 : khata.index("\n")]

                buyerName = buyerName.replace('.txt', '')

                if len(buyerName) > 16:
                    bN_pt1 = buyerName[:16]
                    bN_pt2 = buyerName[:]
                    print(f"[{n}] {bN_pt1}    {dateCreated}\n{bN_pt2}\n")
                else:
                    print(f"[{n}] {buyerName}{(' ') * (20 - len(buyerName))}{dateCreated}\n")
                n += 1
            
            choose = input("\nAccess an account(y/n): ")

            if choose == "y":
                choose = input("enter buyer khata index: ")
                
                if choose.isnumeric():
                    if int(choose) > 0 and int(choose) <= n:
                        n = 1
                        for buyerName in buyersKhatas:
                            buyerName = buyerName
                            if n == int(choose):
                                with open(f"data\\{buyerName}") as f:
                                    print("\n", "-" * 30)
                                    print(f.read())
                                    break
                                    
                            n += 1
                        choose = input("[1]. add a bought product\n[2]. delete this account\n>>>")

                        if choose == "1":
                            boughtProduct = "-> " + input("bought product: ")
                            boughtProductPrice = input("bought product price: ")
                            
                            with open(f"data\\{buyerName}", "a") as f:
                                if len(boughtProduct) > 27:
                                    bP_pt1 = boughtProduct[:27]
                                    bP_pt2 = boughtProduct[27:]
                                    f.write(f"{bP_pt1}")
                                    f.write(f"{(' ') * 4}{boughtProductPrice}")
                                    f.write(f"{(' ') * (13 - len(boughtProductPrice))}{datetime.datetime.now().strftime('%A %d %b %Y')}\n")
                                    f.write(f"{bP_pt2}\n")
                                else:
                                    f.write(boughtProduct)
                                    f.write(f"{' ' * (31 - len(boughtProduct))}{boughtProductPrice}")
                                    f.write(f"{(' ') * (13 - len(boughtProductPrice))}{datetime.datetime.now().strftime('%A %d %b %Y')}\n")

                        elif choose == "2":
                            choose = input(f"Are you sure you want to delete this account of {buyerName.replace('.txt', '')} (y/n)")

                            if choose == "y":
                                os.remove(f"data\\{buyerName}")       

                    else:
                        print("No, buyer khata with this index no.!")
    elif choose == "2":
        newAccholder = input("Enter name of the new account holder: ")
        with open(f"data\\{newAccholder}.txt", "a") as f:
            f.write(f"Created on- {str(datetime.datetime.now().strftime('%A %d %b %Y'))}\nAccount of {newAccholder}--\n\n\
    Products bought{(' ') * 16}Price{(' ') * 8}Date\n")




