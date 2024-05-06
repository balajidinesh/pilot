import ollama


model_file = '''
FROM llava:latest


PARAMETER mirostat_tau 0.4
PARAMETER num_ctx 4096
PARAMETER temperature 0.7
PARAMETER top_k 30
PARAMETER top_p 0.7


'''


ollama.show('llava')