import requests
import os 

url_lambda = os.getenv('URL_LAMBDA')
agent_alias_id = os.getenv('AGENT_ALIAS_ID')
agent_id = os.getenv('AGENT_ID')

headers = {
    'Content-Type': 'application/json',
}

first_menssage = """
{
    "p": "¿Cuál es el valor de 5-(-2)(-2-7)?",
    "r": {
        "a": "-63",
        "b": "-13",
        "c": "-5",
        "d": "8"
    },
    "r_correcta": "b"
}
"""
#Agente de preguntas
json_data = {
    'input_text': first_menssage,
    'agent_alias_id':agent_alias_id,
    'agent_id':agent_id
}

response = requests.post(url_lambda, headers=headers, json=json_data)

first_response_json= response.json()
print(first_response_json['r'])

session_id = first_response_json['session_id']
json_data['session_id'] = session_id

while True:
    user_input_text = input("responde: ")

    if user_input_text == 'exit':
        break

    json_data['input_text'] = user_input_text
    response = requests.post(url_lambda, headers=headers, json=json_data)
    response_json= response.json()
    print(response_json['r'])
