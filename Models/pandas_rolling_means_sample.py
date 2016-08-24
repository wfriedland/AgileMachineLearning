import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import pandas as pd


def demo_pandas_rolling_mean():

    #
    #   Data - closing priceses of SPY
    #
    prices = pd.Series([211.35,211.68,212.37,212.08,210.07,208.45,208.04,207.75,208.37,206.52,207.85,208.44,208.1,210.81,
                        203.13,203.20,206.66,209.48,209.92,208.41,209.53,212.65,213.4,214.95,214.92,216.12,215.83,
                        216.41,218.18,218.05,218.18,217.23,218.94,217.99,219.09,217.96,218.37,218.9,218.75])

    #
    #  Calculate a 20 period simple moving average.
    #
    count = 0
    try:
        price_total = 0
        pricelist = []
        for p in prices:
            price_total = price_total + prices[count]
            count = count + 1
            if (count >= 20):
                tmean = price_total / 20
                pricelist.append(tmean)
                price_total = price_total - prices[count-20]
    except Exception as e:
        print ('trouble in paradice')
        print e

    sma0 = pd.Series(pricelist)
    stdev0 = sma0.std()

    #
    #  Calculate a 20 period simple moving average using the pandas moving window
    #
    try:
        sma1 = pd.Series(prices).rolling(window=20).mean()
    except Exception as e:
        print ('more trouble in paradice')
        print e

    sma1 = sma1.dropna()
    stdev1 = sma1.std()

    #
    #  Compare the standard deviation computed for the two simple moving averages
    #
    if (abs(stdev1 - stdev0) < 1e-10):
        print 'standard deviations are equal'
    else:
        print 'standard deviations not equal'
        print stdev1
        print stdev0

    #
    # plot the two simple moving averages to demonstrate that they are the same
    #
    try:
        fig = plt.figure(44, figsize=(12, 6))
        sp = plt.subplot(221)
        plt.autoscale(enable=True, axis='both',tight=False)
        plt.grid(True)
        plt.title("Moving Average ")
        sp.plot (sma0)

        sp = plt.subplot(222)
        plt.autoscale(enable=True, axis='both',tight=False)
        plt.grid(True)
        plt.title("Moving Average with rolling.means()")
        sp.plot (sma1)
        plt.savefig("./sma.png", dpi=None, facecolor='w', edgecolor='w',
                    orientation='portrait', papertype=None, format=None,
                    transparent=False, bbox_inches=None, pad_inches=0.1,
                    frameon=None)
    except Exception as e:
        print e

    return 100      # force sucessful return