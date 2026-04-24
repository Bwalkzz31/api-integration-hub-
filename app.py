from flask import Flask, render_template, jsonify, request
import uuid
from datetime import datetime

app = Flask(__name__)

event_log = []
integrations = {
    "crm":       {"name": "CRM System",          "status": "connected",    "synced": 0, "icon": "👥"},
    "marketing": {"name": "Marketing Platform",  "status": "connected",    "synced": 0, "icon": "📣"},
    "database":  {"name": "Database Tool",       "status": "connected",    "synced": 0, "icon": "🗄️"},
    "analytics": {"name": "Analytics Engine",    "status": "disconnected", "synced": 0, "icon": "📊"},
}

def log_event(source, event_type, payload, status="success"):
    event = {
        "id": str(uuid.uuid4())[:8],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source": source,
        "type": event_type,
        "payload": payload,
        "status": status
    }
    event_log.insert(0, event)
    if len(event_log) > 50:
        event_log.pop()
    return event

@app.route("/")
def dashboard():
    return render_template("dashboard.html", integrations=integrations)

@app.route("/api/integrations", methods=["GET"])
def get_integrations():
    return jsonify({"integrations": integrations, "total": len(integrations)})

@app.route("/api/integrations/<key>/sync", methods=["POST"])
def sync_integration(key):
    if key not in integrations:
        return jsonify({"error": "Integration not found"}), 404
    ig = integrations[key]
    if ig["status"] == "disconnected":
        return jsonify({"error": f"{ig['name']} is disconnected"}), 400
    records = (request.json or {}).get("records", 10)
    ig["synced"] += records
    event = log_event(ig["name"], "SYNC", {"records_synced": records, "total_synced": ig["synced"]})
    return jsonify({"message": f"Synced {records} records from {ig['name']}", "event": event})

@app.route("/api/integrations/<key>/toggle", methods=["POST"])
def toggle_integration(key):
    if key not in integrations:
        return jsonify({"error": "Integration not found"}), 404
    ig = integrations[key]
    old = ig["status"]
    ig["status"] = "disconnected" if old == "connected" else "connected"
    event = log_event(ig["name"], "STATUS_CHANGE", {"from": old, "to": ig["status"]}, "info")
    return jsonify({"message": f"{ig['name']} is now {ig['status']}", "event": event})

@app.route("/webhook/receive", methods=["POST"])
def receive_webhook():
    data = request.json or {}
    event = log_event(
        data.get("source", "Unknown Service"),
        data.get("event", "WEBHOOK"),
        data.get("data", {}),
        "received"
    )
    return jsonify({"message": "Webhook received", "event_id": event["id"]}), 200

@app.route("/api/logs", methods=["GET"])
def get_logs():
    return jsonify({"logs": event_log, "count": len(event_log)})

@app.route("/api/send-payload", methods=["POST"])
def send_payload():
    body = request.json or {}
    event = log_event("Integration Hub", "OUTBOUND",
                      {"target": body.get("target", "external"), "data": body.get("data", {})}, "sent")
    return jsonify({"message": f"Payload sent to {body.get('target','external')}", "event": event})

@app.route("/api/stats", methods=["GET"])
def get_stats():
    connected = sum(1 for i in integrations.values() if i["status"] == "connected")
    return jsonify({
        "connected_integrations": connected,
        "total_integrations": len(integrations),
        "total_records_synced": sum(i["synced"] for i in integrations.values()),
        "total_events": len(event_log)
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
