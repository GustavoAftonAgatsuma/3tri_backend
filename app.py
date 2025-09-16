# rodar no cmd
#pip install flask

#importar a bliblioteca flask
from flask import flask
#criar uma instancia da aplicação flask
app = flask(__name__)
#este é um decorador que assosia a URL
# '/' (a URL raiz do site) à função que vem logo abaixo
@app.route('/")
#a função que é executada quando a rota '/' é acessada
#ela retorna a string "Hello, World!""
def hello_world()
    return 'Hello, World!'

#executa o servidor de desenvolvimento
if __name__ == '__main__':
    app.run(debug=True)