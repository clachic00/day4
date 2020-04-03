class Quiz:

    def __init__(self,text):
        self.text = text
        self.yes = None
        self.no = None

class QuizManager:

    def __init__(self):
        q1 = Quiz("다수의 선택은 대부분 옳다")
        q2 = Quiz("귀가 얇아 선택이 가장 어렵다")
        q3 = Quiz("물건을 살 때 실물을 직접 살펴봐야 한다")
        q4 = Quiz("옷이든 가구든 세트로 맞추는 것을 좋아한다")
        q5 = Quiz("비싼 건 그만한 가치가 있다고 생각한다")
        q6 = Quiz("유명 브랜드라도 모든 제품이 다 좋진 않다")
        q7 = Quiz("쇼핑은 30분만에 끝낸다")
        q8 = Quiz("제품을 하나씩 택배로 받는 재미가 쏠쏠하다")
        q9 = Quiz("하나를 사더라도 모든 제품을 비교해 봐야 직성이 풀린다")

        q1.yes = q3
        q1.no = q2
        q2.yes = q4
        q2.no = q3
        q3.yes = q6
        q3.no = q5
        q4.yes = q7
        q4.no = q5
        q5.yes = q7
        q5.no = q8
        q6.yes = q9
        q6.no = q8
        q7.no = q8
        q9.no = q8

        self.start_quiz = q1

    def getFirstQuiz(self):
        return self.start_quiz


class QuizUI:

    def __init__(self):
        manager = QuizManager()
        self.playShow(manager.getFirstQuiz())

    def playShow(self, quiz):

        if quiz == None:
            print("THE END")
            return

        answer = input(quiz.text)

        if answer == 'y':
            self.playShow(quiz.yes)
        elif answer == 'n':
            self.playShow(quiz.no)

ui = QuizUI()