# Sometime, we only have the glove format embedding. However, some library need the w2v format
# embeddding format file. Actually, these is very little difference between these two types.
# The only difference is the first line in w2v format which indicates the vocab size and
# embedding dim.

import gensim
from gensim.test.utils import datapath, get_tmpfile
from gensim.scripts.glove2word2vec import glove2word2vec

# If you don't want keep the new format file, can use the tmp file.
# Otherwise, you can keep the file in another path
glove_file = datapath('./glove.840B.300d.txt')
tmp_file = get_tmpfile("test_word2vec.txt")

_ = glove2word2vec(glove_file, tmp_file)
model = gensim.models.KeyedVectors.load_word2vec_format(tmp_file)
