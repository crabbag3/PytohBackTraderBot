import backtrader as bt
import datetime
import pandas as pd
from strategies import GoldenCross
# from strategies.GoldenCross import GoldenCross

# Init cerebro
cerebro = bt.Cerebro()

cerebro.broker.setcash(1000000)

# Create a Data Feed
spy_prices = pd.read_csv('data/spy.csv', index_col='Date', parse_dates=True)

feed = bt.feeds.PandasData(dataname=spy_prices)
# Add Data
cerebro.adddata(feed)

# Run Strategy
cerebro.addstrategy(GoldenCross)
cerebro.run()
cerebro.plot()


# # Add Sizer
# cerebro.addsizer(backtrader.sizers.FixedSize, stake = 1000)
# print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())



# print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

# # cerebro.plot()