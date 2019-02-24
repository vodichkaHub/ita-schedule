from bs4 import BeautifulSoup
from urllib import request as request
import config
import ita_schedule_parser
import google_api_service


response = request.urlopen(config.SCHEDULE_URL)

soup = BeautifulSoup(response.read(), "html.parser")

schedule = ita_schedule_parser.get_info_from_ita_source(soup)
service = google_api_service.get_google_service()
schedule_with_ids = google_api_service.find_and_replace_collisions(google_api_service.get_events(service), schedule)
google_api_service.insert_events(service, schedule_with_ids)
