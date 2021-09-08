def y():
    p = 'cow'
    p = input()

    def z():
        global p
        if p == 'rat':
            p = 'ball'
            return p

    return z()


print(y())
