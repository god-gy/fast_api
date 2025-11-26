from tortoise import fields


class BaseModel:
    id = fields.BigIntField(primary_key=True)
    created_at = fields.DatetimeField(auto_now_add=True)


#######################################################

# MySQL: primary key 를 정할때 주의해야 할 점
# MySQL version 8 이상 부터라면
# innodb가 default engine

# innodb의 특징 중 하나 -> clustering index
# primary key를 기준으로
# primary key 값이 비슷한 row들 끼리 disk 에서도 실제로 모여있음

# HDD
# 랜덤 IO가 느리고, 순차 IO가 빠름.

# 그냥 int가 아니라, 비즈니스 적 의미가 있고,
# 계속해서 증가 하는 어던 값으로 설정 한다면
# 굉장히 빠르게 읽을 수 있음.
