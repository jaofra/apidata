from datetime import date
from dateutil.relativedelta import relativedelta
from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec
app = Flask(__name__)

spec = FlaskPydanticSpec('flask',
                         title='Flask API',
                         version='1.0')
spec.register(app)
@app.route('/')
def index():
    return jsonify({"hello": "world"})

@app.route('/<quantidade>/<tipo>')
def data_de_validade(quantidade, tipo):
    data_atual = date.today()
    qtde = int(quantidade)
    if tipo in ["dia", "dias", "day","days"]:
        data_atual + relativedelta(months=qtde)

    return jsonify({"A data de validade do produto é ": "data_de_validade"})


if __name__ == '__main__':
    app.run(debug=True)