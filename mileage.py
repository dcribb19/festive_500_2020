# mileage.py
# Visualize cycling stats for Rapha Festive 500 (2020) on Strava.

import csv
from datetime import date, datetime
from matplotlib import pyplot as plt
import numpy as np
import os.path
from typing import Dict, List

graph_path = os.path.join(os.getcwd(), 'graphs/')

TODAY = date.today()
REPORT_SUFFIX = TODAY.strftime('%m_%d')
GOAL = 500
DAILY_GOAL = round(GOAL / 8, 1)

festive_dates = [date(2020, 12, x) for x in range(24, 32)]
pace = [round(DAILY_GOAL * x, 1) for x in range(1, 9)]

outside = {}
zwift = {}


def read_csv(filename):
    '''
    Read csv file to add ride stats to dicts
    '''
    with open(filename, 'r', newline='') as csvfile:
        ride_reader = csv.reader(csvfile)
        for row in ride_reader:
            date_csv = datetime.strptime(row[0], '%Y-%m-%d').date()
            miles = float(row[1])
            location = row[2]
            if location == 'outside':
                outside[date_csv] = miles
            else:  # location == 'zwift'
                zwift[date_csv] = miles
    return outside, zwift


def format_dates(dates: List[date]) -> List[str]:
    '''
    Take list of dates and return list of strings for xlabels
    '''
    return sorted(set([day.strftime('%b-%d') for day in dates]))


def format_dict_dates(a_dict: Dict[date, int]) -> Dict[date, int]:
    '''
    Add date and set miles to 0 if no ride on day.
    Must be in challenge timeframe to work.
    '''
    for day in festive_dates:
        if day not in a_dict.keys() and day <= TODAY:
            a_dict[day] = 0
    return a_dict


def bar_stats():
    '''
    plot mileage as stacked bar chart

    Turn dicts into sorted listed of tuples (date, km)
    after formatting dict with dict[date] = 0 if date not in dict
    '''
    outside_bar = sorted(format_dict_dates(outside).items())
    zwift_bar = sorted(format_dict_dates(zwift).items())

    dates = format_dates([x[0] for x in outside_bar])
    dates = np.array(dates)
    # Take sorted list and convert to np.array
    z = np.array([x[1] for x in zwift_bar])
    o = np.array([x[1] for x in outside_bar])
    # z = [0 for _ in range(8)]  # FOR TESTING
    # o = [0 for _ in range(8)]  # FOR TESTING
    plt.figure(1)
    plt.bar(dates, z, label='Zwift', bottom=o, color='green')
    plt.bar(dates, o, label='Outside', color='red')

    # Plot horizontal line representing daily pace needed.
    plt.axhline(DAILY_GOAL, linestyle='--', label='Goal Pace', color='r')

    # Placeholder to correctly space xticks
    # while dates is not full range of festive_dates
    plt.bar(format_dates(festive_dates), [0 for _ in festive_dates])

    plt.title('Daily Kilometers Ridden - December 24-31, 2020')
    plt.xticks(format_dates(festive_dates))
    plt.xticks(rotation=45)
    plt.ylabel('Kilometers')
    plt.yticks(np.arange(0, 101, 10))
    plt.legend()
    # Save image in graph folder
    bar_path = os.path.join(graph_path, f'bar_stats_{REPORT_SUFFIX}.jpg')
    plt.savefig(bar_path, bbox_inches='tight', dpi=300)


def pace_stats():
    '''
    Plot line graph of miles ridden vs. pace
    '''
    plt.figure(2)
    # Goal pace line
    plt.plot(format_dates(festive_dates),
             pace,
             '--',
             label='Goal Pace',
             color='red')

    # Current stats line
    o = format_dict_dates(outside)
    z = format_dict_dates(zwift)
    x = np.array(format_dates(list(o.keys())))
    y = []
    running_total = 0

    daily_km = np.array(
            [o[day] + z[day] for day in festive_dates if day <= TODAY]
        )
    for day in daily_km:
        running_total += day
        y.append(running_total)

    if len(y) == 1:
        plt.scatter(x, y, s=30, c='g', marker='_', label='km Ridden')
    else:
        plt.plot(x, y, 'g', label='km Ridden')
    plt.title('Kilometers Ridden - December 24-31, 2020')
    plt.xticks(rotation=45)
    plt.xticks(np.arange(0, 8))
    plt.ylabel('Kilometers (Total)')
    plt.legend()
    # plt.show()  # FOR TESTING
    # Save image in graphs folder
    pace_path = os.path.join(
                    graph_path, f'pace_stats_{REPORT_SUFFIX}.jpg'
                )
    plt.savefig(pace_path, bbox_inches='tight', dpi=300)


def current_stats() -> str:
    '''
    Return string representation of current stats
    '''
    TODAY = date.today()
    # Do not let date go past Dec 31
    current_stats = ''
    if TODAY > date(2021, 1, 1):
        TODAY = date(2021, 1, 1)

    km_ridden = round(sum(outside.values()) + sum(zwift.values()), 1)
    remaining = round(GOAL - km_ridden, 1)
    days_left = date(2020, 12, 31) - TODAY

    if TODAY in festive_dates:
        daily_pace = pace[festive_dates.index(TODAY)]
    else:
        daily_pace = 0

    percentage = round((km_ridden / GOAL) * 100, 1)

    current_stats = (f'As of {TODAY.strftime("%b %d, %Y")} -\n'
                     f'{km_ridden} kilometers ridden. ({percentage}'
                     '% complete)\n')

    if km_ridden > GOAL:
        current_stats += 'Challenge Completed!\n'

    if days_left.days <= 0:
        current_stats += 'Festive 500 is over. Good effort!\n'
    else:
        current_stats += (f'{days_left.days} days left. {remaining}'
                          'km remaining. ('
                          f'{round(remaining / days_left.days, 1)}'
                          'km/day)\n')
        if km_ridden > daily_pace:
            current_stats += str(round(km_ridden - daily_pace, 1))
            current_stats += 'km ahead of schedule.'
        else:
            current_stats += str(round(km_ridden - daily_pace, 1))
            current_stats += 'km behind schedule.'
    return current_stats


def print_current_stats(current_stats: str):
    '''
    Print text representation of current stats
    '''
    for line in current_stats.splitlines():
        print(line)
