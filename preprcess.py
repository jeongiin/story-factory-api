
from translate import Translator

def ko_to_en(text : str):
    translator = Translator(from_lang="ko", to_lang="en")
    
    return translator.translate(text)


def ko_preprocessing(content_array, n):
    result_array = []
    for content in content_array:
        result_array.append(content.replace(str(n)+'. ',""))
    return result_array

