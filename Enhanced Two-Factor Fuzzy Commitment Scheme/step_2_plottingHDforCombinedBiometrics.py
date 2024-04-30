from plotGraph import *
from step_1_definingExternalNoisySourceSchemes import *

# ======================================================================================================================
# Plotting Hamming Distance for Genuine New Biometric & Attacker New Biometric

# Plot 1 : Genuine (rectorate_building) and Genuine (rectorate_building_fluctuative_temperature)
plottingHammingDistancePair(
    'HD',
    'Genuine Biometric',
    'Genuine Biometric with Fluctuative Temperature',
    xLabelForGraph(0,128),
    calculateHammingDistance_intraBiometric(combinedBiometric_rectorate_building),
    calculateHammingDistance_interBiometric_Genuine(combinedBiometric_rectorate_building, combinedBiometric_rectorate_building_fluctuative_temperature)
)

printParameters_Genuine(
    combinedBiometric_rectorate_building,
    combinedBiometric_rectorate_building_fluctuative_temperature,
    "Genuine Biometric x Genuine Biometric with Fluctuative Temperature"
)

# Plot 2 : Genuine (rectorate_building) and Genuine (rectorate_building_fluctuative_temperature_slightly_moved)
plottingHammingDistancePair(
    'HD',
    'Genuine Biometric',
    'Genuine Biometric with Fluctuative Temperature & Slightly Moved',
    xLabelForGraph(0,128),
    calculateHammingDistance_intraBiometric(combinedBiometric_rectorate_building),
    calculateHammingDistance_interBiometric_Genuine(combinedBiometric_rectorate_building, combinedBiometric_rectorate_building_fluctuative_temperature_slightly_moved)
)

printParameters_Genuine(
    combinedBiometric_rectorate_building,
    combinedBiometric_rectorate_building_fluctuative_temperature_slightly_moved,
    "Genuine Biometric x Genuine Biometric with Fluctuative Temperature & Slightly Moved"
)

# Plot 3 : Genuine (rectorate_building) and Attacker (l_building)
plottingHammingDistancePair(
    'HD',
    'Genuine Biometric',
    'Attacker Biometric (Different Building)',
    xLabelForGraph(0,128),
    calculateHammingDistance_intraBiometric(combinedBiometric_rectorate_building),
    calculateHammingDistance_interBiometric(combinedBiometric_rectorate_building, combinedBiometric_l_building)
)

printParameters(
    combinedBiometric_rectorate_building,
    combinedBiometric_l_building,
    "Genuine Biometric x Attacker Biometric (Different Building)"
)

# Plot 4 : Genuine (rectorate_building) and Attacker (l_building_fluctuative_temperature)
plottingHammingDistancePair(
    'HD',
    'Genuine Biometric',
    'Attacker Biometric (Different Building with Fluctuative Temperature)',
    xLabelForGraph(0,128),
    calculateHammingDistance_intraBiometric(combinedBiometric_rectorate_building),
    calculateHammingDistance_interBiometric(combinedBiometric_rectorate_building, combinedBiometric_l_building_fluctuative_temperature)
)

printParameters(
    combinedBiometric_rectorate_building,
    combinedBiometric_l_building_fluctuative_temperature,
    "Genuine Biometric x Attacker Biometric (Different Building with Fluctuative Temperature)"
)

# Plot 5 : Genuine (rectorate_building) and Attacker (another_city)
plottingHammingDistancePair(
    'HD',
    'Genuine Biometric',
    'Attacker Biometric (Different City)',
    xLabelForGraph(0,128),
    calculateHammingDistance_intraBiometric(combinedBiometric_rectorate_building),
    calculateHammingDistance_interBiometric(combinedBiometric_rectorate_building, combinedBiometric_another_city)
)

printParameters(
    combinedBiometric_rectorate_building,
    combinedBiometric_another_city,
    "Genuine Biometric x Attacker Biometric (Different City)"
)

# Plot 6 : Genuine (rectorate_building) and Attacker (another_city_fluctuative_temperature)
plottingHammingDistancePair(
    'HD',
    'Genuine Biometric',
    'Attacker Biometric (Different City with Fluctuative Temperature)',
    xLabelForGraph(0,128),
    calculateHammingDistance_intraBiometric(combinedBiometric_rectorate_building),
    calculateHammingDistance_interBiometric(combinedBiometric_rectorate_building, combinedBiometric_another_city_fluctuative_temperature)
)

printParameters(
    combinedBiometric_rectorate_building,
    combinedBiometric_another_city_fluctuative_temperature,
    "Genuine Biometric x Attacker Biometric (Different City with Fluctuative Temperature)"
)

# Plot 7 : Genuine (rectorate_building) and Attacker (another_region)
plottingHammingDistancePair(
    'HD',
    'Genuine Biometric',
    'Attacker Biometric (Different Region)',
    xLabelForGraph(0,128),
    calculateHammingDistance_intraBiometric(combinedBiometric_rectorate_building),
    calculateHammingDistance_interBiometric(combinedBiometric_rectorate_building, combinedBiometric_another_region)
)

printParameters(
    combinedBiometric_rectorate_building,
    combinedBiometric_another_region,
    "Genuine Biometric x Attacker Biometric (Different Region)"
)

# Plot 8 : Genuine (rectorate_building) and Attacker (another_region_fluctuative_temperature)
plottingHammingDistancePair(
    'HD',
    'Genuine Biometric',
    'Attacker Biometric (Different Region with Fluctuative Temperature)',
    xLabelForGraph(0,128),
    calculateHammingDistance_intraBiometric(combinedBiometric_rectorate_building),
    calculateHammingDistance_interBiometric(combinedBiometric_rectorate_building, combinedBiometric_another_region_fluctuative_temperature)
)

printParameters(
    combinedBiometric_rectorate_building,
    combinedBiometric_another_region_fluctuative_temperature,
    "Genuine Biometric x Attacker Biometric (Different Region with Fluctuative Temperature)"
)