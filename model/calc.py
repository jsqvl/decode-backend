import random
import math

def calcSustainability(brand, cloth_type, materials):
    brand_weight = 0.4
    materials_weight = 0.4

    return 1

# Should take into account factory locations and partners
def calcBrandQuality(brand):
    return 100*random.random()


def calcFabricQuality(brand, materials):
    brand_weight = 0.5
    brand_quality = calcBrandQuality(brand) * brand_weight

    material_weight = 0.5
    material_quality = 0

    sum = 0
    scaled_x = 0
    count = 0
    vector_f = []
    for i in materials:
        x = i.split(": ")
        if len(x[1]) == 2:
            y = x[1][0 : 1]
        else:
            y = x[1][0 : 2]
        
        count += 1
        # 1 - 10 worst to best scale fabric quality, for now, random
        scaled_x += int(y)*10*random.random()
        sum += int(scaled_x)
        vector_f.append(int(scaled_x))

    mag_vec = 0
    vector_f_copy = vector_f
    for i in vector_f:
        i *= i
        mag_vec += i

    math.sqrt(mag_vec)
    
    for i in vector_f_copy:
        i /= mag_vec
        material_quality += i
    
    return brand_quality + material_quality

def calcNumOfWashes(materials):

    return 125

def start_calc(brand, cloth_type, materials, num_washes, weight):

    return [calcSustainability(calc), calcFabricQuality(str_data), calcNumOfWashes(str_data)]