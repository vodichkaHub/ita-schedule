import config
from bs4 import BeautifulSoup
import re
from datetime import datetime
import datetime_constants
import pytz


def get_info_from_ita_source(soup: BeautifulSoup):
    schedule = get_schedule_per_day(soup)

    return handle_schedule(schedule)


def get_week_ids(soup: BeautifulSoup):
    try:
        fonts = str(soup.find_all("font", attrs={"color": "#ff00ff"})).split('-я')
    except Exception as ex:
        print(ex)

    numbers = set()
    for font in fonts:
        if font == fonts[-1]:
            break
        numbers.add(str(font)[-2:].lstrip())

    return sorted(numbers)


def get_schedule_per_day(soup: BeautifulSoup):
    schedule_per_day = []

    firstBold = soup.b
    boldList = firstBold.find_all_next("b")

    schedule_per_day.append({'date': firstBold.p.getText().split(',')[1].rstrip()})
    next = firstBold.parent
    for i in range(6):
        next = next.find_next("td")
        if (next.p.getText()):
            schedule_per_day[0] = {**schedule_per_day[0], **{i: next.p.getText().rstrip()}}

    schedule_per_day_counter = 1
    for bold in boldList:
        schedule_per_day.append({'date': bold.p.getText().split(',')[1].rstrip()})
        next = bold.parent
        for i in range(6):
            next = next.find_next("td")
            if (next.p.getText()):
                schedule_per_day[schedule_per_day_counter] = {**schedule_per_day[schedule_per_day_counter], **{i: next.p.getText().rstrip()}}
        schedule_per_day_counter += 1

    return schedule_per_day


def handle_schedule(schedule: list):
    result = []
    for day in schedule:
        if len(day) <= 1:
            del day
        else:
            day['date'] = handle_date(day)
            result.append(sepate_day_on_classes(day))

    return result


def handle_date(day: dict):
    mounth_day = day['date'].split(' ')[0]
    mounth = datetime_constants.MOUNTHS[day['date'].split(' ')[2]]
    year = datetime.today().year

    return datetime.strptime(str(year) + '-' + mounth + '-' + mounth_day, '%Y-%m-%d')


def sepate_day_on_classes(day: dict):
    classes = []
    for item in day:
        if item == 'date':
            continue
        else:
            classes.append({
                'summary': day[item],
                'start': handle_start_time(day, item),
                'end': handle_end_time(day, item),
                'colorId': config.EVENTS_COLOR,
                'transparency': config.TRANSPARENCY,
                'visibility': config.VISIBILITY,
                'reminders.overrides[].minutes': config.REMINDER_MINUTES_BEFORE,
            })

    return classes


def handle_start_time(day: dict, class_number: int):
    start_time = datetime_constants.CLASS_TIME['start'][str(class_number)]
    hours = int(start_time.split(':')[0])
    minutes = int(start_time.split(':')[1])

    return {
        'dateTime': day['date'].replace(hour=hours, minute=minutes, tzinfo=pytz.timezone(config.TIMEZONE)).strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': config.TIMEZONE
    }


def handle_end_time(day: dict, class_number: int):
    start_time = datetime_constants.CLASS_TIME['end'][str(class_number)]
    hours = int(start_time.split(':')[0])
    minutes = int(start_time.split(':')[1])

    return {
        'dateTime': day['date'].replace(hour=hours, minute=minutes, tzinfo=pytz.timezone(config.TIMEZONE)).strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': config.TIMEZONE
    }
