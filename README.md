# ИТА расписание - синхронизация с Google календарь

Приложение тянет с сайта ictis.sfedu.ru расписание в календарь.
## Инструкция
1. ### Установка Python
    Требование: >= Python 3.*
    >https://www.python.org/downloads/

2. ### Установка Anaconda
    Требование:  >= Anaconda3
    >https://www.anaconda.com/distribution/

3. ### Стянуть проект
    `git clone https://github.com/vodichkaHub/ita-schedule.git`

    Либо скачать архив:
    >https://github.com/vodichkaHub/ita-schedule/archive/master.zip

4. ### Создать окружение из файла env.yml
    `conda env create --name envname -f=env.yml`

    Активировать окружение.

5. ### Создать приложение Google
    >https://console.cloud.google.com
    - Создать приложение и авторизовать его, получив файл `credentials.json`.
    - Разрешить Google Calendar API.
    - Положить файл `credentials.json` в папку с проектом (рядом с `exec.py`)

6. ### Настроить проект
    - Переименовать файл `config.example.py` в `config.py`.
    - Изменить нужные поля на свое усмотрение. Некоторые из них предустановлены: можно оставить без изменений.

7. ### Запустить `exec.py`
    Я поместил этот скрипт в планировщик. Запуск раз в день.
    
Вопросы можно в телеграмм: @Wadimich
