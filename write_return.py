import read as r1
import datetime
import date as d1

#reads the customer file and stores in a list
def customer_file(cname):
    file_read=open(cname+".txt","r")
    list_customer=[]
    file_content=file_read.readlines()
    for each in file_content:
        list_customer.append(each.replace("\n","").split("\t"))
    file_read.close()
    return list_customer

#prints the list of the customer file
def print_cus_file(proper_list):
    for each in proper_list:
        for words in each:
            a=len(words)
            break
        break
    for each in proper_list:
        for words in each:
            if len(words)>a:
                a=len(words)
    for each in range(len(proper_list)):
        for words in range(len(proper_list[each])):
            if words!=0:
                if len(proper_list[each][words])<=a:
                    print(proper_list[each][words]+int(a-len(proper_list[each][words]))*" ",end="\t")
                else:
                    print(proper_list[each][words])
            else:
                print(proper_list[each][0],end="   ")
        print("\n")

#rewrites the main file to increase the number of books returned
def rewrite_main_file(rewrite_ret):
    out = open("library.txt", 'w')
    for each in rewrite_ret:
        counter =0
        for each_item in each:
            out.write(str(each_item))
            counter+=1
            if counter<=4:
                out.write(",")
        out.write("\n")
    out.close()

#the main function of module return    
def return_book(cname,quantity):
    list_for_return=customer_file(cname)
    print_cus_file(customer_file(cname))
    list_ret=r1.store_file()
    print("Which book is to be returned?("+str(len(list_for_return)-3)+" books in total):")
    try:
        ret_num=int(input())
    except:
        print("Please try again!")
        return_book(cname,quantity)
    else:
        a=ret_num+1
        if ret_num==1 or ret_num==2 or ret_num==3:
            if ret_num==1:
                print("The book "+str(list_for_return[2][1])+" has been returned at "+str(datetime.datetime.now()))
                print("The book was returned after "+str(d1.date_calculation(cname)))
                d1.date_check(cname)
                for i in range(len(list_ret)):
                    if list_for_return[2][1]==list_ret[i][1]:
                        list_ret[i][3]=int(list_ret[i][3])+1
                        rewrite_main_file(list_ret)
                z=input("Return another book?(y/n):")
                if z=="y":
                    return_book(cname,quantity)
                else:
                    print("Thank you for your service!")
            elif ret_num==2:
                print("The book "+str(list_for_return[3][1])+" has been returned at "+str(datetime.datetime.now()))
                print("The book was returned after "+str(d1.date_calculation(cname)))
                d1.date_check(cname)
                for i in range(len(list_ret)):
                    if list_for_return[3][1]==list_ret[i][1]:
                        list_ret[i][3]=int(list_ret[i][3])+1
                        rewrite_main_file(list_ret)
                z=input("Return another book?(y/n):")
                if z=="y":
                    return_book(cname,quantity)
                else:
                    print("Thank you for your service!")
            else:
                print("The book "+str(list_for_return[4][1])+" has been returned at "+str(datetime.datetime.now()))
                print("The book was returned after "+str(d1.date_calculation(cname)))
                d1.date_check(cname)
                for i in range(len(list_ret)):
                    if list_for_return[4][1]==list_ret[i][1]:
                        list_ret[i][3]=int(list_ret[i][3])+1
                        rewrite_main_file(list_ret)
                z=input("Return another book?(y/n):")
                if z=="y":
                    return_book(cname,quantity)
                else:
                    print("Thank you for your service!")


