import pytz
import datetime

country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)
localtime = datetime.datetime.now(tz=tz_to_display)

print("The time in {} is {}".format(country, localtime))
print("UTC is {}".format(datetime.datetime.utcnow()))

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]))
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            localtime=datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {} ".format(zone,localtime))
    else:
        print("\t\t No time zone defined.")