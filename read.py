#to store the data of text file in a 2d list
def store_file():
    file_read=open("library.txt","r")
    l1=[]
    file_content=file_read.readlines()
    for each in file_content:
        l1.append(each.replace("\n","").split(","))
    file_read.close()
    return l1

#to display the 2d list in an organized manner
def print_2d_file(proper_list):
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
                print(proper_list[each][words],end="\t")
        print("\n")


