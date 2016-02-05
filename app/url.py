class Url:

    charMap = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
     'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5',
     '6', '7', '8', '9']

    def __init__(self, url):
        self.url = url

    def getUrl(self):
        return "URL: "+self.url

    def toPetitUrl(self, id):
        shorturl = ""
        while(id > 0):
            shorturl = shorturl + Url.charMap[id % 62]
            id = id / 62

        shorturl = shorturl[::-1]
        return shorturl

    def toId(self, url):
        id = 0
        charMap = Url.charMap
        a = charMap.index('a')
        z = charMap.index('z')
        A = charMap.index('A')
        Z = charMap.index('Z')

        zero = charMap.index('0')
        nine = charMap.index('9')

        for c in url:
            currPos = charMap.index(c)
            if(a <= currPos and currPos <= z):
                id = id * 62 + currPos - a
            elif(A <= currPos and currPos <= Z):
                id = id * 62 + currPos - A + 26
            elif(zero <= currPos and currPos <= nine):
                id = id * 62 + currPos - zero + 52

        return str(id)
