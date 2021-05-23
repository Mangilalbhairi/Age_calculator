from datetime import date # import datetime module

#define function for age calculation
def age_calculator(birth_date):
    #intilization variable for storing current year month or day
    today = date.today()
    current_year = today.year
    current_month = today.month
    current_day = today.day
   
    year = current_year - birth_date.year
    #calculate the age in all posibilities and use if else for check wheather birth date and birth month is greater or not from current month current month 
    if birth_date.month > current_month and birth_date.day > current_day: # if birth date and month is greater than curren month and date than execute this this if block body
        month = current_month + 12 - birth_date.month
        year = year-1
        if current_month == 1 or current_month == 3 or current_month == 5 or current_month == 7 or current_month == 8 or current_month == 10 or current_month == 12:
            
            day = current_day + 31 - birth_date.day
            month = month-1
        else:
            day = current_day + 30 - birth_date.day
            
    elif birth_date.month > current_month:   #if birth month is greater than current month than execute this if block body
         
         month = current_month + 12 - birth_date.month
         day = current_day  - birth_date.day
         year = year-1

    elif birth_date.day > current_day:   #if birth date is greater than current date than execute this if block body
         day = current_day + 30 - birth_date.day
         month = current_month  - birth_date.month
         month = month-1

    else:#if birth month and date both are less than current month and current date than execute else part
        
        
        month = current_month  - birth_date.month
        day = current_day  - birth_date.day
         
         

    return year, month, day # return year month and date after doing complete calulations

#Take input from users        
    
birth_year = int(input("Enter Your Birth Year : "))
birth_month = int(input("Enter Your Birth Month : "))
birth_day = int(input("Enter Your Birth Date : "))

age_old = age_calculator(date(birth_year,birth_month,birth_day))#call the age_calculator function and passing date of birth as a argument
print("Hey You Are ",age_old[0],"Year",age_old[1],"Month",age_old[2],"Days Old" )#print the age 


