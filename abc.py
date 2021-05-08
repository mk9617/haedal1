class player:

    def __init__(self,name,age,team,num):
        self.name = name
        self.age = age
        self.team = team
        self.num = num


    def info(self):
        print(f'이름: {self.name}')
        print(f'나이: {self.age}')
        print(f'팀: {self.team}')
        print(f'등번호:{self.num}')
        print()


player1 = player('김상수',32,'삼성 라이온즈',7)
player2 = player('이대호',40,'롯데 자이언츠',10)
player3 = player('소형준',21,'KT WIZ',30)

player1.info()
player2.info()
player3.info()

