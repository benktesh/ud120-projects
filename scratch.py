#Rn this first
import nltk
if(nltk.corpus):
    pass
else:
    nltk.dowload
from nltk.corpus import stopwords
sw = stopwords.words("english")
print ('Number stopwords: ', len(sw))

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
print (stemmer.stem("responsiveness"))

print (stemmer.stem("unresponsive"))


