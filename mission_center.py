import requests


# /api
class MissionCenter:

    def __init__(self, base_url, headers, cookies):
        self.base_url = base_url
        self.headers = headers
        self.cookies = cookies

    def get_tasks(self, status, begin, end, **kwargs):
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
        return requests.get(f'{base_url}/api/tasks/{status}', headers=headers,
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
                            data={
                                'contact_datas': contacts
                            })

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
        return requests.post(f'{base_url}/api/task/{task_id}/numbers/upload', headers=headers, cookies=cookies,
                            files={'file': excel_file})


if __name__ == "__main__":
    url = "http://call-test.tangees.com"
    header = {
        'Cookie': 'SecurityCenterDuId=IllPYTYvSllFMjBlRWFydTlGa1lDWWhjPSI.FSNHGQ.eghMoXas_yCVbgocZMvMGoOvyyE;accountCenterSessionId=.eJw9jk1rwzAQRP-Lzj2sVlqvlGMphEKd0kIo8cXoY0Xixi7EaV1c-t8rcuhxhnnD-1Gfs1z6U1Yb1aDVkbwXYiyAbAwl0szqTvXlIvNRbUo4z1LjbZ-5EYfWuASGcyheEzc6-xAFvMHK2sjeNtSkKOSiCxQxBV20WEBbtMmRMgoGp7MEECCEwMmVxghrK9HGWBK7rHMyjhyIDwZ8YUIL3lWvSST3c_iS_vrR5_gvON8E2_VgDkO7tOv-uhu6oTsBdNv98vT2aHdj7cbXscUX2673788P6bsepmOYJjlXeJGofv8A-dpVDg.FSNHIA.2sdkzLXiwHoI1MYtRFjVctafCUc'
    }
    cookie = {}
    test = MissionCenter(url, header, cookie)
    # get_tasks
    print(test.get_tasks('draft', '0', '1').json())
    # init_task
    init_task_res = test.init_mission().json()
    print(init_task_res)
    t_id = init_task_res['task_id']
    # get_task
    print(test.get_task(task_id=t_id).json())
    # get_numbers
    print(test.get_numbers(t_id, '0', '10', 'no_call').json())
    # start_mission
    print(test.start_mission(t_id).json())
    # submit_mission
    t_setting = {
        'name': 'api_test',
        'graph_id': '61849c29a3552266652dc7f5',
        'version_id': '61a46d8aa35522703b36af89',
        'call_line_model': 2,
        'call_port_ids': '61d6a114a35522259f5fe5c7',
        'robot_ids': '60e81728e285480159f317d7',
        'smart_diagnose_trigger': 1,
        'smart_diagnose_config': '{"open_filter_by_number":true,"harass_rule":{"filter_by_call_result":{"trigger":false},"filter_by_intention_result":{"trigger":false,"options":[]},"filter_by_days_anti_harass":{"trigger":false}}}',
        'showRule': 'false',
        'sms_trigger': 0,
        'is_transfer': 0,
        'smart_schedule_trigger': 1,
        'is_timed_task': 0,
        'redial_trigger': 0,
        'label_trigger': 0,
        'cc_assign_trigger': 0,
    }
    print(test.submit_mission(t_id, t_setting).json())
    # add_numbers
    print(test.add_numbers(t_id,
                           '[{"number": "18218644344", "contact": "jack", "enterprise": "jack\'s", "vars": {}}]').json())
    # upload_numbers
    e_file = open('C:/Users/TUNGEE/Desktop/数据流/random_phone_number/随机生成号码包20.xlsx', 'rb')
    print(test.upload_numbers(t_id, e_file).json())
