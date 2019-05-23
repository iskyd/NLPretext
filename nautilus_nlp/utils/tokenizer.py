import nltk
from sacremoses import MosesTokenizer, MosesDetokenizer
import spacy
from spacy.lang.fr import French
from spacy.lang.en import English
import spacy.lang as spacylang
#nltk.download('punkt')

try:
    french_spacy = spacylang.fr.French()
except OSError:
    raise OSError("""You must install French langage to use SpaCy. 
                    python -m spacy download fr
                    See https://spacy.io/usage/ for details
                """)
try:
    english_spacy = spacylang.en.English()
except OSError:
    raise OSError("""You must install english langage to use SpaCy. 
                    python -m spacy download en
                    See https://spacy.io/usage/ for details
                """)             


def tokenize(text: str, lang_module: str = 'en_spacy'):
    """
    Convert text to a list of tokens. 

    Args:
        lang_module ({'en_spacy', 'en_nltk', 'fr_spacy', 'fr_moses'}): choose
        the tokenization module according to the langage and the implementation.
        Recommanded: Spacy (faster, better results). To process other langages
        import models.Spacy_models

    Returns:
        list
    """
    if lang_module is 'en_nltk':
        return nltk.word_tokenize(text)
    elif lang_module is 'en_spacy':
        spacydoc = english_spacy(text)
        return list(spacydoc)
    elif lang_module is 'fr_spacy':
        spacydoc = french_spacy(text)
        return list(spacydoc)
    elif lang_module is 'fr_moses':
        t = MosesTokenizer(lang='fr')
        return t.tokenize(text, escape=False)


def untokenize(tokens, lang='fr'):
    '''
    Inputs a list of tokens output string.
    ["J'", 'ai'] >>> "J' ai"
    '''
    d = MosesDetokenizer(lang=lang)
    text = d.detokenize(tokens, unescape=False)
    return text    


def _convert_tokens_to_string(tokens_or_str):
    if type(tokens_or_str) is str:
        return tokens_or_str
    elif type(tokens_or_str) is list:
        return untokenize(tokens_or_str)
    elif type(tokens_or_str) is None:
        return ''
    else:
        raise ValueError('Please input string or tokens')


def _convert_string_to_tokens(tokens_or_str, lang_module='en_spacy'):
    if type(tokens_or_str) is str:
        return tokenize(tokens_or_str, lang_module=lang_module)
    elif type(tokens_or_str) is list:
        return tokens_or_str
    elif type(tokens_or_str) is None:
        return []
    else:
        raise ValueError('Please input string or tokens')