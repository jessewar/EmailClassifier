from collections import Counter

# Get prior probabilities of spam and ham
ham_count = 0.0
spam_count = 0.0
total_count = 0.0
training_file = open('train', 'r')
for line in training_file:
    tokens = line.split(' ')
    classification = tokens[1]
    total_count += 1
    if classification == 'ham':
        ham_count += 1
    else:
        spam_count += 1

ham_prior = ham_count / total_count
spam_prior = spam_count / total_count

# Get counts of words for spam and ham emails
training_file = open('train', 'r')
spam_word_counts = Counter()
ham_word_counts = Counter()
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
        else:
            ham_word_counts[word] += count

# Compute m-estimates for each word
def get_word_likelihoods(word_counts):
    m = len(vocabulary)
    n = sum(word_counts.values())
    p = 1.0 / m
    word_probabilities = {}
    for word in word_counts:
        n_c = word_counts[word]
        word_probabilities[word] = (n_c + m * p) / (n + m)
    return word_probabilities

# Print the top five words with the highest likelihoods of occurring
def top_five_words(word_likelihoods):
    sorted_words = sorted(word_likelihoods.items(), key=lambda x: x[1], reverse=True)
    for word, probability in sorted_words[:5]:
        print 'word: ' + word + ', ' + 'probability: ' + str(probability)


spam_likelihoods = get_word_likelihoods(spam_word_counts)
ham_likelihoods = get_word_likelihoods(ham_word_counts)
print("spam------------")
top_five_words(spam_likelihoods)
print("ham-------------")
top_five_words(ham_likelihoods)

