import torch


def n_gram(n: int, d: dict, s: str) -> dict:
    if n > len(s):
        return d
    s1 = s[-1:]
    s2 = s[: n - 1]
    d[s1 + s2] = d.get(s1 + s2, 0) + 1
    for k in range(n, len(s) + 1):
        s1 = s[k - n : k]
        d[s1] = d.get(s1, 0) + 1
    return d


def table(n: int, d: dict, vocab: list) -> dict:
    list = []
    for element in d:
        if not element[: n - 1] in list:
            list.append(element[: n - 1])
    list.sort()
    lookup = {}
    for element in list:
        tens = torch.zeros(len(vocab), dtype=torch.int)
        for k in range(len(vocab)):
            tens[k] = d.get(element + vocab[k], 0) + 1
        lookup[element] = tens / sum(tens)
    return lookup


def pred(n: int, d: dict, s: str, v: int) -> int:
    t = s[-n + 1 :]
    guess = torch.multinomial(d.get(t, torch.ones(v)), num_samples=1).item()
    return int(guess)
