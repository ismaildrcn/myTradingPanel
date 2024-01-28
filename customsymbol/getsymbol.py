from tradingview_ta import TA_Handler, Interval


class GetSymbol():
    def __init__(self):
        pass

    def get_symbol(self, symbol):
        sml = TA_Handler(
            symbol= symbol.upper(),
            screener="turkey",
            exchange="BIST",
            interval=Interval.INTERVAL_1_DAY,
            # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
        )
        analysis = sml.get_analysis()
        return analysis.time, analysis.indicators['open'], analysis.indicators['close']
