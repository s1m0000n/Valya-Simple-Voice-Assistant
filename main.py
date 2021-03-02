from text import TextProcessor
import speech_recognition as sr
import pyttsx3
from intents import IntentClassifier, valya_intents

bye_msg = 'До скорой встречи!'
text_processor = TextProcessor()


def process_request(query: str) -> str:
    classifier = IntentClassifier(valya_intents)
    doc = text_processor(query)
    intent_class = classifier(doc)
    if intent_class:
        if intent_class == bye_msg:
            return intent_class
        try:
            obj = doc.spans[0].normal.lower()
            return intent_class(obj)()
        except IndexError:
            for lemma in [token.lemma for token in doc.tokens]:
                obj = lemma.lower()
                answer = intent_class(obj)()
                if answer not in ('Даже не знаю, о чём вы это говорите',
                                  'Даже не знаю, какая тут может быть погода'):
                    return answer
            return intent_class('a')()
    else:
        return ''


def voice_assistant(debug=False):
    rec = sr.Recognizer()
    mic = sr.Microphone()
    if debug: print('Удачно инициализирован микрофон и распознаватель речь')
    speech_engine = pyttsx3.init()
    speech_engine.setProperty('voice', 'ru')
    if debug: print('Удачно инициализирован генератор речи')
    while True:
        with mic as source:
            print('Говорите')
            audio = rec.listen(source)
        try:
            query = rec.recognize_google(audio, language='ru-RU')
        except sr.UnknownValueError:
            query = 'Я не поняла ваш запрос, пожалуйста, повторите'
        if debug: print(f'Услышан запрос: {query}')
        result = process_request(query)
        if debug: print(f'Ответ на запрос: {result}')
        speech_engine.say(result)
        speech_engine.runAndWait()
        if result == bye_msg:
            exit()
        if debug: print('Голосовой генератор завершил работу')


if __name__ == '__main__':
    communication_type = 0
    while communication_type not in ('1', '2'):
        communication_type = input('Как бы вы хотели общаться:\n1. Сообщения\n2. Говорить\n> ')
    if communication_type == '1':
        while True:
            text = input('> ')
            print(process_request(text))
    else:
        voice_assistant()
