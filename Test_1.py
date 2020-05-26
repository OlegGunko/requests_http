import requests
import yadisk

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

y = yadisk.YaDisk(token=token)

def translate_it(file_from, file_to, lang_from, lang_to='ru'):
    with open(file_from, encoding='UTF-8') as f:
        text = []
        for line in f:
            line = line.strip()
            text.append(line)

        params = {
            'key': API_KEY,
            'text': text,
            'lang': lang_from + '-' + lang_to,

        }

        response = requests.get(URL, params=params)
        json_ = response.json()
        result = ''.join(json_['text'])

    with open(file_to, 'w', encoding='UTF-8') as new:
        new.write(result)
    return f'Перевод текста записан в файл {file_to}'


def upload_disk(list_files = []):
    y.mkdir ('/Test_2')
    for path in list_files:
        with open (path, 'rb') as f:
            y.upload (f, f'Test_2/translatefrom_{path}')
    return 'Файлы загружены'


if __name__ == '__main__':
    print(translate_it('DE.txt', 'DE_RU.txt', 'de'))
    print(translate_it('ES.txt', 'ES_RU.txt', 'es'))
    print(translate_it('FR.txt', 'FR_RU.txt', 'fr'))
    print(upload_disk(['DE_RU.txt', 'ES_RU.txt', 'FR_RU.txt']))