from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/pwd-generator", methods=["GET"])
def generate_password():
    name = request.args.get("name")

    if not name:
        return jsonify({"error": "Name parameter is mandatory."}), 400
    
    pwd = f"{name}123"
    return jsonify({"password": pwd})

if __name__ == "__main__":
    app.run(debug=True)