# 게임 유닛 만들기
#Unit 부모 클래스 선언
class Unit:
    def __init__(self, name, energy, is_fly):
        self.name = name
        self.energy = energy
        self.is_fly = is_fly
        self.is_alive = True

    def get_tribe(self):
        print(self.name + 'is a basic tribe!!')

    def get_energy(self):
        if self.energy >0:
            print(self.name + '의 현재 에너지는', self.energy, '입니다')
        else:
            self.is_alive = False
            print(self.name + '유닛은 전사했습니다.')

# 테란 종족 클래스
class Terran(Unit):
    def get_tribe(self):
        print(self.name + 'is a Terran!!')

    def be_attactted(self):
        self.energy -= 3

# 프로토스족 클래스
class Protoss(Unit):
    def get_tribe(self):
        print(self.name + 'is a Protoss!!')

    def be_attactted(self):
        self.energy -= 2

# 저그 종족 클래스
class Zerg(Unit):
    def get_tribe(self):
        print(self.name + 'is a Zerg!!')
    def be_attactted(self):
        self.energy -= 4


import time
# from tqdm import tqdm_notebook

marine = Terran('골리앗', 15, False)
corsair = Protoss('커세어', 20, True)
hydra = Zerg('히드라', 10, False)

for x in range(5):
    if x == 0:
        print('게임 시작, 유닛의 에너지는 다음과 같습니다!!' + '-' * 50)
        marine.get_energy()
        corsair.get_energy()
        hydra.get_energy()
        time.sleep(2)
        continue

    marine.be_attactted()
    corsair.be_attactted()
    hydra.be_attactted()

    print('유닛간에 %d차 공방전이 이루어졌습니다.'%(x) + '-' * 50)
    time.sleep(1)
    marine.get_energy()
    time.sleep(1)
    corsair.get_energy()
    time.sleep(1)
    hydra.get_energy()
    time.sleep(1)

    if(marine.is_alive & corsair.is_alive  & hydra.is_alive):
        time.sleep(1)

    else:
        break

print('=' * 50, 'GG 게임이 종료되었습니다')

