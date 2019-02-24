from bs4 import BeautifulSoup
from urllib import request as request
from datetime import datetime as dt
import config
import ita_schedule_parser
import google_api_service


response = request.urlopen(config.SCHEDULE_URL)

soup = BeautifulSoup(response.read(), "html.parser")

schedule = ita_schedule_parser.get_info_from_ita_source(soup)
service = google_api_service.get_google_service()
# print(google_api_service.get_calendar_colors(service))

google_api_service.insert_events(service, schedule)



