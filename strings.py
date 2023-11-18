def sentence_details(sentence):
    prompt = {'islower': 0, 'isupper': 0, 'isnumeric': 0, 'isspace': 0}
    for letter in sentence:
        for promptDetail in prompt:
            if getattr(letter, promptDetail)():
                prompt[promptDetail] += 1
    return prompt


print(sentence_details('aldha35Lgdslaksdh'))
