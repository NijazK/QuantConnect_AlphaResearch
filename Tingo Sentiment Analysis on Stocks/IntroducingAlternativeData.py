from AlgorithmImports import *
class TiingoNewsSentimentAlgorithm(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2016, 11, 1)
        self.SetEndDate(2017, 3, 1)  
        
        #2. Add AAPL and NKE symbols to a Manual Universe 
        symbols = [Symbol.Create("AAPL", SecurityType.Equity, Market.USA), 
            Symbol.Create("NKE", SecurityType.Equity, Market.USA)]
        self.SetUniverseSelection(ManualUniverseSelectionModel(symbols))
        
        # 3. Add an instance of the NewsSentimentAlphaModel
        self.SetAlpha(NewsSentimentAlphaModel())
        self.SetPortfolioConstruction(EqualWeightingPortfolioConstructionModel()) 
        self.SetExecution(ImmediateExecutionModel()) 
        self.SetRiskManagement(NullRiskManagementModel())
        
# 4. Create a NewsSentimentAlphaModel class with Update() and OnSecuritiesChanged() methods
class NewsSentimentAlphaModel(AlphaModel):
    def __init__(self): 
        pass
    def Update(self, algorithm, data):
        insights = []
        return insights
    def OnSecuritiesChanged(self, algorithm, changes):
        pass
