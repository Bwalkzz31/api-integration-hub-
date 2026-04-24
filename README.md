# ⚡ API Integration Hub

A Flask-based dashboard that simulates real-world **API integrations** and **webhook management** across multiple business platforms (CRM, Marketing, Database, Analytics).

Built to demonstrate skills in: REST API design, webhook handling, data synchronization, and full-stack Python development.

---

## 🚀 Features

| Feature | Description |
|---|---|
| 🔌 Integration Dashboard | View and manage connections to CRM, Marketing, DB, and Analytics systems |
| 🔄 REST API Sync | Trigger data sync between platforms via `POST /api/integrations/<key>/sync` |
| 🪝 Webhook Receiver | Accept and log incoming webhook payloads at `POST /webhook/receive` |
| 📋 Event Log | Real-time log of all sync events, webhook calls, and status changes |
| 📊 Stats Panel | Live counts of connected integrations, records synced, and total events |

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** Vanilla JS, HTML5, CSS3
- **APIs:** REST (GET/POST), Webhook ingestion
- **Data:** In-memory event log (extendable to SQLite)

---

## 📦 Setup

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/api-integration-hub.git
cd api-integration-hub

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 🔗 API Endpoints

| Method | Route | Description |
|---|---|---|
| GET | `/api/integrations` | List all integrations and their status |
| POST | `/api/integrations/<key>/sync` | Sync records from a specific integration |
| POST | `/api/integrations/<key>/toggle` | Connect or disconnect an integration |
| POST | `/webhook/receive` | Receive an inbound webhook payload |
| POST | `/api/send-payload` | Simulate sending data to an external service |
| GET | `/api/logs` | Retrieve the full event log |
| GET | `/api/stats` | Get dashboard summary stats |

---

## 🧪 Example Webhook Payload

```json
POST /webhook/receive
{
  "source": "Salesforce CRM",
  "event": "contact.created",
  "data": {
    "contact_id": "C-001",
    "name": "Jane Doe",
    "email": "jane@example.com"
  }
}
```

---

## 📁 Project Structure

```
api-integration-hub/
├── app.py              # Flask app + all routes
├── requirements.txt    # Python dependencies
├── templates/
│   └── dashboard.html  # Frontend dashboard
└── README.md
```

---

## 👩‍💻 Author

**Britany Walker** — AI Trainer & IT Management Professional  
[GitHub](https://github.com/Bwalkzz31) · [Portfolio](https://bwalkzz31.github.io)
