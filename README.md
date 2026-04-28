# 🚀 API Integration Hub — Flask Dashboard

A full‑stack API simulation environment built with **Flask**, designed to demonstrate real‑world REST API behavior, webhook ingestion, event logging, and integration toggles across CRM, marketing, and database systems.

This project showcases backend engineering, API design, and UI‑driven interaction in a controlled testing environment.

---

## 🧩 Features

| Feature | Description |
|--------|-------------|
| **Integration Dashboard** | Manage simulated CRM, Marketing, Database, and Analytics integrations |
| **REST API Sync** | Trigger sync events using `POST /api/integrations/<key>/sync` |
| **Webhook Receiver** | Accept and log incoming webhook payloads at `POST /webhook/receive` |
| **Event Log** | Real‑time log of sync events, webhook calls, and integration state changes |
| **Stats Panel** | Live counts of connected integrations, sync events, and total logs |

---

## 🛠 Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML5, CSS3, Vanilla JavaScript  
- **APIs:** REST (GET/POST), Webhook ingestion  
- **Data:** In‑memory event log (extendable to SQLite or PostgreSQL)

---

## 📦 Setup

```bash
# 1. Clone the repo
git clone https://github.com/Bwalkzz31/api-integration-hub.git
cd api-integration-hub

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
