import COVID19Py
import pprint

covid19 = COVID19Py.COVID19()

location = covid19.getLocationByCountryCode("UA")
print(location[0]["latest"])