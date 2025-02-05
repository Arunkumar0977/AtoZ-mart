import mysql.connector
print("                                                     *****************************************************************")
print("                                                     *                                                               *")
print("                                                     *                   Welcome To A to Z Mart                      *")
print("                                                     *                                                               *")
print("                                                     *****************************************************************")

mydb=mysql.connector.connect(host="localhost",user='root',passwd='hostme@2004')
mycursor=mydb.cursor()
mycursor.execute("create database if not exists mart")
mycursor.execute("use mart")
mycursor.execute("create table if not exists login(username varchar(25) not null,password varchar(25) not null)")
mycursor.execute("create table if not exists purchase(odate date not null, name varchar(35) not null, pcode int not null, amount int not null)")
mycursor.execute("create table if not exists stock(pcode int not null, pname varchar(25) not null, quantity int not null, price int not null)")
mydb.commit()
z=0
mycursor.execute("select * from login")
for i in mycursor:
    z+=1
if(z==0):
    mycursor.execute("insert into login values('username','1234')")
    mydb.commit()
while True:
    print("""
1.Admin
2.Customer
3.Exit
""")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        passs=(input("Enter password:"))
        mycursor.execute("select * from login")
        for i in mycursor:
            username,password=i
        if(passs==password):
            print("                                                                       -----------------------")
            print("                                                                      |       WELCOME         |")
            print("                                                                       -----------------------")
            loop2='y'
            while(loop2=='y' or loop2=='y'):
                print("""
            1.Add New Item
            2.Updating Price
            3.Deleting Item
            4.Display all Items
            5.To change the password
            6.Log Out
            
""")
                ch=int(input("Enter your choice: "))
                if(ch==1):
                    loop='y'
                    while(loop=='y' or loop=='y'):
                        pcode=int(input("Enter product code: "))
                        pname=input("Enter product name: ")
                        quantity=int(input("Enter product quantity: "))
                        price=int(input("Enter product price: "))
                        mycursor.execute("insert into stock values('"+str(pcode)+"','"+pname+"', '"+str(quantity)+"','"+str(price)+"')")
                        mydb.commit()
                        print("                                                          Record Inserted Successfully .....")
                        loop=input("Do you want to enter more items(y/n):")
                        print("                                                          Thank you for your response!")
                    loop2=input("Do you want to continue Editing Stock(y/n):")
                elif(ch == 2):
                    loop2 = 'y'
                    while loop2.lower() == 'y':  # Simplified to handle both 'y' and 'Y'
                        pcode = int(input("Enter product code: "))
                        new_price = int(input("Enter new price: "))
                        try:
                            mycursor.execute("UPDATE stock SET price = %s WHERE pcode = %s", (new_price, pcode))  # Use parameterized query
                            mydb.commit()
                            print("                            New Price Updated Successfully .....")
                        except mysql.connector.Error as err:
                            print(f"Error: {err}")

                        loop = input("Do you want to change the price of any other item (y/n): ")
                        print("                                                          Thank you for your response!")
                        if loop.lower() != 'y':
                            break  # Exit the inner loop if the user doesn't want to continue

                    loop2 = input("Do you want to continue Editing Stock (y/n): ")
                    print("                                                          Back to main menu!" if loop2.lower() != 'y' else "                                                          Continuing to edit stock...")

                elif(ch==3):
                        loop='y'
                        while(loop=='y' or loop=='Y'):
                            pcode=int(input("Enter product code:"))
                            mycursor.execute("Delete from stock where pcode='"+str(pcode)+"'")
                            mydb.commit()
                            print("                                 Item deleted Successfully.....")
                            loop=input("Do you want to delete any other data(y/n):")
                            print("                                                          Thank you for your response!")
                        loop2=input("Do you want to continue editing stock(y/n):")
                elif(ch==4):
                    mycursor.execute("select * from stock")
                    print("pcode || pname || quantity || price")
                    for i in mycursor:
                        t_code,t_name,t_quant,t_price=i
                        print(f"{t_code} || {t_name} || {t_quant} || {t_price}")
                elif(ch==5):
                    old_pass=input("Enter old password:")
                    mycursor.execute("select * from login")
                    for i in mycursor:
                        username,password=i
                    if(old_pass==password):
                        new_pass=input("Enter new password:")
                        mycursor.execute("update login set password='"+new_pass+"'")
                        mydb.commit()
                        print("                                                               New password Updated Successfully.....")
                elif(ch==6):
                    print("                          Loged Out Successfully...................")
                    break

        else:
                print("                                                                     Wrong Password.............")

############################################################Customer Section################
    elif(ch==2):
        print("""1.Item Bucket
2.Payment
3.View Available Items
4.Go Back """)
        ch=int(input("Enter your  choice:"))
        if(ch==1):
            loop='y'
            while(loop=='y' or loop=='y'):
                name=input("Enter your name:")
                pcode=int(input("Enter product code:"))
                quantity=int(input("Enter product Quantity:"))
                mycursor.execute("select * from stock where pcode='"+str(pcode)+"'")
                for i in mycursor:
                    t_code,t_name,t_quant,t_price=i
                    amount=t_price*quantity
                    net_quant=t_quant-quantity
                    mycursor.execute("update stock set quantity='"+str(net_quant)+"' where pcode='"+str(pcode)+"'")
                    mycursor.execute("INSERT INTO purchase (odate, name, pcode, amount) VALUES (NOW(), %s, %s, %s)", (name, str(pcode), str(amount)))
                    mydb.commit()
                    print("                                 Inserted Successfully......")
                    loop=input("Do you want to enter more items(y/n):")
                    print("                                                          Thank you for your response!")
                loop2=input("Do you want to continue Editing Stock(y/n):")
                    
        elif(ch==2):
            print(f"                                     Amount to be paid:{amount}")
        elif(ch==3):
            print("CODE || NAME || PRICE")
            mycursor.execute("select * from stock")
            for i in mycursor:
                t_code,t_name,t_quant,t_price=i
                print(f"{t_code} || {t_name} || {t_price} ")
        elif(ch==4):
            print("                             THANK YOU!")
            print("                             -----------")
            print("                            VISIT AGAIN!")
            break
    elif(ch==3):
        print("                                                                                   THANK YOU!")
        print("                                                                                  -----------")
        print("                                                                                  VISIT AGAIN!")
        break
       
    



    
