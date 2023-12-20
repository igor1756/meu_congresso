from flask import Flask, render_template, request, redirect, url_for, session
# from models.questions import Question
import models.questions as q

app = Flask(__name__)
app.secret_key = 'chave_secreta'

# Lista de perguntas e respostas (agora com opções)

questions = q.itens

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # na primeira vai entrar e criar score
    if 'score' not in session:
        session['score'] = 0
        session['question_index'] = 0

    if request.method == 'POST':
        # pega a resposta dada pelo jogador
        user_answer = request.form.get('answer', '').strip()
        # pega a resposta correta
        correct_answer = questions[session['question_index']]["resposta_correta"]

        # comparara ambas e soma no placar se coincidir
        if user_answer == correct_answer:
            session['score'] += 1

        # passa pra proxima pergunta
        session['question_index'] += 1

        # Verifica se todas as perguntas foram respondidas
        if session['question_index'] == len(questions):
            return redirect(url_for('score'))

    # verifica de novo se ha perguntas
    if session['question_index'] < len(questions):
        # pega o dict com a questao da vez
        current_question = questions[session['question_index']]
        # manda a questão pro jogo
        return render_template('quiz.html', question=current_question)
    # se acabaram as perguntas mostra o placar
    else:
        return redirect(url_for('score'))

@app.route('/score')
def score():
    final_score = session['score']
    session.clear()
    return render_template('score.html', final_score=final_score)

if __name__ == '__main__':
    app.run(debug=True)
