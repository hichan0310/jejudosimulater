# a,b=map(int, input().split())
# while a!=b:
#     while a%2==0:
#         print("B+=B")
#         a>>=1
#     while b%2==0:
#         print("A+=A")
#         b>>=1
#     if a>b:
#         b+=a
#         print("B+=A")
#     else:
#         a+=b
#         print("A+=B")
# 백준 코드인데 옮겨두기 귀찮아서 그냥 여기다 둠




import cv2
import keyboard

camera = cv2.VideoCapture(0)
while not keyboard.is_pressed(' '):
    ret, frame = camera.read()
    cv2.imshow('camera', frame)
    cv2.waitKey(1)
for i in range(10):
    ret, frame = camera.read()
    cv2.imshow('camera', frame)
    cv2.imwrite(f"./images/{i}.jpg", frame)
    cv2.waitKey(1)


# todo
#   haar cascade 써서 이미지에서 눈 골라내기 : https://velog.io/@leeyk_2121_ar/%EC%9D%B4%EB%AF%B8%EC%A7%80-%ED%8C%8C%EC%9D%BC%EC%97%90%EC%84%9C-%EC%96%BC%EA%B5%B4-%EC%98%81%EC%97%AD-%EC%B6%94%EC%B6%9C-%EC%8B%A4%EC%8A%B52
#   눈 감았는지 판단하는 모델 만들기 : 아마 cnn 쓰겠지
#   눈 매칭시키고 합성하기 : md 파일 참고
