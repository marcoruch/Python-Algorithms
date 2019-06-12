sonne_im_februar = [6,2,4,0,1,5,3,6,6,3,7,8,2,7,8,6,3,7,3,6]

def beste_urlaub(weather_forecast):
    max = 0
    maxRange = ""
    span = [[0 for _ in range(6)] for _ in range(len(weather_forecast) - 5)]

    for curSpan in range(len(weather_forecast) - 5):
        for curDay in range(5):
            span[curSpan][5] += weather_forecast[curSpan + curDay]
            span[curSpan][curDay] += weather_forecast[curSpan + curDay]
        if (max < span[curSpan][5]):
            max = span[curSpan][5]
            maxRange = str(span[curSpan])
    return maxRange
            
print(beste_urlaub(sonne_im_februar))


