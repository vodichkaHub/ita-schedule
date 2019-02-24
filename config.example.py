APP_NAME = "ita-schedule"

GOOGLE_EMAIL = "" # Вписать свой goole email

SCHEDULE_URL = "http://ictis.sfedu.ru/rasp/HTML/<свой ИД>" # Ссылка с сайта ictis

CALENDAR_ID = "primary" # Изменить, если календарей несколько

TIMEZONE = "Europe/Moscow"

# Права для приложения
GOOGLE_SCOPES = ["https://www.googleapis.com/auth/userinfo.email",
                "https://www.googleapis.com/auth/userinfo.profile",
                "https://www.googleapis.com/auth/calendar",
                ]

# Цвет для всех пар. Вписать цифру.
# 1: "#a4bdfc"  |  2: "#7ae7bf"  |  3: "#dbadff"  |  4: "#ff887c"  |  5: "#fbd75b"  |
# 6: "#ffb878"  |  7: "#46d6db"  |  8: "#e1e1e1"  |  9: "#5484ed"  |  10: "#51b749"  |  11: "#dc2127"
EVENTS_COLOR = "10"

# "opaque" - Default value. The event does block time on the calendar. This is equivalent to setting Show me as to Busy in the Calendar UI.
# "transparent" - The event does not block time on the calendar. This is equivalent to setting Show me as to Available in the Calendar UI.
TRANSPARENCY = "opaque"

# "default" - Uses the default visibility for events on the calendar. This is the default value.
# "public" - The event is public and event details are visible to all readers of the calendar.
# "private" - The event is private and only event attendees may view event details.
# "confidential" - The event is private. This value is provided for compatibility reasons.
VISIBILITY = "public"

# Количество минут до пары для напоминания. min = 0, max = 40320 (4 недели)
REMINDER_MINUTES_BEFORE = 15
