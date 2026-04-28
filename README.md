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


# 🔄 Salesforce ↔ HubSpot Sync Portfolio  
A professional API integration case study demonstrating a full bidirectional CRM sync pipeline between **Salesforce** and **HubSpot**.  
This project highlights real‑world API architecture, JSON transformation, webhook security, conflict resolution, and AI‑assisted evaluation.

Built to showcase system design, API reasoning, and integration troubleshooting at a professional level.

---

## 🧩 Overview  
Modern organizations rely on multiple CRMs, marketing tools, and automation platforms.  
This project simulates a **real integration pipeline** that keeps Salesforce and HubSpot data synchronized using:

- REST APIs  
- Webhooks  
- JSON mapping  
- Conflict resolution logic  
- Rate‑limited batch processing  
- Error handling + retry logic  
- AI evaluation (RLHF) for API reasoning  

This is not a “toy” example — it models the same challenges faced in real enterprise integrations.

---

## 🏗 Architecture Summary  

### **1. Inbound Webhooks (HubSpot → Salesforce)**  
- HubSpot sends contact updates via webhook  
- Payload is validated with a shared secret  
- JSON is transformed into Salesforce‑compatible fields  
- Conflicts are resolved using timestamp priority  
- Records are queued for Salesforce API update  

### **2. Outbound Sync (Salesforce → HubSpot)**  
- Salesforce changes are pulled via REST API  
- Data is normalized and mapped to HubSpot schema  
- Rate limits are respected using exponential backoff  
- Failed updates are logged and retried  

### **3. Bidirectional Merge Logic**  
- Detects which system has the “source of truth”  
- Prevents overwrite loops  
- Handles partial updates  
- Supports field‑level conflict resolution  

---

## 🛠 Tech Stack  
- **APIs:** Salesforce REST API, HubSpot CRM API  
- **Data:** JSON, Webhooks, Batch Sync  
- **Security:** HMAC signatures, API keys, OAuth (conceptual)  
- **Evaluation:** RLHF rubric for API reasoning  
- **Documentation:** Markdown, Architecture Diagrams  

---

## 📥 Example Webhook Payload (HubSpot → Salesforce)

```json
{
  "objectId": "104201",
  "eventType": "contact.propertyChange",
  "properties": {
    "firstname": "Alicia",
    "lastname": "Reed",
    "email": "alicia.reed@example.com",
    "lifecyclestage": "customer"
  },
  "timestamp": 1714501200000
}

