import json
import requests
import yaml
from yaml import Loader

REQUEST_URL = 'http://localhost:5005/model/parse'
NLU_YAML_PATH = 'C:\\Users\\gabriel.bercanu\\Desktop\\Work\\transcript-creator\\chatbot-github\\Streamlist-chatbot-en\\data\\nlu.yml'

def main():
    obj = {'text': 'hello!'}
    response = requests.post(REQUEST_URL, data=json.dumps(obj))
    response = response.json()
    #print(response.json())
    intent = response['intent']
    print('Intent: {}'.format(intent))
    
    with open(NLU_YAML_PATH, 'r') as f:
        try:
            intent_data = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)
        
    #print('Intent data: {}'.format(intent_data))
    nlu = intent_data['nlu']
    for nlu_entry in nlu:
        intent = nlu_entry['intent']
        examples = nlu_entry['examples']
        split_examples = examples.split('\n')[:-1] # ignore last training newline producing and empty string
        split_examples = list(map(lambda x : x[2:], split_examples)) # remove leading hypen and whitespace separator
        print('{} split examples: {}'.format(intent, split_examples))
        
        for split_example in split_examples:
            req_obj = {'text':split_example}
            response = requests.post(REQUEST_URL, data=json.dumps(req_obj)).json()
            
        print('-----------------------------------------')

if __name__ == '__main__':
    main()