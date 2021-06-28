def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        return print("True")
    else:
        return print("False")
is_leap_year(2004)
is_leap_year(2021)