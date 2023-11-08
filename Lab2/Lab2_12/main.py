def group_by_rhyme(words):
    rhyme_groups = []

    for word in words:
        rhyme = word[-2:]
        added = False

        for group in rhyme_groups:
            if group[0][-2:] == rhyme:
                group.append(word)
                added = True
                break

        if not added:
            rhyme_groups.append([word])

    return rhyme_groups


# Test case
words = ['ana', 'banana', 'carte', 'arme', 'parte']
result = group_by_rhyme(words)
print("Words grouped by rhyme:", result)
