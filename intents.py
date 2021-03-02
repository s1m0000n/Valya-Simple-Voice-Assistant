import csv


class IntentClassifier:
    def __init__(self, intent_pairs: dict):
        self.intent_pairs = intent_pairs

    def __call__(self, query: str):
        for key, value in self.intent_pairs.items():
            if query in key:
                return value
        return DontKnowIntent


class IntentKeywords:
    def __init__(self, keywords: tuple):
        self.keywords = keywords

    def __contains__(self, doc) -> bool:
        for keyword in self.keywords:
            if isinstance(keyword, str):
                for token in doc.tokens:
                    if token.lemma == keyword:
                        return True
            else:
                for i in range(len(doc.tokens)):
                    if doc.tokens[i].lemma == keyword[0] and doc.tokens[i + 1].lemma == keyword[1]:
                        return True
        return False


class WeatherIntent:
    def __init__(self, city='москва'):
        self.city = city

    def __call__(self, *args, **kwargs) -> str:
        with open('sample_weather.csv', mode='r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == self.city:
                    return f'В {row[1].strip().title()} {row[2].strip()} градусов по Цельсию и {row[3].strip()}.'
            return 'Даже не знаю, какая тут может быть погода'


class WhoIsIntent:
    def __init__(self, obj: str):
        self.obj = obj

    def __call__(self, *args, **kwargs) -> str:
        with open('sample_whois.csv', mode='r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row[0] == self.obj:
                    return f'{self.obj.title()} - это {row[1].strip()}'
            return 'Даже не знаю, о чём вы это говорите'


class HelloIntent:
    def __init__(self, _):
        pass

    def __call__(self):
        return 'Привет, меня зовут Валя, я твой новый голосовой ассистент.'


class DontKnowIntent:
    def __init__(self, _):
        pass

    def __call__(self):
        return 'Я не поняла ваш запрос. Моя функциональность постоянно расширяется, ваш язык очень трудный! Ха-ха!'


class ThanksIntent:
    def __init__(self, _):
        pass

    def __call__(self):
        return 'Не за что, всегда готова придти на помощь!'


class HowAreYouIntent:
    def __init__(self, _):
        pass

    def __call__(self):
        return 'У меня всё хорошо, занимаюсь своими делами, ем оперативную память. А у вас как?'


class HAYAnswerReactionIntent:
    def __init__(self, _):
        pass

    def __call__(self):
        return 'Это просто здорово. Я готова вам что-нибудь рассказать, только спросите.'


valya_intents = {
    IntentKeywords(('погода', ('за', 'окно'), ('на', 'улица'))): WeatherIntent,
    IntentKeywords((('кто', 'такой'), ('что', 'такой'))): WhoIsIntent,
    IntentKeywords(('пока', 'выход')): 'До скорой встречи!',
    IntentKeywords(('привет', 'здравствуй', 'здравствуйте', ('добрый', 'день'), ('добрый', 'вечер'))): HelloIntent,
    IntentKeywords(('спасибо',)): ThanksIntent,
    IntentKeywords((('как', 'дела'), ('как', 'делишки'), ('как', 'дело'),
                    ('как', 'поживать'), ('что', 'новый'),)): HowAreYouIntent,
    IntentKeywords(('хорошо', 'отлично', 'нормально', 'хороший',
                    'отличный', 'нормальный', 'чудесно', 'чудесный')): HAYAnswerReactionIntent,
}
