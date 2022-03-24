from googletrans import Translator
from time import sleep
from os import system 
from tqdm import tqdm

input()
for i in "번역기 준비중....":
    sleep(0.1)
    print(i, end="", flush=True)
system("cls")

for i in tqdm(range(100)):
    sleep(0.05)

print("로딩완료!!")
input("시작하려면 Enter 를 눌러주세요")
system("cls")


na_code = ['ko','ja','zh-cn','en']

while True:
    print("="*30)
    print("번역해ZOOM")
    print("="*30)
    text = input("번역할 문장을 입력하세요 : ")
    print("="*30)
    print("1. 한국어")
    print("2. 일본어")
    print("3. 중국어")
    print("4. 영어")
    print("="*30)
    sr = int(input("번역하고자 하는 텍스트는 어떤 나라의 언어인가요?"))
    de = int(input("어떤 나라 언어로 번역할까요?"))

    translator = Translator()
    trans1 = translator.translate(text, src=na_code[sr-1], dest=na_code[de-1])
    print(f"{text} > {trans1.text}")
    user = input("\n메인페이지로 돌아가기(Enter) 종료(quit)")
    if user == "quit":
        print("번역기 종료!! ㅠㅠ")
        break
    system("cls")








