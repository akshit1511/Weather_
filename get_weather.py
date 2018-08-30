import urllib.request
import urllib.parse

global citylen
import datetime
def weather_response(location, API_key):
    content = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID='+API_key )
    #This was to extract data from the url
    json = content.read().decode()
    return json
   

def has_error(location,json):
    
    
    error_loc = json.find('name') # checking if the cityname entered exists in the string
    citylen = len(location)
    
    if( json[error_loc +7 : error_loc +7+ citylen] != location):
    	return(True)
    else:
    	return(False) 



def get_temperature (json, n, t):
    
     datentime = datetime.datetime.today() + datetime.timedelta(days = n)
     str_date = str(datentime)
     date = json.find(str_date[:10] + ' '+ t)
    
     #finding the reqd date and time in the json string
     temp = json.find('temp', date) #finding temperature written next to date n time
     return float(json[temp + 6 : temp + 12])




def get_humidity(json, n, t):
     datentime = datetime.datetime.today() + datetime.timedelta(days = n)
     str_date = str(datentime)
     date = json.find(str_date[:10] + " " +t)
     
     humidity = json.find('humidity', date)
     n = float(json[humidity+10:humidity+12])
     if n!=10:
        return n
    else:
     return float(json[humidity+10:humidity+13]) 

def get_pressure(json, n, t):
     datentime = datetime.datetime.today() + datetime.timedelta(days = n)
     str_date = str(datentime)
     date = json.find(str_date[:10] + ' ' + t)
     pressure = json.find('pressure', date)
     return float(json[pressure+10:pressure+15])

def get_wind(json, n, t):
     datentime = datetime.datetime.today() + datetime.timedelta(days = n)
     str_date = str(datentime)
     date = json.find(str_date[:10] + ' ' + t)
     wind = json.find('wind', date)
     return float(json[wind+15:wind+18])

def get_sealevel(json, n, t):
     datentime = datetime.datetime.today() + datetime.timedelta(days = n)
     str_date = str(datentime)
     date = json.find(str_date[:10]+' '+ t)
     sealvl = json.find('sea', date)

     return float(json[sealvl + 11 : sealvl + 18])



location = input("location - ")
print(get_temperature (weather_response(location,'cb5980b863904caf30c76a9a617610c5'), 3, '18:00:00'))
# print(get_humidity(weather_response(location,API_key), 3, '12:00:00'))
# print(get_pressure(weather_response(location,API_key), 3, '12:00:00'))
# print(get_wind(weather_response('weather','cb5980b863904caf30c76a9a617610c5'), 3, '12:00:00'))
# print(get_sealevel(weather_response('weather','cb5980b863904caf30c76a9a617610c5'), 4, '12:00:00'))
