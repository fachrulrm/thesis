from functionality import *
from step_3_generatingExternalNoisySourcesDataset import datasetPerScheme

import pandas as pd
import matplotlib.pyplot as plt

# ==============================================================================================================================================
# Read Data from Excel
dataCount = datasetPerScheme

KRR_variance_rectorate_building_fluctuative_temperature = readExcelColumn(
    "/Users/fachrulreizamedina/Thesis Virtuoso/Implementasi/Script/External Noisy Source Dataset & KRR/Datasets_Ext_Scheme_2.xlsx",
    3,
    dataCount
)

KRR_variance_rectorate_building_fluctuative_temperature_slightly_moved = readExcelColumn(
    "/Users/fachrulreizamedina/Thesis Virtuoso/Implementasi/Script/External Noisy Source Dataset & KRR/Datasets_Ext_Scheme_3.xlsx",
    3,
    dataCount
)

KRR_variance_l_building = readExcelColumn(
    "/Users/fachrulreizamedina/Thesis Virtuoso/Implementasi/Script/External Noisy Source Dataset & KRR/Datasets_Ext_Scheme_4.xlsx",
    3,
    dataCount
)

KRR_variance_l_building_fluctuative_temperature = readExcelColumn(
    "/Users/fachrulreizamedina/Thesis Virtuoso/Implementasi/Script/External Noisy Source Dataset & KRR/Datasets_Ext_Scheme_5.xlsx",
    3,
    dataCount
)

KRR_variance_another_city = readExcelColumn(
    "/Users/fachrulreizamedina/Thesis Virtuoso/Implementasi/Script/External Noisy Source Dataset & KRR/Datasets_Ext_Scheme_6.xlsx",
    3,
    dataCount
)

KRR_variance_another_city_fluctuative_temperature = readExcelColumn(
    "/Users/fachrulreizamedina/Thesis Virtuoso/Implementasi/Script/External Noisy Source Dataset & KRR/Datasets_Ext_Scheme_7.xlsx",
    3,
    dataCount
)

KRR_variance_another_region = readExcelColumn(
    "/Users/fachrulreizamedina/Thesis Virtuoso/Implementasi/Script/External Noisy Source Dataset & KRR/Datasets_Ext_Scheme_8.xlsx",
    3,
    dataCount
)

KRR_variance_another_region_fluctuative_temperature = readExcelColumn(
    "/Users/fachrulreizamedina/Thesis Virtuoso/Implementasi/Script/External Noisy Source Dataset & KRR/Datasets_Ext_Scheme_9.xlsx",
    3,
    dataCount
)

# ==============================================================================================================================================
# Calculating KRR from KRR's dataset

maxCorrectedBits = 27

xLabel                             = []
yLabel_variance_rectorate_building = []

for i in range(maxCorrectedBits+1):
    xLabel.append(i)
    yLabel_variance_rectorate_building.append(100) # Since this is the genuine external noisy source WITHOUT any change
    # or interference in it. In other words, this is the baseline external noisy source (thus it should be 100% since
    # there are no error bit)

yLabel_variance_rectorate_building_fluctuative_temperature = calculatingKRRfromKRRsDataset(
    KRR_variance_rectorate_building_fluctuative_temperature,
    xLabel
)

yLabel_variance_rectorate_building_fluctuative_temperature_slightly_moved = calculatingKRRfromKRRsDataset(
    KRR_variance_rectorate_building_fluctuative_temperature_slightly_moved,
    xLabel
)

yLabel_variance_l_building = calculatingKRRfromKRRsDataset(
    KRR_variance_l_building,
    xLabel
)

yLabel_variance_l_building_fluctuative_temperature = calculatingKRRfromKRRsDataset(
    KRR_variance_l_building_fluctuative_temperature,
    xLabel
)

yLabel_variance_another_city = calculatingKRRfromKRRsDataset(
    KRR_variance_another_city,
    xLabel
)

yLabel_variance_another_city_fluctuative_temperature = calculatingKRRfromKRRsDataset(
    KRR_variance_another_city_fluctuative_temperature,
    xLabel
)

yLabel_variance_another_region = calculatingKRRfromKRRsDataset(
    KRR_variance_another_region,
    xLabel
)

yLabel_variance_another_region_fluctuative_temperature = calculatingKRRfromKRRsDataset(
    KRR_variance_another_region_fluctuative_temperature,
    xLabel
)

