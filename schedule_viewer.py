import requests
import pandas as pd
import datetime

TIME_COLUMN = 'Godziny:'
SCHEDULE_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vShWufZ2H6t7U7fOH_9g00UWiQ0F64pUA26k96ySwrbpVlnSTiFeH8O49iHXg6QK_qfSLsFfDJfpguc/pub?gid=0&single=true&output=csv"

# function parsing names of the days of the week from the sheet
def parse_day_name(index):
    for elem in reversed(index):
        for letter in elem:
            if not letter.isalpha():
                index.remove(elem)
                break

    return index

# returns dict containing (hour: course) pairs
def parse_column(key, schedule):
    times = schedule[TIME_COLUMN].to_list()
    possible_courses = schedule[key].to_list()
    
    possible_courses_dict = dict(zip(times, possible_courses))
    todays_courses = {key: value for (key, value) in possible_courses_dict.items() if value != '-'}

    return todays_courses

def main():
    # getting current day of the week
    current_day = datetime.datetime.today().weekday()

    schedule = pd.read_csv(SCHEDULE_URL, encoding='UTF-8').fillna('-')

    index = schedule.axes[1].to_list()
    parsed_index = parse_day_name(index)

    current_day_name = parsed_index[current_day]
    
    parse_column(current_day_name, schedule)

if __name__ == '__main__':
    main()