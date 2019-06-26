class Device():
    def __init__(self):
        self.name = ''
        self.multiplier = 1.5
        self.SW = 0
        self.TL = self.SW+2 #TS Lower then TL (can't be equal)
        self.FD = 0
        self.TS = []
        self.MR = 0
        self.CS = 0
        self.threshold = 0
        self.time = 0
        self.temp = 0

    def insert_name(self, string):
        if string and isinstance(string, str):
            self.name = string
            return True
        return False

    def insert_multiplier(self, val):
        if val in ["1", "2"]:
            self.multiplier = int(val)
        elif val == '':
            self.multiplier = 1.5
        else:
            return False
        return True

    def insert_SW(self, val):
        try:
            if int(val) in range(100):
                self.SW = int(val)
                self.TL = self.SW+2
                self.TS = [TS for TS in self.TS if TS < self.TL]
                return True
            return False
        except ValueError:
            return False

    def insert_FD(self, val):
        try:
            if int(val) in range(1,8):
                self.FD = int(val)
                return True
            return False
        except ValueError:
            return False

    def insert_TS(self, val):
        try:
            if int(val) < self.TL:
                self.TS.append(int(val))
                return True
            return False
        except ValueError:
            return False

    def insert_MR(self, val):
        try:
            if int(val) in range(1, 6):
                self.MR = int(val)
                return True
            return False
        except ValueError:
            return False

    def calculating(self):
        self.CS = sum(map(int, self.TS)) + self.FD
        self.threshold = int(self.FD*self.CS-self.SW)
        if self.threshold > 90:
            for tmp in range(2, 5):
                if self.threshold // tmp < 90:
                    print("Próg wyniósł powyżej 90, został zredukowany "+str(tmp)+"-krotnie")
                    self.threshold //= tmp
                    self.temp = tmp
                    break
            else:
                return False
        time = (self.threshold + max(self.TS) ) * self.multiplier / (self.SW + self.MR**2)
        self.time = int(time) if int(time) >= time else (int(time) + 1)
        if self.temp:
            self.time *= self.temp
            self.temp = 0

    def print_calculation(self):
        print("Wynalazek =", self.name)
        print("FD =", self.FD)
        print("TL =", self.TL-1)
        print(" - (funkcjonalność)\n".join(str(TS) for TS in self.TS))
        print("CS =", self.CS)
        print("MR =", self.MR)
        print("Próg =", self.threshold)
        print("Czas =", self.time)
