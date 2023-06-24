import csv
from datetime import datetime
import statistics
import operator

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    datetime_string = datetime.fromisoformat(iso_string)
    date_format = datetime_string.strftime("%A %d %B %Y")
    return date_format
pass

def convert_f_to_c(temp_in_farenheit):
    temp = round((float(temp_in_farenheit) - 32) * 5/9, 1)
    return temp
pass

def calculate_mean(weather_data):
    mean_list = list(map(float, weather_data))
    mean = statistics.mean(mean_list)
    return mean
pass

def load_data_from_csv(csv_file):
    data = []
    with open(csv_file) as myfile:
        csv_reader = csv.reader(myfile)
        next(csv_reader, None)
        for row in csv_reader:
            if row:
                integers = [int(value) if len(value) < 4 else value for value in row]
                data.append(integers)
    return data
    pass

def find_min(weather_data):
    if len(weather_data) == 0:
        return ()
    min_value = float(weather_data[0])
    min_index = 0
    if len(weather_data) > 0:
        for index, temp in enumerate(weather_data):
            if float(temp) <= min_value:
                min_value = float(temp)
                min_index = index
        return (min_value, min_index)
pass

def find_max(weather_data):
    if len(weather_data) == 0:
        return ()
    max_value = float(weather_data[0])
    max_index = 0
    if len(weather_data) > 0:
        for index, temp in enumerate(weather_data):
            if float(temp) >= max_value:
                max_value = float(temp)
                max_index = index
        return (max_value, max_index)
pass

def generate_summary(weather_data):
    summary = ""
    if len(weather_data) > 0:
        overview = f"{len(weather_data)}"
        min_temp, min_index = find_min([day[1] for day in weather_data])
        max_temp, max_index = find_max([day[2] for day in weather_data])
        avarage_low = calculate_mean(day[1] for day in weather_data)
        average_high = calculate_mean(day[2] for day in weather_data)
        minimum_day = convert_date(weather_data[min_index][0])
        maximum_day = convert_date(weather_data[max_index][0])
        summary += f"{overview} Day Overview\n  The lowest temperature will be {format_temperature(convert_f_to_c(min_temp))}, and will occur on {minimum_day}.\n  The highest temperature will be {format_temperature(convert_f_to_c(max_temp))}, and will occur on {maximum_day}.\n  The average low this week is {format_temperature(convert_f_to_c(avarage_low))}.\n  The average high this week is {format_temperature(convert_f_to_c(average_high))}.\n"
        return summary
pass

def generate_daily_summary(weather_data):
    summary = ""
    for val in weather_data:
        line_1 = "---- " + convert_date(val[0]) + " ----"
        minimum_temp = format_temperature(convert_f_to_c(val[1]))
        maximum_temp = format_temperature(convert_f_to_c(val[2]))
        return_summary = f"{line_1}\n  Minimum Temperature: {minimum_temp}\n  Maximum Temperature: {maximum_temp}\n\n"
        summary += return_summary
    return summary
pass