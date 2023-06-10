def parchment(string, divisor=' '):
    string = set(string)
    global snuffbox
    sn2 = ["" for i in range(len(snuffbox))]
    c = 0
    for i in snuffbox:
        for j in string:
            i = i.replace(j, '')
        sn2[c] = divisor.join(set(i))
        c+=1
    snuffbox = sn2
    snuffbox = tuple(snuffbox)

snuffbox = ('black', 'powder', 'piece', 'parchment')
parchment('mutabor', divisor=';')
print(snuffbox)
