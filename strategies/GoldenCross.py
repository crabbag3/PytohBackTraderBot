import math
import backtrader as backtrader

class GoldenCross(bt.Strategy):
	params = (('fast', 50), ('slow', 200), ('order_percentage', 0.95), ('ticker', 'SPY'))

	def __init__(self):
		self.fast_moving_average = bt.indicators.SMA(
			self.data.close, period = self.params.fast, plotname='50 day moving average'
			)

		self.slow_moving_average = bt.indicators.SMA(
			self.data.close, period = self.params.slow, plotname='200 day moving average'
			)

		self.crossover = bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)

		def next(self):
			pass