import write_return as wr
import datetime

#to import the borrowed date and calculate it
def date_calculation(cust_name):
    date_list=wr.customer_file(cust_name)
    fixed_date=date_list[0][1].split("-")
    b_year=fixed_date[0]
    b_month=fixed_date[1]
    b_date=fixed_date[2]
    a = datetime.date.today()
    b = datetime.date(int(b_year),int(b_month),int(b_date))
    x = a-b
    return x.days

#to check the time borred and display the output accordingly
def date_check(cus_file_name):
    if date_calculation(cus_file_name)>10:
        print("Your return date exceeds the library borrow-return rule(10 days) so a fine is being added to your bill.")
        print("You have to pay a fine of 1$ per book per day that exceeds the borrow date rule.")
    
        

        
    
