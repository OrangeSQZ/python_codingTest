def solution(babbling):
    c = 0
    for b in babbling:
        # print('before:',b)
        for w in [ "aya", "ye", "woo", "ma" ]:
            if w * 2 not in b:
                b = b.replace(w, ' ')
        # print('after:',b)
        if len(b.strip()) == 0:
            c += 1
    return c