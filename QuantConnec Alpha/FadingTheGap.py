class ShortingPERatios(QCAlgorithm):

    def initialization(self):
        self.SetStartDate(2017, 11, 1)
        self.setEndDate(2018, 7, 1)
        self.SetCash(100000)
        self.AddEquity("TSLA", Resolution.Minute)

        self.schedule.On(self.DateRules.EveryDay(), self.TimeRules.BeforeMarketClose("TSLA", 0), self.ClosingBar)

        self.schedule.On(self.DateRules.EveryDay(), self.TimeRules.AfterMarketOpen("TSLA", 1), self.OpeningBar)

        self.schedule.On(self.DateRules.EveryDay(), self.TimeRules.AfterMarketOpen("TSLA", 45), self.ClosePositions)


        self.window = RollingWindow[TradeBar](2)

        self.volatility = standardDeviation("TSLA", 60)


    def OnData(self, data):
        if data["TSLA"] is not None:
            self.volatility.Update(self.Time, data["TSLA"].Close)
    
    def OpeningBar(self):
        if self.CurrentSlice["TSLA"] is not None:
            self.window.Add(self.CurrentSlice["TSLA"])

        if not self.window.IsReady or not self.volatility.IsReady:
            return

        delta = self.window[0].Open - self.window[1].Close

        deviations = delta / self.volatility.Current.Value

        if deviations < -3:
            self.SetHoldings("TSLA", 1)

        if delta < -10:
            self.SetHoldings("TSLA", 1)

    def ClosePositions(self):
        self.liquidate("TSLA")
        pass
    
