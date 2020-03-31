from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text

STOP_WORDS = stop_words = text.ENGLISH_STOP_WORDS

class SimilitudeFunction:
  def similitude(self, query, document, algorithm):
    if(algorithm == "scalarTF"):
      scalarTF = ScalarTF(STOP_WORDS)
      return scalarTF.calculate(query, document)
    #else if(algorithm == "scalarTFIDF"):
    #else if(algorithm == "cosineTF"):
    #else if(algorithm == "cosineTFIDF"):
    else:
      print("valid options For algoritm are: scalarTF, scalarTFIDF, cosineTF, cosineTFIDF")

class ScalarTF:
  def __init__(self, stopWordsList):
    if(stopWordsList):
      self.vectorizer = CountVectorizer(lowercase=False, stop_words=stopWordsList)
    else:
      self.vectorizer = CountVectorizer(lowercase=False)
  def calculate(self, query, document):
    corpusString = document.split()#CS
    matrix_tf = self.vectorizer.fit_transform(corpusString) # 1 row with n columns = dictionary words
    analyze = self.vectorizer.build_analyzer()
    print(analyze(document))
    q_tf = self.vectorizer.transform([query])
    print(matrix_tf.shape)
    print(q_tf.shape)
    similarity = matrix_tf.dot(q_tf.transpose())
    #print("##############")
    print("similarity: ")
    print(similarity)
    return similarity
#class ScalarTFIDF:
#class CosineTF:
#class CosineTFIDF:

