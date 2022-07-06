

def convertTo24H(input):
    temp_string = ''
    for x in input:
        if x.isdigit():
            temp_string = temp_string.join(x)

    if 'pm' in input:
        return (int(temp_string) + 12) % 24
    else:
        return int(temp_string)


def convertTimeRange(x):
    times = x.split('-')

    # initializing variables and turning the times into 24-hour style
    beg_time = convertTo24H(times[0])
    end_time = convertTo24H(times[1])

    # initiate string with ',' to make it easier to search for a time using the in keyword (',9,' = 9 vs '9' = 9 or 19)
    time_string = ","
    while beg_time % 24 != end_time + 1:
        time_string = time_string + str(beg_time % 24) + ','
        beg_time = beg_time + 1
    return time_string


# turn a range into a string containing the individual months
def convertMonthRange(x):
    months = x.split('-')

    beg_month = int(months[0])
    end_month = int(months[1])
    month_string = ""

    #
    if beg_month > end_month:
        # a while loop to create a string of the month names separated by a comma
        while beg_month % 12 != end_month:
            # create a string separated by commas containing the month name
            month_string = month_string + returnMonthName(beg_month % 12) + ','
            beg_month = beg_month + 1
    else:
        while beg_month != end_month:
            # create a string separated by commas containing the month name
            month_string = month_string + returnMonthName(beg_month % 12) + ','
            beg_month = beg_month + 1
    month_string = month_string + returnMonthName(beg_month % 12) + ','
    return month_string


# return the string of a month when given the int number (where December is 12
def returnMonthName(x):
    if x == 1:
        return 'January'
    elif x == 2:
        return 'February'
    elif x == 3:
        return 'March'
    elif x == 4:
        return 'April'
    elif x == 5:
        return 'May'
    elif x == 6:
        return 'June'
    elif x == 7:
        return 'July'
    elif x == 8:
        return 'August'
    elif x == 9:
        return 'September'
    elif x == 10:
        return 'October'
    elif x == 11:
        return 'November'
    elif x == 0:
        return 'December'
    else:
        raise Exception('Invalid Number given')


# find the months that the fish is available
def findAvailableMonths(givenMonths):
    # if there are two time frames
    if '&' in givenMonths:
        months_set = (givenMonths).split(" & ")
        months1 = convertMonthRange(months_set[0])
        month2 = convertMonthRange(months_set[1])
        return months1 + month2
    # if one time frame
    elif '-' in givenMonths:
        return convertMonthRange(givenMonths)
    else:
        return returnMonthName(int(givenMonths))


# return a tuple with the given user info
def getUserInfo():
    user_tuple = []
    # ask the user to choose a hemisphere:
    user_input1 = input("What hemisphere are you playing in? (s for southern/n for northern):\n")
    if user_input1 == 's':
        user_tuple.append('month-southern')
    else:
        user_tuple.append('month-northern')

    # ask the user to choose a language from the list
    # using direct association because the user will be copypasting from our list
    user_tuple.append(input("What language do you want the fish name to be written in? Please copy and paste one of the following: \n"
                          "(name-USen/name-EUen/name-EUde/name-EUes/name-USes/name-EUfr/name-USfr/name-EUit/name-EUnl/name-CNzh/name-TWzh/"
                          "name-JPja/name-KRko/name-EUru)\n"))
    return user_tuple