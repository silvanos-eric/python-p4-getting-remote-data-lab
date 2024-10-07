import requests
import json


class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        return requests.get(self.url).content

    def load_json(self):
        bytes = self.get_response_body()
        return json.loads(bytes)


if __name__ == '__main__':
    get_requester = GetRequester(
        'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
    )
    import ipdb
    ipdb.set_trace()
