import json

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

def read_json(path) -> dict | list[dict]:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_index(agent: Elasticsearch, index_name: str, settings):
    agent.indices.create(index=index_name, body=settings)
    
def upload(index, data):
    for item in data:
        yield{
            '_index': index,
            '_source': item
        }

def main():
    login = 'jinr_school_34'
    password = 'U6d3HG4v'
    index = 'jobhunt_34'
    url = 'https://pluton.mephi.ru/elk-e'
    es = Elasticsearch(
        url,
        basic_auth=(login, password)
    )
    print(es.info())
    #settings = read_json('data/mapping.json')
    #create_index(es, index, settings)
    data = read_json('data/data.json')
    bulk(es, upload(index=index, data=data))
if __name__ == '__main__':
    main()