from flask import Flask, request, jsonify
from database import Database
app = Flask("NSO_HomeAssignment")

db = Database()


@app.route("/AddMessage", methods=["POST"])
def add_message():

    data = request.get_json()
    
    application_id = data.get('application_id')
    session_id = data.get('session_id')
    message_id = data.get('message_id')
    participants = str(data.get('participants'))
    content = data.get('content')
    if None in (application_id, session_id, message_id, participants, content):
        return jsonify({"error": "Missing required parameters"}), 400
    db.add_message(application_id, session_id, message_id, participants, content)
    return jsonify({"status": "OK"}), 200

@app.route("/GetMessage", methods=["GET"])
def get_message():
    application_id, session_id, message_id = get_params_url()
    # if all the parameters are None, return 400
    if all([not application_id, not session_id, not message_id]):
        return jsonify({"error": "Missing required parameters"}), 400
    message = db.get_message(application_id, session_id, message_id)
    return (jsonify(message), 200) if message else (jsonify({"error": "Message not found"}), 404)


@app.route("/DeleteMessage", methods=["DELETE"])
def delete_message():
    try:
        application_id, session_id, message_id = get_params_url()
        db.delete_message(application_id, session_id, message_id)
    except:
        return jsonify({"error": "Message not found"}), 404
    return jsonify({"status": "OK"}), 200

def get_params_url():
    """Get parameters from url"""
    application_id = request.args.get('applicationId')
    session_id = request.args.get('sessionId')
    message_id = request.args.get('messageId')

    return application_id, session_id, message_id
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
