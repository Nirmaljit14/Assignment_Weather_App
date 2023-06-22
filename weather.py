import csv
from datetime import datetime
import statistics
import operator

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


# def format_temperature(temp):
#     #user_input = float(input("Please emter the temprature "))
#     temp = user_input * 9/5 + 32
#     return f"{temp}{DEGREE_SYBMOL}"

# # results = format_temperature(user_input)
# # print(results)


# def convert_date(iso_string):
#     datetime_str = datetime.fromisoformat(iso_string)
#     date_format = datetime_str.strftime("%A %d %B %Y")
#     return date_format
# pass


# def convert_f_to_c(temp_in_farenheit):
#     temp = round((float(temp_in_farenheit) - 32) * 5/9, 1)
#     return temp
# pass


# def calculate_mean(weather_data):
#     mean_list = list(map(float, weather_data))
#     mean = statistics.mean(mean_list)
#     print(mean)
#     return mean
# pass


# def load_data_from_csv(csv_file):
#     data = []
#     with open(csv_file) as myfile:
#         csv_reader = csv.reader(myfile)
#         next(csv_reader, None)
#         for row in csv_reader:
#             if row:
#                 integers = [int(value) if len(value) < 4 else value for value in row]
#                 data.append(integers)
#     return data
#     pass


# def find_min(weather_data):

#     if len(weather_data) == 0:
#         return ()

#     min_value = float(weather_data[0])
#     min_index = 0

#     if len(weather_data) > 0:
#         for index, temp in enumerate(weather_data):
#             if float(temp) <= min_value:
#                 min_value = float(temp)
#                 min_index = index
#         return (min_value, min_index)

# pass


# def find_max(weather_data):
#     if len(weather_data) == 0:
#         return ()

#     max_value = float(weather_data[0])
#     max_index = 0

#     if len(weather_data) > 0:
#         for index, temp in enumerate(weather_data):
#             if float(temp) >= max_value:
#                 max_value = float(temp)
#                 max_index = index
#         return (max_value, max_index)
# pass


def generate_summary(weather_data):

        if not weather_data:
            return "No weather data available."
            summary_list=()
            min_temp_day = find_min(weather_data, key=lambda day: day[1])
            max_temp_day = find_max(weather_data, key=lambda day: day[2])
            avg_low = sum(day[1] for day in weather_data) / len(weather_data)
            avg_high = sum(day[2] for day in weather_data) / len(weather_data)
            summary = f"The lowest temperature will be {min_temp_day[1]}°C, and will occur on {min_temp_day[0].strftime('%A %d %B %Y')}.\n" 
            f"The highest temperature will be {max_temp_day[2]}°C, and will occur on {max_temp_day[0].strftime('%A %d %B %Y')}.\n" \
                f"The average low this week is {avg_low:.1f}°C.\n" \
                    f"The average high this week is {avg_high:.1f}°C."
            return summary
            print(summary)
    # """Outputs a summary for the given weather data.

    # Args:
    #     weather_data: A list of lists, where each sublist represents a day of weather data.
    # Returns:
    #     A string containing the summary information.
    #"""
        pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass

# start from whAt YOU NEED TO WHAT YOU HAVE 
# DO NOT LOAD CSV IN SUMMARY
# DO NOT TIUCH AKREADY PERFOMRED FUNCTIONS