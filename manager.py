import requests
from abc import ABC, abstractmethod
from emoji import is_emoji


class ManagerInterface(ABC):
    @abstractmethod
    def update_emoji(self, id_emodji: int, new_emoji: str, endpoint: str, data: str):
        pass

    @abstractmethod
    def add_new_emoji(self, emoji: str):
        pass

    @abstractmethod
    def delete_emoji(self, id: int):
        pass


class Manager(ManagerInterface):
    def __init__(self, base_usl: str):
        self.base_url = base_usl

    def _send_request(self, method: str, endpoint: str, data=None) -> requests.Response:
        url = f'{self.base_url}/{endpoint}'
        headers = {'Contex-Type': 'application/json'}

        if method == 'PUT':
            response = requests.put(url, json=data, headers=headers)
        if method == 'POST':
            response = requests.post(url, json=data, headers=headers)
        if method == 'DELETE':
            response = requests.delete(url, headers=headers)

        return response

    def add_new_emoji(self, emoji: str) -> str:
        data = {'emoji': emoji}
        response = self._send_request(method='POST', endpoint='govno', data=data)
        if isinstance(response, requests.Response):
            if response.status_code == 200:
                print('SUCCESS!')
            elif response.status_code == 409:
                print('Error : Dublicate')
            else:
                print("I don't know what is this")

        return 'ABOBUS'

    def update_emoji(self, emoji_id: int, new_emoji: str) -> requests.Response:
        data = {'emoji': new_emoji}
        response = self._send_request(method='PUT', endpoint=f'govno/{emoji_id}', data=data)
        if isinstance(response, requests.Response):
            if response.status_code == 200:
                print('SUCCESS!')
            elif response.status_code == 404:
                print('Error : Not Found')
            else:
                print("I don't know what is this")

    def delete_emoji(self, id: int) -> requests.Response:
        response = self._send_request(method='DELETE', endpoint=f'govno/{id}')
        if isinstance(response, requests.Response):
            if response.status_code == 200:
                print('SUCCESS!')
            else:
                print("I don't know what is this")


if __name__ == '__main__':
    put_manager = Manager('http://127.0.0.1:5000')

    new_emoji = '❎'
    put_manager.delete_emoji()
