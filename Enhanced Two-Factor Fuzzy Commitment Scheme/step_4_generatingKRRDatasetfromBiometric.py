from ECC import *
from step_3_generatingExternalNoisySourcesDataset import *

import openpyxl

# ======================================================================================================================
# ECC parameters

n            = 127
k            = 15
genPolyOctal = "22057042445604554770523013762217604353"

# ======================================================================================================================
# Encoding Random Bits

# Defining Random Bits
randomBits = "110100100110010"

message = convertingStringtoPolynomial(addingParityBitstoMessage(adjustingMessageLength(randomBits, k), n, k))
genPoly = convertingStringtoPolynomial(generatingGenPoly(genPolyOctal))

codeword_randomBits = "0" + convertingPolynomialtoString(
    generatingCodeword(message, polynomialDivision(message, genPoly)[1]))

# ======================================================================================================================
# Calculating h (combinedBiometric XORed with codeword_randomBits)

h_variance_rectorate_building_fluctuative_temperature = generatingHelperBitsFromVarianceDataset(
    combinedBiometric_variance_rectorate_building_fluctuative_temperature, codeword_randomBits)

h_variance_rectorate_building_fluctuative_temperature_slightly_moved = generatingHelperBitsFromVarianceDataset(
    combinedBiometric_variance_rectorate_building_fluctuative_temperature_slightly_moved, codeword_randomBits
)

h_variance_l_building = generatingHelperBitsFromVarianceDataset(
    combinedBiometric_variance_l_building, codeword_randomBits
)

h_variance_l_building_fluctuative_temperature = generatingHelperBitsFromVarianceDataset(
    combinedBiometric_variance_l_building_fluctuative_temperature, codeword_randomBits
)

h_variance_another_city = generatingHelperBitsFromVarianceDataset(
    combinedBiometric_variance_another_city, codeword_randomBits
)

h_variance_another_city_fluctuative_temperature = generatingHelperBitsFromVarianceDataset(
    combinedBiometric_variance_another_city_fluctuative_temperature, codeword_randomBits
)

h_variance_another_region = generatingHelperBitsFromVarianceDataset(
    combinedBiometric_variance_another_region, codeword_randomBits
)

h_variance_another_region_fluctuative_temperature = generatingHelperBitsFromVarianceDataset(
    combinedBiometric_variance_another_region_fluctuative_temperature, codeword_randomBits
)

# ======================================================================================================================
# Calculating received_codeword (h XORed with authentic biometric)

authenticBiometric = combinedBiometric_rectorate_building
authenticCodeword  = codeword_randomBits

receivedCodeword_variance_rectorate_building_fluctuative_temperature = generatingReceivedCodewordFromVarianceDataset(
    h_variance_rectorate_building_fluctuative_temperature, authenticBiometric
)

receivedCodeword_variance_rectorate_building_fluctuative_temperature_slightly_moved = generatingReceivedCodewordFromVarianceDataset(
    h_variance_rectorate_building_fluctuative_temperature_slightly_moved, authenticBiometric
)

receivedCodeword_variance_l_building = generatingReceivedCodewordFromVarianceDataset(
    h_variance_l_building, authenticBiometric
)

receivedCodeword_variance_l_building_fluctuative_temperature = generatingReceivedCodewordFromVarianceDataset(
    h_variance_l_building_fluctuative_temperature, authenticBiometric
)

receivedCodeword_variance_another_city = generatingReceivedCodewordFromVarianceDataset(
    h_variance_another_city, authenticBiometric
)

receivedCodeword_variance_another_city_fluctuative_temperature = generatingReceivedCodewordFromVarianceDataset(
    h_variance_another_city_fluctuative_temperature, authenticBiometric
)

receivedCodeword_variance_another_region = generatingReceivedCodewordFromVarianceDataset(
    h_variance_another_region, authenticBiometric
)

receivedCodeword_variance_another_region_fluctuative_temperature = generatingReceivedCodewordFromVarianceDataset(
    h_variance_another_region_fluctuative_temperature, authenticBiometric
)

