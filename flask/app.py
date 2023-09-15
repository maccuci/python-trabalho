from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tarefas = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tarefa = request.form['tarefa_nome']
        tarefas.append(tarefa)
        return redirect(url_for('index'))
    return render_template('index.html', tarefas=tarefas)

@app.route('/deletar/<int:index>')
def delete(index):
  if 0 <= index < len(tarefas):
    del tarefas[index]

  # Renderiza a página de exclusão
  return render_template('index.html', tarefas=tarefas)

if __name__ == '__main__':
    app.run(debug=True)
