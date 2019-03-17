class StrPattern:
    def __init__(self,S, T):
        self.s = S
        self.t = T

    def BF_Index(self):
        i = 0
        j = 0
        print(len(self.s))
        print(len(self.t))
        while i < len(self.s) or j < len(self.t):
            if self.s[i] == self.t[j]:
                i = i + 1
                j = j + 1
            else:
                i = i - j + 1
                j = 0
        if j >= len(self.t):
            print(i - j + 1)
        else:
            print(-1)

    def KMS_Index(self):






s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaal"
t = "aaal"
S = StrPattern(s,t)
S.StringPattern()