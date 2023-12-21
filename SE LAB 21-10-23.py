--variable_as_static_code--
def weather_prediction (t,h,w):
  W=0.5*t*t-0.2*h+0.1*w-15
  if W>300:
    return "sunny",W
  elif 200<W<=300:
    return "cloudy",W
  elif 100<W<=200:
    return "rainy",W
  else 
    return "stormy",W
print(weather_prediction(20,70,15)
