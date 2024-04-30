import pandas as pd
import matplotlib.pyplot as plt

def plottingHammingDistancePair(xLabel, y1Label, y2Label, xValue, y1Value, y2Value):
    # Creating line plot
    data_dict = {xLabel: xValue,
                 y1Label: y1Value,
                 y2Label: y2Value
                 }

    df = pd.DataFrame(data_dict)

    ax = plt.gca()

    df.plot(kind='line',
            x=xLabel,
            y=y1Label,
            color='green',
            ax=ax)

    df.plot(kind='line',
            x=xLabel,
            y=y2Label,
            color='red',
            ax=ax)

    plt.title('Line Plots')
    plt.show()

