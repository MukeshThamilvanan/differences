import math


def evaluate(x,y):
    eq = (((1/(1-(x * y))) + 3)/(4 - (5 * x)))
    return eq

def piecewise(x, y):

    if x <= 0:
        return x - (2 * y)

    elif 0 < x and x <= 10:
        return ((1 - y)/x)

    elif x > 10:
        return ((y + 1) ** 2) / ( x ** 3)

def farmhouse(house_length, house_width, house_height):
    roof_width = (house_width / math.sqrt(2))
    area_body = (2 * (house_height * house_length)) + (2 * (house_height * house_width))
    area_top = (roof_width ** 2) + (2 * (house_length * roof_width))
    return (area_body + area_top)

def coinage(talents, mina, drachmae, oboloi):
    if talents < 0 or mina < 0 or drachmae < 0 or oboloi < 0:
        return (float(-1))
    else:
        a = talents * 60 * 70
        b = mina * 70
        c = oboloi * (1/6)
        return (a+b+c+drachmae)


evaluate(1,2)