print("Scheme #2, KRR 100% at "+str(yLabel_variance_rectorate_building_fluctuative_temperature.index(100)))
print("Scheme #3, KRR 100% at "+str(yLabel_variance_rectorate_building_fluctuative_temperature_slightly_moved.index(100)))

print("Scheme #4, KRR 0% maximum at "+str(checkAttackerKRR(
    yLabel_variance_l_building
)))

print("Scheme #5, KRR 0% maximum at "+str(checkAttackerKRR(
    yLabel_variance_l_building_fluctuative_temperature
)))

print("Scheme #6, KRR 0% maximum at " + str(checkAttackerKRR(
    yLabel_variance_another_city
)))

print("Scheme #7, KRR 0% maximum at " + str(checkAttackerKRR(
    yLabel_variance_another_city_fluctuative_temperature
)))

print("Scheme #8, KRR 0% maximum at " + str(checkAttackerKRR(
    yLabel_variance_another_region
)))

print("Scheme #9, KRR 0% maximum at " + str(checkAttackerKRR(
    yLabel_variance_another_region_fluctuative_temperature
)))

# ==============================================================================================================================================
# Plotting line graph

data_dict = {"t-bits": xLabel,
             "Scheme #1": yLabel_variance_rectorate_building,
             "Scheme #2": yLabel_variance_rectorate_building_fluctuative_temperature,
             "Scheme #3": yLabel_variance_rectorate_building_fluctuative_temperature_slightly_moved,
             "Scheme #4": yLabel_variance_l_building,
             "Scheme #5": yLabel_variance_l_building_fluctuative_temperature,
             "Scheme #6": yLabel_variance_another_city,
             "Scheme #7": yLabel_variance_another_city_fluctuative_temperature,
             "Scheme #8": yLabel_variance_another_region,
             "Scheme #9": yLabel_variance_another_region_fluctuative_temperature,
             }

df = pd.DataFrame(data_dict)
ax = plt.gca()

df.plot(kind='line',
        x="t-bits",
        y="Scheme #1",
        color='yellowgreen',
        ax=ax)

df.plot(kind='scatter',
        x="t-bits",
        y="Scheme #1",
        color='yellowgreen',
        ax=ax)

df.plot(kind='line',
        x="t-bits",
        y="Scheme #2",
        color='greenyellow',
        ax=ax)

df.plot(kind='scatter',
        x="t-bits",
        y="Scheme #2",
        color='greenyellow',
        ax=ax)

df.plot(kind='line',
        x="t-bits",
        y="Scheme #3",
        color='lightgreen',
        ax=ax)

df.plot(kind='scatter',
        x="t-bits",
        y="Scheme #3",
        color='lightgreen',
        ax=ax)

df.plot(kind='line',
        x="t-bits",
        y="Scheme #4",
        color='gold',
        ax=ax)

df.plot(kind='scatter',
        x="t-bits",
        y="Scheme #4",
        color='gold',
        ax=ax)

df.plot(kind='line',
        x="t-bits",
        y="Scheme #5",
        color='yellow',
        ax=ax)

df.plot(kind='scatter',
        x="t-bits",
        y="Scheme #5",
        color='yellow',
        ax=ax)

df.plot(kind='line',
        x="t-bits",
        y="Scheme #6",
        color='tomato',
        ax=ax)

df.plot(kind='scatter',
        x="t-bits",
        y="Scheme #6",
        color='tomato',
        ax=ax)

df.plot(kind='line',
        x="t-bits",
        y="Scheme #7",
        color='brown',
        ax=ax)

df.plot(kind='scatter',
        x="t-bits",
        y="Scheme #7",
        color='brown',
        ax=ax)

df.plot(kind='line',
        x="t-bits",
        y="Scheme #8",
        color='lightcoral',
        ax=ax)

df.plot(kind='scatter',
        x="t-bits",
        y="Scheme #8",
        color='lightcoral',
        ax=ax)

df.plot(kind='line',
        x="t-bits",
        y="Scheme #9",
        color='red',
        ax=ax)

df.plot(kind='scatter',
        x="t-bits",
        y="Scheme #9",
        color='red',
        ax=ax)

plt.title('Line Plots')
plt.xlabel("t-bits")
plt.ylabel("KRR (%)")
plt.show()