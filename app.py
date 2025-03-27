from time import strftime

from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec

from datetime import date

tempo = date.today()

print(f'ano {tempo.year}')
print(f'mes {tempo.month}')
print(f'dia {tempo.day}')

app = Flask(__name__)
spec = FlaskPydanticSpec('flask',
                         title='Flask API',
                         version='1.0')
spec.register(app)


@app.route("/")
def hello_world():
    return f'ola Mundo!'


@app.route("/<ano>/<mes>/<dia>")
def calcula_data(ano, mes, dia):

    try:
        data_da_rota = date(int(ano), int(mes), int(dia))

        if tempo.year < data_da_rota.year:
            situacao = 'futuro'
        elif tempo.year > data_da_rota.year:
            situacao = 'passado'
        else:
            situacao = 'presente'
        resultado_da_subtracao = data_da_rota - tempo
        dias_de_diferenca = resultado_da_subtracao.days
        meses_diferenca = abs(tempo.year - data_da_rota.year) * 12 + abs(tempo.month - data_da_rota.month)
        anos_diferenca = tempo.year - data_da_rota.year
        return jsonify({'situacao': situacao,
                        'dias de diferenca': abs(dias_de_diferenca),
                        'meses de diferenca': abs(meses_diferenca),
                        'ano de diferenca': abs(anos_diferenca)
                        })
    except ValueError:
        return f'dado invalido'




if __name__ == "__main__":
    app.run(debug=True)