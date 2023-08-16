weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
list_f = [(weather_c[temp_c] * 9/5) + 32 for temp_c in weather_c]
weather_f = []
keys = weather_c.keys()
i = -1

for key in weather_c:
    i += 1
    pair = (key, list_f[i])
    weather_f.append(pair)

weather_f = dict(weather_f)
print(weather_f)