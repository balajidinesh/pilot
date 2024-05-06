import ollama
from ollama import AsyncClient

# client = Client(host="localhost", port=8080)

CLIENT = AsyncClient(host='http://localhost:11434')

MODEL_FILE_DEF = '''
FROM llava:latest

PARAMETER mirostat_tau 0.4
PARAMETER num_ctx 4096
PARAMETER temperature 0.7
PARAMETER top_k 30
PARAMETER top_p 0.7
'''

BASEMODEL = 'llava'
MODEL = 'operate-v'


def model_from_llava(client=CLIENT, model=MODEL, model_file=MODEL_FILE_DEF):
    try:
        client.chat(model=BASEMODEL)
    except ollama.ResponseError as e:
        print('Error:', e.error)
        if e.status_code == 404:
            client.pull(BASEMODEL)
    try:
        client.chat(model=model)
    except ollama.ResponseError as e:
        print('Error:', e.error)
        if e.status_code == 404:
            client.create(model=MODEL, modelfile=model_file)
