import pyowm

token = 'fcc3a43d25b640bc3d8077930f33f4e5'
owm = pyowm.OWM(token)

obs = owm.weather_at_place('Saint Petersburg, RU')
w = obs.get_weather()
temp = w.get_temperature(unit='celsius')
a = w.get_wind()
b = w.get_humidity()
с = w.get_pressure()
d = obs.get_reception_time(timeformat='iso')

print(d)
print("Температура:", temp['temp'])
print("Скорость ветра:", a['speed'])
print("Влажность:", b)
print("Давление:", с['press'])

input()