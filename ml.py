from collections import Counter

training_file = open('train', 'r')
spam_word_counts = Counter()
vocabulary = set()
for line in training_file:
    tokens = line.split(' ')
    classification = tokens[1]
    for i in range(2, len(tokens), 2):
        word = tokens[i]
        count = int(tokens[i+1])
        vocabulary.add(word)
        if classification == 'spam':
            spam_word_counts[word] += count

m = len(vocabulary)
n = sum(spam_word_counts.values())
p = 1.0 / m
word_probabilities = {}
for word in spam_word_counts:
    n_c = spam_word_counts[word]
    word_probabilities[word] = (n_c + m * p) / (n + m)
sorted_words = sorted(word_probabilities.items(), key=lambda x: x[1], reverse=True)
for word, probability in sorted_words[:5]:
    print 'word: ' + word + ', ' + 'probability: ' + str(probability)
