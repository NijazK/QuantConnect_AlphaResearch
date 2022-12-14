from AlgorithmImports import *

### <summary>
### Basic template algorithm simply initializes the date range and cash
### </summary>
### <meta name="tag" content="trading and orders" />
### <meta name="tag" content="limit orders" />
### <meta name="tag" content="placing orders" />
### <meta name="tag" content="updating orders" />
### <meta name="tag" content="regression test" />
class LimitFillRegressionAlgorithm(QCAlgorithm):

    def Initialize(self):
        '''Initialise the data and resolution required, as well as the cash and start-end dates for your algorithm. All algorithms must initialized.'''

        self.SetStartDate(2013,10,7)  #Set Start Date
        self.SetEndDate(2013,10,11)    #Set End Date
        self.SetCash(1000000)           #Set Strategy Cash
        # Find more symbols here: http://quantconnect.com/data
        self.AddEquity("UCO", Resolution.Second)

    def OnData(self, data):
        '''OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.'''
        if data.ContainsKey("UCO"):
            if self.IsRoundHour(self.Time):
                negative = 1 if self.Time < (self.StartDate + timedelta(days=2)) else -1
                self.LimitOrder("UCO", negative*10, data["UCO"].Price)

    def IsRoundHour(self, dateTime):
        '''Verify whether datetime is round hour'''
        return dateTime.minute == 0 and dateTime.second == 0

    def OnOrderEvent(self, orderEvent):
        self.Debug(str(orderEvent))
