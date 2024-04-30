from step_1_definingExternalNoisySourceSchemes import *
import random

# ======================================================================================================================
# Generating External Noisy Sources Dataset (100 entries per scheme)

datasetPerScheme = 100

# First Scheme does not have variance. It is the baseline

# Defining Dataset for the Second Scheme
variance_rectorate_building_fluctuative_temperature = []

for i in range(datasetPerScheme):
    baselineTemperature     = str(random.randint(18,31)) # 18 up to 31 is the minimum and maximum Bandung's temperature on November 2022. See https://bandungkota.bps.go.id/indicator/151/1248/1/temperatur-derajat-celcius-per-bulan-di-kota-bandung.html
    baselineLongitude       = rectorate_building[1]
    baselineLattitude       = rectorate_building[2]
    baselineAltitude        = rectorate_building[3]

    variance_rectorate_building_fluctuative_temperature.append([
        baselineTemperature, baselineLongitude, baselineLattitude, baselineAltitude
    ])

# Defining Dataset for the Third Scheme
variance_rectorate_building_fluctuative_temperature_slightly_moved = [] # Moved less than 1.11 meters for longitude (horizontal) and 1.11 meters for lattitude (vertical)

for i in range(datasetPerScheme):
    baselineTemperature = str(random.randint(18,31))  # 18 up to 31 is the minimum and maximum Bandung's temperature on November 2022. See https://bandungkota.bps.go.id/indicator/151/1248/1/temperatur-derajat-celcius-per-bulan-di-kota-bandung.html
    baselineLongitude   = "107.63042"+str(random.randint(0, 9))+str(random.randint(0, 9))
    baselineLattitude   = "-6.97393"+str(random.randint(0, 9))+str(random.randint(0, 9))
    baselineAltitude    = rectorate_building[3]

    variance_rectorate_building_fluctuative_temperature_slightly_moved.append([
        baselineTemperature, baselineLongitude, baselineLattitude, baselineAltitude
    ])

# Defining Dataset for the Fourth Scheme
variance_l_building = [] # Moved less than 11.1 meters for longitude (horizontal) and 11.1 meters for lattitude (vertical)

for i in range(datasetPerScheme):
    baselineTemperature = rectorate_building[0]
    baselineLongitude   = "107.6296"+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))
    baselineLattitude   = "-6.9735"+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))
    baselineAltitude    = "0666"

    variance_l_building.append([
        baselineTemperature, baselineLongitude, baselineLattitude, baselineAltitude
    ])

# Defining Dataset for the Fifth Scheme
variance_l_building_fluctuative_temperature = [] # Moved less than 11.1 meters for longitude (horizontal) and 11.1 meters for lattitude (vertical)

for i in range(datasetPerScheme):
    baselineTemperature = str(random.randint(18,31))  # 18 up to 31 is the minimum and maximum Bandung's temperature on November 2022. See https://bandungkota.bps.go.id/indicator/151/1248/1/temperatur-derajat-celcius-per-bulan-di-kota-bandung.html
    baselineLongitude   = "107.6296"+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))
    baselineLattitude   = "-6.9735"+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))
    baselineAltitude    = "0666"

    variance_l_building_fluctuative_temperature.append([
        baselineTemperature, baselineLongitude, baselineLattitude, baselineAltitude
    ])

# Defining Dataset for the Sixth Scheme
variance_another_city = [] # Moved less than 11.1 km for longitude (horizontal) and 11.1 km for lattitude (vertical)

for i in range(datasetPerScheme):
    baselineTemperature  = rectorate_building[0]
    baselineLongitude    = "108.0" + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    baselineLattitude    = "-7.2" + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    baselineAltitude     = "0903"

    variance_another_city.append([
        baselineTemperature, baselineLongitude, baselineLattitude, baselineAltitude
    ])

# Defining Dataset for the Seventh Scheme
variance_another_city_fluctuative_temperature = [] # Moved less than 11.1 km for longitude (horizontal) and 11.1 km for lattitude (vertical)

