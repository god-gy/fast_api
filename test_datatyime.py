# 이제 실전 문제 하나를 풀어보겠습니다. (스스로 풀려고 노력해 봅시다)
#
# 택배가 언제 도착할지, 예상 배송일을 계산하는 단위 테스트를 하나 예시로 들겠습니다.
#
# - 택배는 2영업일 이후에 도착합니다. 월요일부터 토요일까지가 영업일입니다.
# - 단순화를 위해 “도서산간지역”은 고려하지 않습니다.
# - 단순화를 위해 설날, 추석 등의 공휴일은 고려하지 않습니다.

from datetime import datetime, timedelta

# literal을 쓰지 않고 상수를 쓰는 이유
# 2라는 숫자가 "이게 배송일이야"라고 배경을 모르는 사람들(동료, 미래의 나)에게 알려줌
# magic number를 쓰지 말자 : 특정한 값인데 설명이 없거나 여러번 등장하는데 상수로 바꿀 수 있는 경우
DELIVERY_DAYS = 2

def _is_holiday(day: datetime) -> bool:
    return day.weekday() > 5

def get_eta(purchase_date: datetime) -> datetime:
    current_date = purchase_date
    remaining_days = DELIVERY_DAYS

    while remaining_days > 0:
        current_date += timedelta(days=1)
        if not _is_holiday(current_date):
            remaining_days -= 1
    return current_date

def test_get_eta_2023_12_01() -> None:
    result = get_eta(datetime(2023, 12, 1))
    assert result == datetime(2023, 12, 4)

def test_get_eta_2024_12_31() -> None:
    """공휴일 정보가 없어서 1월 1일도 평일로 취급된다."""
    result = get_eta(datetime(2024, 12, 31))
    assert result == datetime(2025, 1, 2)

def test_get_eta_2024_02_28() -> None:
    result = get_eta(datetime(2024, 2, 28))
    assert result == datetime(2024, 3, 1)

def test_get_eta_2023_02_28() -> None:
    result = get_eta(datetime(2023, 2, 28))
    assert result == datetime(2023, 3, 2)
