from login import fyers
class Event:
    "Base class for signal event"


class SignalEvent(Event):
    """
    Entry signal. Consumed by Portfolio to produce Order events.
    """

    def __init__(self, symbol: str, entry_ts,
                 strategy: str, venue, entry_price: float, entry_type: str, stop_price: float, 
                 trail: bool, note: str, dataset, ic=1):

        self.type = 'SIGNAL'
        self.entry_ts = entry_ts        # Entry bar timestamp.
        self.strategy = strategy        # Signal strategy name.
        self.symbol = symbol            # Ticker code for instrument.
        self.entry_price = entry_price  # Trade entry price.
        self.entry_type = entry_type.upper()  # Order type for entry.
        self.stop_price = stop_price    # Stop-loss order price.
        self.void_price = void_price    # Invalidation price.
        self.instrument_count = ic      # # of instruments in use.
        self.trail = trail              # True or False for trailing stop.
        self.op_data = dataset          # Dataset used to generate signal.
        self.note = note                # Signal notes.

    def __str__(self):
        return str("Signal Event: " + self.direction + " Symbol: " +
                   self.symbol + " Entry price: " + str(self.entry_price) +
                   " Entry timestamp: " + str(self.entry_ts) + " Timeframe: " +
                   self.timeframe + " Strategy: " + self.strategy +
                   " Venue: " + self.venue.get_name() + " Order type: " +
                   self.entry_type + " Note: " + self.note)

    def get_signal_dict(self):
        return {
            'strategy': self.strategy,
            'venue': self.venue.get_name(),
            'symbol': self.symbol,
            'entry_timestamp': self.entry_ts,
            'timeframe': self.timeframe,
            'direction': self.direction,
            'entry_price': self.entry_price,
            'entry_type': self.entry_type,
            'targets': self.targets,
            'stop_price': self.stop_price,
            'void_price': self.void_price,
            'instrument_count': self.instrument_count,
            'trail': self.trail,
            'note': self.note,
            'op_data': self.op_data}

