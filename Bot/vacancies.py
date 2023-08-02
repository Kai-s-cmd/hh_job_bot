import requests
import pprint
from tokens import apps_access_token


class SearchVacancies:
    """Авторизуется с помощью токена приложения и получает вакансии по поисковому запросу."""
    def __init__(self):
        self.api_ulr = 'https://api.hh.ru/vacancies'
        self.token_type = 'bearer'
        self.access_token = apps_access_token

    def searching(self):
        params = {
            'page': '10',
            'per_page': '20',
            'text': 'name:(python or django or DRF or backend) description:(python or django or DRF or PostgreSQL) Not ментор NOT Senior not Преподаватель NOT TechLead NOT техлид NOT middle NOT golang NOT java NOT PHP NOT middle+ NOT mld NOT mld+ NOT C# NOT C++ NOT Ruby NOT Node.js NOT Teamlead NOT тимлид NOT наставник'
        }
        headers = {
            'OauthToken': f'{self.token_type} {self.access_token}',
            'User-Agent': 'Job-Seeker (simplelogin-newsletter.ei40x@aleeas.com)'
        }
        result = requests.get(self.api_ulr, params=params, headers=headers)
        return result.json()


pprint.pp(SearchVacancies().searching())



