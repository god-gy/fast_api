import random
from datetime import datetime

from sqids import sqids

squid = sqids.Sqids()


class Sqids:

    @classmethod
    def encode(cls, nums: list[int]) -> str:
        return squid.encode(nums)


if __name__ == "__main__":
    now = datetime.now()
    print(
        Sqids.encode(
            [now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond, random.randint(1, 9)]
        )
    )
