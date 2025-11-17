# 제품 코드
def add(a: int, b: int) -> int:
    return a + b

# 테스트 코드
def test_add() -> None:
    # Given : 재료 준비
    a, b = 1, 1

    # When : 테스트 대상이 되는 함수 호출
    result = add(a, b)  # result의 타입은 int

    # Then :
    assert result == 2
    if not result == 2:
        raise AssertionError

