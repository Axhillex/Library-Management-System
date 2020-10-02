#to check if the name exists or not in the directory
def chk_name(cname,quantity,adnam):
    a=False
    try:
        file=open(cname+".txt","r")
        file.close()
    except:
        print("please try again")
    else:
        a=True
    return a
  
