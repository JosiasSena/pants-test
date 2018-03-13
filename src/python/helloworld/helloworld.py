from fibonaccihelper import FibonacciHelper
from flask import Flask

app = Flask(__name__)
fib_helper = FibonacciHelper()


@app.route("/")
def index():
    return "Hello World - Lets do some Fibonacci calculations!"


@app.route("/<fibo_number>")
def fibonacci(fibo_number):
    return str(fib_helper.get_fibonacci_number(int(fibo_number)))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
