def common_letters(a,b):
    s1 = set(a)
    s2 = set(b)
    common = s1 & s2
    print("Common letters: " + str(common))
common_letters("house", "computers")