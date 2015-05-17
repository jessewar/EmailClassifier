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

print 'ham ' + str(ham_count / total_count)
print 'spam ' + str(spam_count / total_count)
    
