import requests


# /api
class MissionCenter:

    def __init__(self, base_url, headers, cookies):
        self.base_url = base_url
        self.headers = headers
        self.cookies = cookies

    def get_tasks(self, begin, end, **kwargs):
        base_url = self.base_url
        headers = self.headers
        cookies = self.cookies
        for k, v in kwargs.items():
            if k == 'base_url':
                base_url = v
            elif k == 'header':
                headers = v
            elif k == 'cookies':
                cookies = v
        return requests.get(f'{base_url}/api/tasks/joined', headers=headers,
                            params={'begin': begin, 'end': end}, cookies=cookies)

    def init_mission(self, **kwargs):
        base_url = self.base_url
        headers = self.headers
        cookies = self.cookies
        for k, v in kwargs.items():
            if k == 'base_url':
                base_url = v
            elif k == 'header':
                headers = v
            elif k == 'cookies':
                cookies = v
        return requests.post(f'{base_url}/api/task/init', headers=headers, cookies=cookies)

    def get_task(self, task_id, **kwargs):
        base_url = self.base_url
        headers = self.headers
        cookies = self.cookies
        for k, v in kwargs.items():
            if k == 'base_url':
                base_url = v
            elif k == 'header':
                headers = v
            elif k == 'cookies':
                cookies = v
        return requests.get(f'{base_url}/api/task/{task_id}', headers=headers, cookies=cookies)

    def get_numbers(self, task_id, begin, end, status, **kwargs):
        base_url = self.base_url
        headers = self.headers
        cookies = self.cookies
        for k, v in kwargs.items():
            if k == 'base_url':
                base_url = v
            elif k == 'header':
                headers = v
            elif k == 'cookies':
                cookies = v
        return requests.get(f'{base_url}/api/task/{task_id}/number/list', headers=headers, cookies=cookies,
                            params={
                                'task_id': task_id,
                                'begin': begin,
                                'end': end,
                                'status': status
                            })

    def start_mission(self, task_ids, **kwargs):
        base_url = self.base_url
        headers = self.headers
        cookies = self.cookies
        for k, v in kwargs.items():
            if k == 'base_url':
                base_url = v
            elif k == 'header':
                headers = v
            elif k == 'cookies':
                cookies = v
        return requests.put(f'{base_url}/api/tasks/start', headers=headers, cookies=cookies,
                            data={
                                'open_diagnosis': 0,
                                'task_ids': task_ids
                            })

    def submit_mission(self, task_id, task_setting, **kwargs):
        base_url = self.base_url
        headers = self.headers
        cookies = self.cookies
        for k, v in kwargs.items():
            if k == 'base_url':
                base_url = v
            elif k == 'header':
                headers = v
            elif k == 'cookies':
                cookies = v
        return requests.post(f'{base_url}/api/task/{task_id}/v2', headers=headers, cookies=cookies,
                             data=task_setting)

    def add_numbers(self, task_id, contacts, **kwargs):
        base_url = self.base_url
        headers = self.headers
        cookies = self.cookies
        for k, v in kwargs.items():
            if k == 'base_url':
                base_url = v
            elif k == 'header':
                headers = v
            elif k == 'cookies':
                cookies = v
        return requests.put(f'{base_url}/api/task/{task_id}/numbers/add', headers=headers, cookies=cookies,
                            data=contacts)

    def upload_numbers(self, task_id, excel_file, **kwargs):
        base_url = self.base_url
        headers = self.headers
        cookies = self.cookies
        for k, v in kwargs.items():
            if k == 'base_url':
                base_url = v
            elif k == 'header':
                headers = v
            elif k == 'cookies':
                cookies = v
        return requests.put(f'{base_url}/api/task/{task_id}/numbers/upload', headers=headers, cookies=cookies,
                            files={'file': excel_file})
