file = "test.txt"

cached = ""

def read7(file):
    return file.read(7)

def readN(file, n):
    global cached
    reads = []
    to_read = (n - len(cached)) / 7 + 1
    for i in range(to_read):
        reads.append(read7(file))
    string = cached + "".join(reads)
    cached = string[n:]
    return string[:n]

if __name__ == "__main__":
    with open(file) as f:
        assert readN(f, 3) == "Hel"
        assert readN(f, 5) == "lo wo"
        assert readN(f, 10) == "rld\n"