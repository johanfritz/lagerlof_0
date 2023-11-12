class parse:
    def __init__(self, filename: str):
        self.file = []
        letters = []
        with open(filename, "r") as file:
            for row in file:
                self.file.append(row)
                for letter in row:
                    if not letter in letters:
                        letters.append(letter)
        self.stoi1 = {}
        self.itos1 = {}
        letters.sort()
        for k in range(len(letters)):
            self.stoi1[letters[k]] = k
            self.itos1[k] = letters[k]
        self.letters = letters

    def __len__(self):
        return len(self.file)

    def __getitem__(self, index: int):
        return self.file[index]

    def stoi(self, s: str):
        return self.stoi1[s]

    def itos(self, ind: int):
        if ind > len(self):
            raise KeyError("itos: index greater than length.")
        return self.itos1[ind]

    def vocabSize(self) -> int:
        return len(self.stoi1)

    def vocab(self):
        return self.letters
