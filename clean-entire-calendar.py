import google_api_service

service = google_api_service.get_google_service()

google_api_service.clean_all_events_by_color_id(service)

