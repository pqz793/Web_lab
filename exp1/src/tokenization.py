#import sys
#sys.path.append(r'E://nltk_data')

import nltk

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

print(nltk.sent_tokenize(EXAMPLE_TEXT))
