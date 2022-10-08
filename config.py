BOT_API_TOKEN = '5637414693:AAEefxi0ZxcduloY7cinpNWi4g_WwOglQEs'
WEATHER_API_KEY = '8537d9ef6386cb97156fd47d832f479c'

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + WEATHER_API_KEY + '&units=metric'
)
