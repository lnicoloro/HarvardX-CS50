months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input('Date: ').strip()
    try:
        month, day, year = date.split('/')

        if int(day) < 0 or int(day) > 31 or int(month) < 0 or int(month) > 12:
            pass
        else:
            print(f"{year}-{int(month):02}-{int(day):02}")
            break

    except:

        month, day, year = date.split(' ')

        day = day.replace(',','')

        for item in months:
            if month == item:
                month = months.index(item) + 1

        if int(day) < 0 or int(day) > 31 or int(month) < 0 or int(month) > 12:
            pass

        else:
            print(f"{year}-{int(month):02}-{int(day):02}")
            break






