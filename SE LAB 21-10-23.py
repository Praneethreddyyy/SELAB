--variable_as_static_code--
def weather_prediction (t,h,w):
  w=(0.5*t*t-0.2*h+0.1*w-15)
  if w>300:
    return "sunny",w
  elif 200<w<=300:
    return "cloudy",w
  elif 100<w<=200:
    return "rainy",w
  else 
    return "stormy",w
print(weather_prediction(20,70,15)
