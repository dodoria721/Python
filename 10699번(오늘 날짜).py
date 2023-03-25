import datetime
time = datetime.datetime.today() + datetime.timedelta(hours=9)
print(time.strftime("%Y-%m-%d"))


"""
datetime 모듈에 있는 timedelta 클래스는 특정 날짜로부터 상대적 날짜를 계산할 수 있다.
timedelta() 괄호 안에 day(일), hours(시), minutes(분), seconds(초), microseconds(마이크로 초), miliseconds(밀리 초), weeks(주)를 쓸 수 있다. 
양수는 이후, 음수는 이전을 뜻한다.

time2 = datetime.datetime.today()

'현재 시간부터 5일 뒤'
time2 + timedelta(days=5)
'현재 시간부터 5일 전'
time2 + timedelta(days=-5) == time2 - timedelta(days=5)
'현재 시간부터 3일 전의 3시간 후의 10분 전'
tiem2 + timedelta(days=-3, hours=2, minutes = -10)

※ 덧셈과 뺄셈에 유의
"""
