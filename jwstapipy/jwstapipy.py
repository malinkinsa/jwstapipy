import httpx

from typing import List, Dict, Optional


class JwstAPI:
    def __init__(self, api_key: str) -> str:

        self.url = 'https://api.jwstapi.com'
        self.headers = {
            'X-API-KEY': api_key,
            'Content-Type': 'application/json',
        }

    async def get_version(self):
        with httpx.Client() as version_client:
            response = version_client.get(
                url=self.url,
                headers=self.headers,
            )

            if response.status_code == 200:
                return response.json()['body']
            else:
                return response.json()['error']

    async def get_programs_list(self) -> List:

        programs_list = []
        url = f'{self.url}/program/list'

        with httpx.Client() as programs_list_client:
            response = programs_list_client.get(
                url=url,
                headers=self.headers,
            )

            if response.status_code == 200:
                for program_id in response.json()['body']:
                    programs_list.append(program_id['program'])

                return programs_list
            else:
                return response.json()['error']

    async def get_suffixes_list(self) -> List[Dict]:
        suffixes_list = []

        url = f'{self.url}/suffix/list'

        with httpx.Client() as suffixes_list_client:
            response = suffixes_list_client.get(
                url=url,
                headers=self.headers,
            )

            if response.status_code == 200:
                for suffix in response.json()['body']:
                    data = {
                        'suffix': suffix['suffix'],
                        'instruments': suffix['instruments'],
                        'description': suffix['description'],
                    }

                    suffixes_list.append(data)

                return suffixes_list
            else:
                return response.json()['error']

    async def get_program_data(self, program_id: str, first_page: Optional[int] = 1, last_page: Optional[int] = None,
                               per_page: Optional[int] = 10) -> List[Dict]:

        url = f'{self.url}/program/id/{program_id}'
        return await self.data_processing(url, first_page, last_page, per_page)

    async def get_data_by_suffix(self, suffix: str, first_page: Optional[int] = 1, last_page: Optional[int] = None,
                                 per_page: Optional[int] = 10) -> List[Dict]:

        url = f'{self.url}/all/suffix/{suffix}'
        return await self.data_processing(url, first_page, last_page, per_page)

    async def get_files_by_type(self, file_type: str, first_page: Optional[int] = 1, last_page: Optional[int] = None,
                                per_page: Optional[int] = 10) -> List[Dict]:

        url = f'{self.url}/all/type/{file_type}'
        return await self.data_processing(url, first_page, last_page, per_page)

    async def get_data_by_observation(self, observation: str, first_page: Optional[int] = 1,
                                      last_page: Optional[int] = None, per_page: Optional[int] = 10) -> List[Dict]:

        url = f'{self.url}/observation/{observation}'
        return await self.data_processing(url, first_page, last_page, per_page)

    async def data_processing(self, url, first_page: Optional[int] = 1, last_page: Optional[int] = None,
                              per_page: Optional[int] = 10):

        data = []
        start_page = first_page

        if last_page:
            for page in range(first_page, last_page):
                with httpx.Client() as program_client:
                    response = program_client.get(
                        url=f'{url}?page={page}&perPage={per_page}',
                        headers=self.headers,
                    )

                    if response.status_code == 200:
                        result = response.json()['body']
                        if not result:
                            break
                        else:
                            data.extend(result)

                    else:
                        return response.json()['error']
        else:
            pagination = True
            with httpx.Client() as program_client:
                while pagination:
                    response = program_client.get(
                        url=f'{url}?page={start_page}&perPage={per_page}',
                        headers=self.headers,
                    )

                    if response.status_code == 200:
                        result = response.json()['body']
                        if not result:
                            pagination = False
                        else:
                            data.extend(result)
                            start_page += 1
                    else:
                        return response.json()['error']

        return data
