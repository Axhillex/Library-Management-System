import read as r1
import datetime

#function to rewrite the main file to decrease the quantity of available books
def rewrite_main_file(rewrite_list):
    rewrite_file= open("library.txt", 'w')
    for each in rewrite_list:
        counter =0
        for each_item in each:
            rewrite_file.write(str(each_item))
            counter+=1
            if counter<=4:
                rewrite_file.write(",")
        rewrite_file.write("\n")
    rewrite_file.close

#main function of the borrow module
def lend_book(quantity,cname,adname):
    list_for_lend=r1.store_file()
    list_for_operate_borrow=[[] for i in range(3)]
    print("S.No. of the book to be borrowed:")
    try:
        book=int(input())
    except:
        print("Please try again!")
        lend_book(quantity,cname,adname)
    else:
        list_for_lend[book][3]=int(list_for_lend[book][3])-quantity
        if int(list_for_lend[book][3])>0:
            if True:
                print(cname+" has borrowed "+str(quantity)+" book named "+list_for_lend[book][1]+" from "+adname+"("+str(datetime.datetime.now())+(")"))
                print("Your total is:"+str(list_for_lend[book][4]))
                print("Information is saved in file named "+cname+".")
                rewrite_main_file(list_for_lend)
                list_for_operate_borrow[0]=list_for_lend[book]
                next_book=input("Does customer want to borrow another book?(y/n):")
                if next_book=="y":
                    book1=int(input("S.No. of the book to be borrowed:"))
                    if book1==book:
                        print("Already borrowed!!")
                        lend_book(quantity,cname,adname)
                    else:
                        list_for_lend[book1][3]=int(list_for_lend[book1][3])-quantity
                        if int(list_for_lend[book1][3])>0:
                            print(cname+" has borrowed "+str(quantity)+" book named "+list_for_lend[book1][1]+" from "+adname+"("+str(datetime.datetime.now())+(")"))
                            print("Your total is:"+str(float(list_for_lend[book1][4])+float(list_for_lend[book][4])))
                            print("Information is saved in file named "+cname+".")
                            rewrite_main_file(list_for_lend)
                            list_for_operate_borrow[1]=list_for_lend[book1]
                            next_book=input("Does customer want to borrow another book?(y/n):")
                            if next_book=="y":
                                book2=int(input("S.No. of the book to be borrowed:"))
                                if book2==book1 or book2==book:
                                    print("Already borrowed!!")
                                    lend_book(quantity,cname,adname)
                                else:
                                    list_for_lend[book2][3]=int(list_for_lend[book2][3])-quantity
                                    if int(list_for_lend[book2][3])>0:
                                        print(cname+" has borrowed "+str(quantity)+" book named "+list_for_lend[book2][1]+" from "+adname+"("+str(datetime.datetime.now())+(")"))
                                        print("Your total is:"+str(float(list_for_lend[book1][4])+float(list_for_lend[book][4])+float(list_for_lend[book2][4])))
                                        print("Information is saved in file named "+cname+".")
                                        rewrite_main_file(list_for_lend)
                                        list_for_operate_borrow[2]=list_for_lend[book2]
                                        print(cname+" has borrowed 3 books in total. No more can be borrowed.")
                                        print("Thank you for your service.")
                                        borrow_2dlist_file(quantity,list_for_operate_borrow,cname)
                                    else:
                                        print("The book is out of stock but the remaining borrowed books list has been made in a file named "+cname)
                            else:
                                print("Thank you for your service.")
                                borrow_2dlist_file(1,list_for_operate_borrow,cname)
                        else:
                            print("The book is out of stock but the remaining borrowed books list has been made in a file named "+cname)
                else:
                    borrow_2dlist_file(1,list_for_operate_borrow,cname)
                    print("The borrowed list has been made in the file of name "+cname)
                    print("Thank you for your service.")
                    
            else:
                print("The borrowed list has been made in the file of name "+cname)
                print("Thank you for your service.")
        else:
            print("The book is out of stock")

#function to create a new file of the customer and store the information
def borrow_2dlist_file(quantity,lis,name):
    file_borrow=open(name+".txt","w")
    file_borrow.writelines("Bill of customer:"+name+"\t"+str(datetime.date.today())+"\n")
    file_borrow.writelines("S.No.\t Name\t Author\t Amount\n")
    for i in range(len(lis)):
        for j in range(len(lis[i])):
            if j!=3:
                file_borrow.write(str(lis[i][j])+"\t")
        if j!=3:
            file_borrow.write("\n")
    file_borrow.close


