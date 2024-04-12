from flask import Flask, request, jsonify, send_from_directory
from nltk.chat.util import Chat, reflections
import random
import os

app = Flask(__name__)

patterns = [
    (r'Oi|Olá|Hey|E aí', ['Olá! Como posso ajudar você hoje?', 'Oi! Em que posso ser útil?', 'Hey! Em que posso ajudar?']),
    (r'Quero marcar uma consulta|Preciso de uma consulta|Quero agendar uma consulta|Como marcar uma consulta?', ['Claro! Para marcar uma consulta, por favor, me informe sua especialidade médica e sua disponibilidade de horário.']),
    (r'Qual é a especialidade médica?|Quais são as especialidades disponíveis?|Quais médicos estão disponíveis?', ['Atualmente, temos especialidades como Clínica Geral, Pediatria, Ginecologia, entre outras.']),
    (r'Quais são os horários disponíveis?|Quando há horários vagos?|Quais são os horários de consulta?', ['Os horários disponíveis variam de acordo com a especialidade médica e a agenda dos profissionais. Por favor, me informe a especialidade desejada para que eu possa verificar os horários disponíveis.']),
    (r'Como cancelar uma consulta marcada?|Preciso cancelar meu agendamento|Quero desmarcar minha consulta', ['Para cancelar uma consulta já marcada, por favor, forneça o seu nome completo, a data e o horário da consulta que deseja cancelar.']),
    (r'Posso alterar minha consulta?|Quero mudar o horário da minha consulta|Gostaria de remarcar minha consulta', ['Sim, é possível alterar o horário da sua consulta. Por favor, me informe o seu nome completo, a data e o horário da consulta atual e o novo horário desejado.']),
    (r'(.*)', ["Desculpe, não entendi. Poderia reformular a pergunta?", "Não consigo responder a isso.", "Isso está além do meu conhecimento."])
]

chatbot = Chat(patterns, reflections)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data['input']
    response = chatbot.respond(user_input)
    return jsonify({'response': response})

# Rota para servir o arquivo HTML
@app.route('/')
def index():
    return send_from_directory(os.path.dirname(__file__), 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
