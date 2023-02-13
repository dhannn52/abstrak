class lauk:
    def __init__(ule, q):
        ule.quest = q
        ule.answer = []
        ule.isi = []
        ule.nilai = 0

    def lele(self):
        if self.quest == "M":
            print("_ _ _ _ _")
            self.isi = [int(x) for x in input("jawaban :").split()]
            print("jawaban yang benar:", self.answer)
            print("skor", self.nilai)

    def gurame(self):
        import random

        x = [1,2,3,4,5]
        v = ["a","b","c"]

        for i in range(len(x)):
            k = random.choice(x)
            self.answer.append(k)
            x.remove(k)

    def skor(self):
        if self.answer[0] == self.isi[0]:
            self.nilai += 20
        elif self.answer[1] == self.isi[1]:
            self.nilai += 20
        elif self.answer[2] == self.isi[2]:
            self.nilai += 20
        elif self.answer[3] == self.isi[3]:
            self.nilai += 20
        elif self.answer[4] == self.isi[4]:
            self.nilai += 20

def output():
    print("selamat datang")
    q =lauk(input("ketik [M] jika sudah siap bermain :"))
    q.lele()

if __name__ == "__main__":
    while True:
        output()
