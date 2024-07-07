import datetime

try:
    
    date1 = datetime.date(1999, 1, 14)

    date2_input = input("Enter a date: ")

    def my_date(date):
        
        date2_input = date.split("-")
        date2 = datetime.date(int(date2_input[0]), int(date2_input[1]), int(date2_input[2]))
        
        date_out = (date2 - date1).days
        
        if date_out <= 0:
            print("Not Born Yet!")
        else:    
            print(date_out)
        
    my_date(date2_input) 

except:
    print("Error!")       