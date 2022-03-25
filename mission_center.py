import requests


# /api
class MissionCenter:

    def __init__(self, host, headers, cookies):
        self.host = host
        self.headers = headers
        self.cookies = cookies

    def get_tasks(self, begin, end, **kwargs):
        host = self.host
        headers = self.headers
        cookies = self.cookies
        for k, v in kwargs.items():
            if k == 'host':
                host = v
            elif k == 'header':
                headers = v
            elif k == 'cookies':
                cookies = v
        return requests.get(f'{host}/api/tasks/joined', headers=headers,
                            params={'begin': begin, 'end': end}, cookies=cookies)

    def init_mission(self, **kwargs):
        host = self.host
        headers = self.headers
        cookies = self.cookies
        for k, v in kwargs.items():
            if k == 'host':
                host = v
            elif k == 'header':
                headers = v
            elif k == 'cookies':
                cookies = v
        return requests.post(f'{host}/api/task/init', headers=headers, cookies=cookies)

    def get_task(self):
        pass

    def get_numbers(self):
        pass

    def start_mission(self):
        pass

    def submit_mission(self):
        pass

    def add_numbers(self):
        pass

    def upload_numbers(self):
        pass