# ======================================================================================================================
# Calculating KRR Dataset

KRR_variance_rectorate_building_fluctuative_temperature = generatingKRRFromVarianceDataset(
    receivedCodeword_variance_rectorate_building_fluctuative_temperature, authenticCodeword
)

KRR_variance_rectorate_building_fluctuative_temperature_slightly_moved = generatingKRRFromVarianceDataset(
    receivedCodeword_variance_rectorate_building_fluctuative_temperature_slightly_moved, authenticCodeword
)

KRR_variance_l_building = generatingKRRFromVarianceDataset(
    receivedCodeword_variance_l_building, authenticCodeword
)

KRR_variance_l_building_fluctuative_temperature = generatingKRRFromVarianceDataset(
    receivedCodeword_variance_l_building_fluctuative_temperature, authenticCodeword
)

KRR_variance_another_city = generatingKRRFromVarianceDataset(
    receivedCodeword_variance_another_city, authenticCodeword
)

KRR_variance_another_city_fluctuative_temperature = generatingKRRFromVarianceDataset(
    receivedCodeword_variance_another_city_fluctuative_temperature, authenticCodeword
)

KRR_variance_another_region = generatingKRRFromVarianceDataset(
    receivedCodeword_variance_another_region, authenticCodeword
)

KRR_variance_another_region_fluctuative_temperature = generatingKRRFromVarianceDataset(
    receivedCodeword_variance_another_region_fluctuative_temperature, authenticCodeword
)

# ==============================================================================================================================================
# Saving to Excel

savingToExcel(
    "/Users/fachrulreizamedina/Thesis Virtuoso/Implementasi/Script/External Noisy Source Dataset & KRR/Datasets_Ext_Scheme_2.xlsx",
    variance_rectorate_building_fluctuative_temperature,
    KRR_variance_rectorate_building_fluctuative_temperature
)

savingToExcel(
    "/Users/fachrulreizamedina/Thesis Virtuoso/Implementasi/Script/External Noisy Source Dataset & KRR/Datasets_Ext_Scheme_3.xlsx",
    variance_rectorate_building_fluctuative_temperature_slightly_moved,
    KRR_variance_rectorate_building_fluctuative_temperature_slightly_moved
)

savingToExcel(
    "/Users/fachrulreizamedina/Thesis Virtuoso/Implementasi/Script/External Noisy Source Dataset & KRR/Datasets_Ext_Scheme_4.xlsx",
    variance_l_building,
    KRR_variance_l_building
)

savingToExcel(
    "/Users/fachrulreizamedina/Thesis Virtuoso/Implementasi/Script/External Noisy Source Dataset & KRR/Datasets_Ext_Scheme_5.xlsx",
    variance_l_building_fluctuative_temperature,
    KRR_variance_l_building_fluctuative_temperature
)

savingToExcel(
    "/Users/fachrulreizamedina/Thesis Virtuoso/Implementasi/Script/External Noisy Source Dataset & KRR/Datasets_Ext_Scheme_6.xlsx",
    variance_another_city,
    KRR_variance_another_city
)

savingToExcel(
    "/Users/fachrulreizamedina/Thesis Virtuoso/Implementasi/Script/External Noisy Source Dataset & KRR/Datasets_Ext_Scheme_7.xlsx",
    variance_another_city_fluctuative_temperature,
    KRR_variance_another_city_fluctuative_temperature
)

savingToExcel(
    "/Users/fachrulreizamedina/Thesis Virtuoso/Implementasi/Script/External Noisy Source Dataset & KRR/Datasets_Ext_Scheme_8.xlsx",
    variance_another_region,
    KRR_variance_another_region
)

savingToExcel(
    "/Users/fachrulreizamedina/Thesis Virtuoso/Implementasi/Script/External Noisy Source Dataset & KRR/Datasets_Ext_Scheme_9.xlsx",
    variance_another_region_fluctuative_temperature,
    KRR_variance_another_region_fluctuative_temperature
)