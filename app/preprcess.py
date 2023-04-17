
from translate import Translator

def ko_to_en(text : str):
    translator = Translator(from_lang="ko", to_lang="en")
    
    return translator.translate(text)


def ko_preprocessing(content, n):
    return content.replace(str(n)+'. ',"")
