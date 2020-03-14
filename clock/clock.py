class Clock:
    def __init__(self, hour, minute):
        self.minute = minute % 60
        self.hour = ((minute // 60) + hour) % 24

    def __repr__(self):
        return f'{self.hour:02}:{self.minute:02}'

    def __eq__(self, other):
        if isinstance(other, Clock):
            return self.minute == other.minute and self.hour == other.hour
        return False

    def __add__(self, minutes):
        return Clock(
            ((self.minute + minutes) // 60 + self.hour) % 24,
            (self.minute + minutes) % 60)

    def __sub__(self, minutes):
        return Clock(
            ((self.minute - minutes) // 60 + self.hour) % 24,
            (self.minute - minutes) % 60)
