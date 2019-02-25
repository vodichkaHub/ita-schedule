from __future__ import print_function
import datetime
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import config


def get_google_service():
    creds = None
    current_dir_name = os.path.dirname(os.path.realpath(__file__))
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(current_dir_name + '/token.pickle'):
        with open(current_dir_name + '/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                current_dir_name + '/credentials.json', scopes=config.GOOGLE_SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open(current_dir_name + '/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)


def insert_events(service, schedule: list):
    current_dir_name = os.path.dirname(os.path.realpath(__file__))
    if not os.path.exists(os.path.dirname(current_dir_name + '/logs/')):
        try:
            os.makedirs(os.path.dirname(current_dir_name + '/logs/'))
        except Exception as ex: # Guard against race condition
            raise
    for day in schedule:
        try:
            res = service.events().insert(calendarId=config.CALENDAR_ID, body=day).execute()
            log_message('  INFO  ' + str(res))
        except Exception as ex:
            log_message('  ERROR  ' + str(ex))
            pass


def get_calendar_colors(service):
    return service.colors().get().execute()


def get_events(service):
    from_time = (datetime.datetime.now() - datetime.timedelta(weeks=1)).isoformat() + 'Z'
    to_time = (datetime.datetime.now() + datetime.timedelta(weeks=5)).isoformat() + 'Z'
    events_result = service.events().list(calendarId=config.CALENDAR_ID, timeMin=from_time, timeMax=to_time, singleEvents=True, orderBy='startTime').execute()

    return events_result.get('items', [])


def find_and_replace_collisions(events_from_calendar: list, events_to_insert: list):
    result = []
    for exist_event in events_from_calendar:
        for day in events_to_insert:
            for insert_event in day:
                if event_already_exists(exist_event, insert_event):
                    insert_event['id'] = exist_event['id']
                if insert_event not in result: result.append(insert_event)

    return result


def event_already_exists(e_event: dict, i_event: dict):
    return (e_event['end']['dateTime'] == i_event['end']['dateTime'] + '+03:00') \
            & (e_event['start']['dateTime'] == i_event['start']['dateTime'] + '+03:00') \
            & (e_event['summary'] == i_event['summary'])


def test(service):
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(event)


def log_message(message):
    current_dir_name = os.path.dirname(os.path.realpath(__file__))
    with open(current_dir_name + "/logs/main-log-" + str(datetime.datetime.now().strftime("%d-%m-%y")) + ".log", "a+") as log:
                log.write(str(datetime.datetime.now().isoformat()) + message + "\n\n")
