# 앞뒤 공백 제거
def removeSpace(str):
    return str.strip()

# 가격 원단위 콤마(,) 제거 to Integer
    # split 으로 나누기 [1, 001, 324, 500]
    # 1001324500
def wonToInt(won):
   price = won.split(',')  # 324,500 --> [324, 500]
   # 슬라이싱 이용  (처음부터 끝까지 조인) , int 로 캐스팅
   return int(''.join(price[:]))   # 324500


# 숫자를 원단위 표기로 변경
def intToWon(won):
    return format(won, ',') # format(매개변수2개)이용



if __name__ == '__main__':
    print(removeSpace('  나이키 코르테즈   '))
    print(wonToInt('155,123,456,454,543,233'))
    print(intToWon(15512345645454))




