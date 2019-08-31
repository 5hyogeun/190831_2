from flask import Flask
from flask import render_template, request, jsonify
import re
from calculator.controller import CalculatorController

app = Flask(__name__)

@app.route("/move/<path>")
def move(path):
    return render_template('{}.html'.format(path))

@app.route('/ui_calc')
def ui_calc():
    stmt = request.args.get('stmt', 'NONE')
    if(stmt == 'NONE'):
        print('넘어온 값이 없음')
    else:
        print('넘어온 식 : {}'.format(stmt))    # 5 + 8
        patt = '[0-9]+'
        op = re.sub(patt, '', stmt)
        print('넘어온 연산자 : {}'.format(op))
        nums = stmt.split(op)
        result = 0
        n1 = int(nums[0])
        n2 = int(nums[1])
        if op == '+': result = n1 + n2
        elif op == '-': result = n1 - n2
        elif op == '*': result = n1 * n2
        elif op == '/': result = n1 / n2

    return jsonify(result=result)

@app.route("/ai_calc", methods = ["POST"])
def ai_calc():
    num1 = request.form['num1']
    num2 = request.form['num2']
    opcode = request.form['opcode']
    c = CalculatorController(num1, num2, opcode)
    result = c.calc()
    render_params = {}
    render_params['result'] = int(result)
    return render_template('ai_calc.html', **render_params)    # 플라스크 진자

@app.route("/")
def index():
    return render_template('index.html')    # index에 있는 것을 긁어오는 method

if __name__ == '__main__':
    app.debug = True
    app.run()