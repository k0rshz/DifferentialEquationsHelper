from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

WOLFRAM_APP_ID = "Y32RKW-G9Q4U3TJJ9"

def query_wolfram_alpha(equation):
    url = "http://api.wolframalpha.com/v2/query"
    params = {
        "input": f"solve {equation}",  # запрос на решение уравнения
        "format": "plaintext",
        "output": "JSON",
        "appid": WOLFRAM_APP_ID
    }

    response = requests.get(url, params=params)
    data = response.json()

    try:
        solution = data["queryresult"]["pods"][1]["subpods"][0]["plaintext"]
        return solution if solution else "Решение не найдено"
    except (KeyError, IndexError):
        return "Решение не удалось найти"

@app.route("/solve_equation", methods=["POST"])
def solve_equation():
    data = request.get_json()
    equation = data.get("equation")
    if not equation:
        return jsonify({"error": "Уравнение не предоставлено"}), 400
    solution = query_wolfram_alpha(equation)
    return jsonify({"solution": solution})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)