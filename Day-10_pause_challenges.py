def format_name(f_name, l_name):
    first_name = f_name.title()
    last_name = l_name.title()
    print(first_name, last_name)

    #OR we can use following one line to get the same output

    print(f_name.title(), l_name.title())


format_name(f_name="NIKHIL",l_name="BOrgAVE")


## CHECK LEAP YEAR

# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# print(format_name("AnGEla", "YU"))


def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    leap_year = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
            else:
                leap_year = False
        else:
            leap_year = True
    else:
        leap_year = False
    return(leap_year)
    print(leap_year)


leap_year = is_leap_year(2021)
print(leap_year)