for i in range(datasetPerScheme):
    baselineTemperature = str(random.randint(20,31))  # 20 up to 31 is the minimum and maximum Tasikmalaya's temperature on November 2021. See https://tasikmalayakota.bps.go.id/indicator/151/131/1/suhu.html
    baselineLongitude = "108.0" + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
        random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    baselineLattitude = "-7.2" + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
        random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    baselineAltitude = "0903"

    variance_another_city_fluctuative_temperature.append([
        baselineTemperature, baselineLongitude, baselineLattitude, baselineAltitude
    ])

# Defining Dataset for the Eighth Scheme
variance_another_region = [] # Moved less than 11.1 km for longitude (horizontal) and 11.1 km for lattitude (vertical)

for i in range(datasetPerScheme):
    baselineTemperature = rectorate_building[0]
    baselineLongitude = "120.9" + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
        random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    baselineLattitude = "1.2" + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
        random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    baselineAltitude = "0829"

    variance_another_region.append([
        baselineTemperature, baselineLongitude, baselineLattitude, baselineAltitude
    ])

# Defining Dataset for the Nineth Scheme
variance_another_region_fluctuative_temperature = []

for i in range(datasetPerScheme):
    baselineTemperature = str(random.randint(17,29))  # 17 up to 29 is the minimum and maximum North Sulawesi's temperature on 2022. See https://sulut.bps.go.id/indicator/151/926/1/suhu-menurut-stasiun-pengamatan-bmkg.html
    baselineLongitude = "120.9" + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
        random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    baselineLattitude = "1.2" + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
        random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    baselineAltitude = "0829"

    variance_another_region_fluctuative_temperature.append([
        baselineTemperature, baselineLongitude, baselineLattitude, baselineAltitude
    ])

# ======================================================================================================================
# Creating New Biometric Based-on Internal & External Noisy Sources Dataset

combinedBiometric_variance_rectorate_building_fluctuative_temperature = [] # Lists inside list

for i in variance_rectorate_building_fluctuative_temperature:
    combinedBiometric_variance_rectorate_building_fluctuative_temperature.append(integratingBiometrics(responseArr, convertingExternalNoisySource_String_to_Binary(i)))

combinedBiometric_variance_rectorate_building_fluctuative_temperature_slightly_moved = [] # Lists inside list

for i in variance_rectorate_building_fluctuative_temperature_slightly_moved:
    combinedBiometric_variance_rectorate_building_fluctuative_temperature_slightly_moved.append(
        integratingBiometrics(responseArr, convertingExternalNoisySource_String_to_Binary(i)))

combinedBiometric_variance_l_building = []  # Lists inside list

for i in variance_l_building:
    combinedBiometric_variance_l_building.append(
        integratingBiometrics(responseArr, convertingExternalNoisySource_String_to_Binary(i)))

combinedBiometric_variance_l_building_fluctuative_temperature = [] # Lists inside list

for i in variance_l_building_fluctuative_temperature:
    combinedBiometric_variance_l_building_fluctuative_temperature.append(
        integratingBiometrics(responseArr, convertingExternalNoisySource_String_to_Binary(i)))

combinedBiometric_variance_another_city = []

for i in variance_another_city:
    combinedBiometric_variance_another_city.append(
        integratingBiometrics(responseArr, convertingExternalNoisySource_String_to_Binary(i)))

combinedBiometric_variance_another_city_fluctuative_temperature = []

for i in variance_another_city_fluctuative_temperature:
    combinedBiometric_variance_another_city_fluctuative_temperature.append(
        integratingBiometrics(responseArr, convertingExternalNoisySource_String_to_Binary(i)))

combinedBiometric_variance_another_region = []

for i in variance_another_region:
    combinedBiometric_variance_another_region.append(
        integratingBiometrics(responseArr, convertingExternalNoisySource_String_to_Binary(i)))

combinedBiometric_variance_another_region_fluctuative_temperature = []

for i in variance_another_region_fluctuative_temperature:
    combinedBiometric_variance_another_region_fluctuative_temperature.append(
        integratingBiometrics(responseArr, convertingExternalNoisySource_String_to_Binary(i)))