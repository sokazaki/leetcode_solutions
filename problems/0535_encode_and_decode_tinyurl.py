import string

class Codec:

    def __init__(self):
        self.url2code = {}
        self.code2url = {}
        self.base62 = string.ascii_letters + '0123456789'

    def encode(self, longUrl):
        while longUrl not in self.url2code:
            code = ''.join(random.choice(self.base62) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl):
        return self.code2url[shortUrl[-6:]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
