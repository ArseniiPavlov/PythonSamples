import numpy as np
import scipy.spatial
import re
np.set_printoptions(edgeitems=150)

f = open('sentences.txt')
sent_lines = f.readlines()
for i in xrange(len(sent_lines)):
    sent_lines[i] = sent_lines[i].lower()
    sent_lines[i] = re.split('[^a-z]', sent_lines[i])
for i in xrange(len(sent_lines)):
    while True:
        try:
            sent_lines[i].remove('')
        except ValueError:
            break
word_dict = {}
ind = 0
for i in xrange(len(sent_lines)):
    for j in xrange(len(sent_lines[i])):
        if sent_lines[i][j] not in word_dict:
            word_dict[sent_lines[i][j]] = ind
            ind += 1
word_matrix = np.zeros((22, 254), dtype=float)
for i in xrange(len(sent_lines)):
    for j in xrange(len(sent_lines[i])):
        word_matrix[i, word_dict[sent_lines[i][j]]] += 1

sent_dist = {}
for i in xrange(len(word_matrix)):
    sent_dist[scipy.spatial.distance.cosine(word_matrix[0], word_matrix[i])] = i
f1 = open('submission-1.txt', 'w')
f1.write(str(sent_dist[sorted(sent_dist)[1]]) + ' ' + str(sent_dist[sorted(sent_dist)[2]]))
f1.close()
f.close()
print(sent_dist[sorted(sent_dist)[3]], sent_dist[sorted(sent_dist)[4]])

