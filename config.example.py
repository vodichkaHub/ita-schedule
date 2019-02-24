APP_NAME = 'ita-schedule'

GOOGLE_EMAIL = '' # Впиши свой goole email

SCHEDULE_URL = 'http://ictis.sfedu.ru/rasp/HTML/<свой ИД>' # ссылка с сайта ictis

CALENDAR_ID = 'primary' # Изменить, если календарей несколько

TIMEZONE = 'Europe/Moscow'

# Права для приложения
GOOGLE_SCOPES = ['https://www.googleapis.com/auth/userinfo.email',
                'https://www.googleapis.com/auth/userinfo.profile',
                'https://www.googleapis.com/auth/calendar',
                ]

# Цвет для всех пар. Вписать цифру.
# 1: "#a4bdfc"  |  2: "#7ae7bf"  |  3: "#dbadff"  |  4: "#ff887c"  |  5: "#fbd75b"  |
# 6: "#ffb878"  |  7: "#46d6db"  |  8: "#e1e1e1"  |  9: "#5484ed"  |  10: "#51b749"  |  11: "#dc2127"
EVENTS_COLOR = "10"
