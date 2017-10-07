# yr = 365
# wk = 7
# if jan 1, 1701 is a saturday and  jan 8 is a saturday then every 7 days is a saturday, what is that day?

months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
oddmonths = ["january", "march","may", "july", "august", "october", "december"]


saturdays = []

def monchecker(i):
    if i == "february":
        return 29
    elif i in oddmonths:
         return 32
    else:
        return 31

day = 1
for i in range(1701, 1800):
    for i in months:
        x = monchecker(i)

        counter = 1

        while day != x:
            if counter == 7:
                saturdays.append([counter,day])
                counter = 1
            else:
                counter +=1
            day += 1
        day = 1


print(saturdays)

# for i in saturdays:
#     if i == [7,1]:
#         print ('yes')
