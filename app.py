from flask import Flask
from flask import jsonify

alunos = [
    {
        'id': '1',
        'nome': 'Marcos'
    },
	{
        'id': '2',
        'nome': 'Tamires'
    },
	{
        'id': '3',
        'nome': 'Kassia'
    },
	{
        'id': '4',
        'nome': 'Daisy'
    },
	{
        'id': '5',
        'nome': 'Juca'
    }
]

app = Flask(__name__)

@app.route('/alunos', methods=['GET'])
def get_alunos():
	return jsonify({'alunos':alunos})

@app.route('/alunos/<string:nome>', methods=['GET'])
def get_aluno(nome):
	for aluno in alunos:
		if aluno['nome'] == nome:
			return ("O aluno " + aluno['nome'] + " tem ID = " + aluno['id'])
	return "Aluno não existe!"
	

if __name__=="__main__":
	app.run(port=80, debug=True)