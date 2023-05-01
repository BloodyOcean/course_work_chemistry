from datetime import datetime, timedelta
import random
from generators import Generator


class DatetimeGenerator(Generator):

    def __init__(self, start: datetime, end: datetime):
        self.start = start
        self.end = end

    def next(self):
        """
        Returns a random datetime string between two given datetimes in the format of
        YYYY-MM-DD HH:MM:SS, suitable for use in SQL Server.

        Args:
        start (datetime): The start of the datetime range
        end (datetime): The end of the datetime range
        
        Returns:
        str: A randomly generated datetime string within the given range.
        """
        delta = self.end - self.start
        seconds = delta.total_seconds()
        random_seconds = random.randrange(seconds)
        random_delta = timedelta(seconds=random_seconds)
        random_datetime = self.start + random_delta
        return random_datetime.strftime('\'%Y-%m-%d %H:%M:%S\'')
