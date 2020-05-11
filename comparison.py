with open("followers.txt") as f1, open("followings.txt") as f2:
    s1 = {line.strip() for line in f1}
    s2 = {line.strip() for line in f2}

    diff = s2.difference(s1)

for i in diff:
    print(i)

