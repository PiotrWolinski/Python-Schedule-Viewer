import requests
import pandas as pd
import datetime

pd.set_option('display.max_rows', None)

# simple function parsing days of the week from the sheet
def parse_index(index):
    for elem in reversed(index):
        for letter in elem:
            if not letter.isalpha():
                index.remove(elem)
                break

    return index


def parse_column(key, df):
    pass

# getting current day of the week
current_day = datetime.datetime.today().weekday()


schedule_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vShWufZ2H6t7U7fOH_9g00UWiQ0F64pUA26k96ySwrbpVlnSTiFeH8O49iHXg6QK_qfSLsFfDJfpguc/pub?gid=0&single=true&output=csv"

schedule = pd.read_csv(schedule_url, encoding='UTF-8').fillna('-')

# print(schedule['Wtorek'])
print(schedule)

index = schedule.axes[1].to_list()
parsed_index = parse_index(index)

print(parsed_index)

current_day_name = index[current_day]
print(current_day_name)