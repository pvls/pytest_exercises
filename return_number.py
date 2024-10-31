def factorial(n):
    if n < 0:
        raise ValueError('received negative input')
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

def count_words_occurence_in_string(text, word):
    words = text.split()
    return words.count(word)


