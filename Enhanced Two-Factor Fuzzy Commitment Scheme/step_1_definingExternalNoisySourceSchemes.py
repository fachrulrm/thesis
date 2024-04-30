from functionality import *

# ======================================================================================================================
# Reading Genuine PUF (Optimized) Dataset

responseArr      = importDataInternalNoisySource('/Users/fachrulreizamedina/Thesis Virtuoso/Implementasi/Script/Datasets_Uniformed_16.xlsx', 1000)
responseRogueArr = importDataRogueInternalNoisySource('/Users/fachrulreizamedina/Thesis Virtuoso/Implementasi/Script/Datasets_Uniformed_16.xlsx', 1000)

# ======================================================================================================================
# Defining External Noisy Sources Schemes & Baseline per Scheme

# Scheme 1 : Genuine PUF (Optimized) & Genuine External Noisy Source

rectorate_building = [
    "25", "107.6304210", "-6.9739385", "0665"
] # temperature, longitude, lattitude, altitude

# Scheme 2 : Genuine PUF (Optimized) & Genuine External Noisy Source with Fluctuative Temperature

rectorate_building_fluctuative_temperature = [
    "31", "107.6304210", "-6.9739385", "0665"
] # temperature, longitude, lattitude, altitude

# Scheme 3 : Genuine PUF (Optimized) & Genuine External Noisy Source with Fluctuative Temperature and Slightly Moved

rectorate_building_fluctuative_temperature_slightly_moved = [
    "29", "107.6304264", "-6.9739335", "0665"
]

# Scheme 4 : Genuine PUF (Optimized) & Attacker External Noisy Source (Different Building, Same Area)

l_building = [
    "25", "107.6296244", "-6.9735577", "0666"
] # temperature, longitude, lattitude, altitude

# Scheme 5 : Genuine PUF (Optimized) & Attacker External Noisy Source (Different Building, Same Area) with Fluctuative Temperature

l_building_fluctuative_temperature = [
    "23", "107.6296244", "-6.9735577", "0666"
] # temperature, longitude, lattitude, altitude

# Scheme 6 : Genuine PUF (Optimized) & Attacker External Noisy Source (Another City)

another_city = [
    "25", "108.0076775", "-7.2946701", "0903"
] # temperature, longitude, lattitude, altitude

# Scheme 7 : Genuine PUF (Optimized) & Attacker External Noisy Source (Another City) with Fluctuative Temperature

another_city_fluctuative_temperature = [
    "20", "108.0076775", "-7.2946701", "0903"
] # temperature, longitude, lattitude, altitude

# Scheme 8 : Genuine PUF (Optimized) & Attacker External Noisy Source (Another Regional)

another_region = [
    "25", "120.9823318", "1.2057738", "0829"
] # temperature, longitude, lattitude, altitude

# Scheme 9 : Genuine PUF (Optimized) & Attacker External Noisy Source (Another Regional) with Fluctuative Temperature

another_region_fluctuative_temperature = [
    "22", "120.9823318", "1.2057738", "0829"
] # temperature, longitude, lattitude, altitude

# ======================================================================================================================
# Creating New Biometric Based-on Internal & External Noisy Sources

combinedBiometric_rectorate_building = \
    integratingBiometrics(responseArr, convertingExternalNoisySource_String_to_Binary(rectorate_building))

combinedBiometric_rectorate_building_fluctuative_temperature = \
    integratingBiometrics(responseArr, convertingExternalNoisySource_String_to_Binary(rectorate_building_fluctuative_temperature))

combinedBiometric_rectorate_building_fluctuative_temperature_slightly_moved = \
    integratingBiometrics(responseArr, convertingExternalNoisySource_String_to_Binary(rectorate_building_fluctuative_temperature_slightly_moved))

combinedBiometric_l_building = \
    integratingBiometrics(responseRogueArr, convertingExternalNoisySource_String_to_Binary(l_building))

combinedBiometric_l_building_fluctuative_temperature = \
    integratingBiometrics(responseRogueArr, convertingExternalNoisySource_String_to_Binary(l_building_fluctuative_temperature))

combinedBiometric_another_city = \
    integratingBiometrics(responseRogueArr, convertingExternalNoisySource_String_to_Binary(another_city))

combinedBiometric_another_city_fluctuative_temperature = \
    integratingBiometrics(responseRogueArr, convertingExternalNoisySource_String_to_Binary(another_city_fluctuative_temperature))

combinedBiometric_another_region = \
    integratingBiometrics(responseRogueArr, convertingExternalNoisySource_String_to_Binary(another_region))

combinedBiometric_another_region_fluctuative_temperature = \
    integratingBiometrics(responseRogueArr, convertingExternalNoisySource_String_to_Binary(another_region_fluctuative_temperature))

# print(hammingDistance(convertingExternalNoisySource_String_to_Binary(rectorate_building), convertingExternalNoisySource_String_to_Binary(another_region_fluctuative_temperature)))