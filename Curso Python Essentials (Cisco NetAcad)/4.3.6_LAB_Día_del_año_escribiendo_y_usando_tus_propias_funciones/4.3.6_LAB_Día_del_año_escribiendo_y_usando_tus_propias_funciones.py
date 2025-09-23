def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month >= 1 and month <= 12:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_year_leap(year):
            days[1] = 29
            days_amount = days[month - 1]
        else:
            days_amount = days[month - 1]
        return days_amount
    else:
        return None

def day_of_year(year, month, day):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if days_in_month(year,month) != None:
        day_of_year_number = 0
        if day >= 1 and day <= days_in_month(year, month): 
            if is_year_leap(year):
                days[1] = 29
                for i in range(month - 1):
                    day_of_year_number += days[i]
                day_of_year_number += day
            else:
                for i in range(month - 1):
                    day_of_year_number += days[i]
                day_of_year_number += day
            return day_of_year_number
        
        else:
            return None

        
    else:
        return None

print(day_of_year(2000, 12, 31))