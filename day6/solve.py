with open('input.txt') as f:
    groups = f.read().split('\n\n')
    count1 = 0
    count2 = 0
    for group in groups:
        answers = group.splitlines()
        count1 += len(set(char for answer in answers for char in answer))
        count2 += len(set.intersection(*[set(answer) for answer in answers]))
    print(count1)
    print(count2)
