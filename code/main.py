# importing packages
from urllib.request import urlopen
import json
from datetime import datetime
from methods import getUserInfo,findAvailableMonths,convertTimeRange


# find the current time
current_time = datetime.now()

user_Info = getUserInfo()
hemisphere = user_Info[0]
language = user_Info[1]


# create a json object with our api
json_obj = urlopen('https://acnhapi.com/v1a/fish')
data = json.load(json_obj)

# create the final dictionary
available_fishes_information = {}
available_fishes_prices = {}

for x in data:
    # gather information about the fish
    fish_name = x['name'][language]
    fish_price = x['price']
    fish_location = x['availability']['location']

    # if the fish is not available all year, find months
    available_months = 'allYear'
    if not x['availability']["isAllYear"]:
        # create a string with the name of each month the fish is available

        available_months = findAvailableMonths(x['availability'][hemisphere])

    # if the fish is not available all day
    time_frame = 'allDay'
    if not x['availability']["isAllDay"]:
        time_frame = convertTimeRange(x['availability']['time'])

    # check to see if the fish is available this month
    if (current_time.strftime('%B') in available_months) or (available_months == 'allYear'):
        # check to see if the fish is available at this time
        if (str(',' + current_time.strftime('%H') + ',') in time_frame) or (time_frame == 'allDay'):
            # add to a dictionary
            available_fishes_information[fish_name] = fish_location
            available_fishes_prices[fish_name] = fish_price


print('fish currently available (price highest to lowest): ')
# sort the dictionary by fish prices and find the corresponding information in the other dictionary
for x in sorted(available_fishes_prices.items(), key=lambda item: item[1], reverse=True):
    print('name: {0:18} | location: {1:30} | cost: {2:7}'.format(x[0], available_fishes_information[x[0]],
                                                                 str(available_fishes_prices[x[0]])))
