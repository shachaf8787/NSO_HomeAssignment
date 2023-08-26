from flask import Flask, request, jsonify

app = Flask("NSO_HomeAssignment")


@app.route("/AddMessage", methods=["POST"])
def add_message():

    data = request.get_json()
    
    application_id = data.get('application_id')
    session_id = data.get('session_id')
    message_id = data.get('message_id')
    participants = data.get('participants')
    content = data.get('content')
    if None in [application_id, session_id, message_id, participants, content]:
        return jsonify({"error": "Missing required parameters"}), 400
     
    return jsonify({"status": "OK"}), 200

@app.route("/GetMessage", methods=["GET"])
def get_message():
    return "OK"


@app.route("/DeleteMessage", methods=["DELETE"])
def delete_message():
    return "OK"


    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
