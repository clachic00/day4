

class Quiz:

    def __init__(self,text):
        self.text = text
        self.yes = None
        self.no = None


q1 = Quiz("나는 미술관, 박물관 관람을 좋아한다")
q2 = Quiz("천혜의 자연관경을 가진 나라가 좋다")
q3 = Quiz("여행을 가면 늘 잘먹고 다녀야 한다")

q1.no=q2
q2.yes=q3

current = q1

while True:
    if current == None:
        print("THE END")
        break

    answer = input(current.text)

    if answer == 'y':
        current = current.yes

    elif answer == 'n':
        current = current.no
