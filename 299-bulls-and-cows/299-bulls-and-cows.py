class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        x = 0
        y = 0
        for a,b in zip(secret,guess):
            if a== b:
                x += 1
                
        c = defaultdict(int)
        for i in range(len(secret)):
            if secret[i] != guess[i]:
                c[secret[i]] += 1
        # print(c)
        for i in range(len(guess)):
            if c.get(guess[i],0) > 0 and guess[i] != secret[i]:
                y += 1
                c[guess[i]] -=1
        return str(x) + "A" + str(y) + "B"
                