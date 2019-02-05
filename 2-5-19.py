import string
import random

CHARACTERS = string.letters + string.digits
NUM_CHARACTERS = len(CHARACTERS)

class URL_Shortener:
    def __init__(self):
        self.short_to_long = {}
        self.long_to_short = {}

    def generate_short(self):
        output = []
        for _ in range(6):
            index = random.randint(0, NUM_CHARACTERS - 1)
            output.append(CHARACTERS[index])
        return "".join(output)

    def shorten(self, url):
        if url in self.long_to_short:
            return self.long_to_short[url]
        
        shortened = self.generate_short()
        while shortened in self.short_to_long:
            shortened = self.generate_short()

        self.short_to_long[shortened] = url
        self.long_to_short[url] = shortened

        return shortened

    def restore(self, short):
        if short in self.short_to_long:
            return self.short_to_long[short]
        raise ValueError("Invalid shortened URL")

urls = URL_Shortener()
url = "google.com"
short = urls.shorten(url)
assert url == urls.restore(short)
assert short == urls.shorten(url)