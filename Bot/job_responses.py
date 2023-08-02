import requests
from tokens import access_token
import pprint


class Responses:
    """Откликается на вакансии из search/vacancies"""

    def __init__(self):
        self.api_ulr = 'https://api.hh.ru/vacancies'
        self.token_type = "bearer"
        self.access_token = access_token["access_token"]

    def get_resume_id(self):
        """Авторизуется под пользователем, 
        отправляет запрос на получение резюме и извлекает идентификатор резюме"""
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'HH-User-Agent': 'Job-Seeker (simplelogin-newsletter.ei40x@aleeas.com)'
        }
        params = {
            'locale': 'RU',
            'host': 'hh.ru'
        }
        resume_id = requests.get('https://api.hh.ru/resumes/mine', headers=headers, params=params)
        id = resume_id.json()['items'][0]["similar_vacancies"]['url']
        result = id.split('/')[-2] # делит ссылку по слешам и выдает 2 итем с конца
        return result
    
    def responses_on_vacancies(self):

        params = {
            'page': '10',
            'per_page': '20',
            'text': 'name:(python or django or DRF or backend) description:(python or django or DRF or PostgreSQL) Not ментор NOT Senior not Преподаватель NOT TechLead NOT техлид NOT middle NOT golang NOT java NOT PHP NOT middle+ NOT mld NOT mld+ NOT C# NOT C++ NOT Ruby NOT Node.js NOT Teamlead NOT тимлид NOT наставник'
        }


pprint.pp(Responses().get_resume_id())
