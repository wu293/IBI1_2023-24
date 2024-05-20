age = int(input("The year you were born is \n"))
year= age+18
def Favourite_JamesBond_Actor(year):
    if year >= 1973 and year <= 1986:
        print("Your favorite James Bond actor is Roger Moore")
    elif year >= 1987 and year <= 1994:
        print("Your favorite James Bond actor is Timothy Dalton")
    elif year >= 1995 and year <= 2005:
        print("Your favorite James Bond actor is Pierce Brosnan")
    elif year >= 2006 and year <= 2021:
        print("Your favorite James Bond actor is aniel Craig")
    else:
        print("error")

Favourite_JamesBond_Actor(year)
