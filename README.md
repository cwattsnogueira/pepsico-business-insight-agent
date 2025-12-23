# **PepsiCo Business Insight Agent**

AI‑powered strategic insights for enterprise decision‑making
Built for brand performance, consumer behavior, supply chain, and marketing strategy.


<p align="center">

  <img src="https://img.shields.io/badge/PepsiCo-Strategy%20AI-blue?style=for-the-badge&logo=pepsi&logoColor=white" />

  <!-- Languages & Frameworks -->
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Gradio-UI%20Framework-orange?style=for-the-badge&logo=gradio&logoColor=white" />

  <!-- AI & Cloud -->
  <img src="https://img.shields.io/badge/OpenAI-API-green?style=for-the-badge&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/AWS-EC2-orange?style=for-the-badge&logo=amazon-aws&logoColor=white" />

  <!-- Tools -->
  <img src="https://img.shields.io/badge/Virtualenv-Environment-yellow?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Dotenv-Config-lightgrey?style=for-the-badge&logo=dotenv&logoColor=white" />

  <!-- Project Status -->
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />

</p>

---

#  Overview

The **PepsiCo Business Insight Agent** is an AI‑powered strategic analysis tool designed to emulate the thinking style of a seasoned enterprise strategist.  
It interprets any business question and produces a clear, structured, executive‑ready analysis tailored to PepsiCo brands such as **Gatorade, Pepsi, Lay’s**, and more.

The application runs through a clean **Gradio UI**, making it accessible for analysts, managers, and executives.

---

#  Core Capabilities

The agent is built around a carefully engineered system prompt that ensures:

- Strategic, domain‑aware reasoning  
- Executive‑friendly communication  
- Action‑oriented recommendations  
- No reliance on real‑time data  
- Consistent structure across all responses  

Every answer follows a four‑part framework:

1. **Key Insight**  
2. **Business Impact**  
3. **Recommended Actions**  
4. **Risks & Considerations**

This ensures clarity, consistency, and immediate business relevance.

---

#  Project Structure

```
pepsico-agent/
│
├── app.py                 # Gradio UI for interacting with the agent
├── prompts.py             # System prompt definition
├── agent/
│   └── orchestrator.py    # Core agent logic + OpenAI API call
│
├── venv/                  # Python virtual environment (optional)
├── .env                   # Environment variables (API key)
└── README.md              # Project documentation
```

---

#  How It Works

### **1. System Prompt**
Defines the agent’s identity as a *Senior Business Insight Strategist* and enforces:

- Domain interpretation  
- Strategic reasoning  
- Structured output  
- PepsiCo‑specific logic  

### **2. Orchestrator**
Handles:

- Loading environment variables  
- Initializing the OpenAI client  
- Sending user queries + system prompt  
- Returning the model’s structured response  

### **3. Gradio App**
Provides a clean UI with:

- A dropdown of preset high‑impact business questions  
- A free‑text input box  
- A “Generate Insight” button  
- A response display area  

Runs on:

```
http://0.0.0.0:7860
```

---

#  Installation & Setup

### **1. Clone the repository**
```bash
git clone <your-repo-url>
cd pepsico-agent
```

### **2. Create and activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Install dependencies**
```bash
pip install -r requirements.txt
```

### **4. Add your OpenAI API key**
Create a `.env` file:

```
OPENAI_API_KEY=sk-PASTE-YOUR-KEY-HERE
```

### **5. Run the app**
```bash
python3 app.py
```

---

#  AWS EC2 Deployment Guide

This guide walks through deploying the Gradio app on an Amazon Linux 2023 EC2 instance.

---

## **1. Launch an EC2 Instance**

- Region: **eu‑west‑3 (Paris)**  
- AMI: **Amazon Linux 2023**  
- Instance type: **t2.micro**  
- Storage: **8–16 GB**  
- Security Group:
  - SSH (22) — your IP  
  - HTTP (80) — anywhere  
  - Custom TCP 7860 — anywhere  

---

## **2. Connect to the Instance**

```bash
ssh -i ~/.ssh/pepsico-agent-key.pem ec2-user@<YOUR-ELASTIC-IP>
```

---

## **3. Install System Dependencies**

```bash
sudo yum update -y
sudo yum install python3 python3-pip git -y
```

---

## **4. Clone Your Repository**

```bash
git clone https://github.com/<your-username>/pepsico-agent.git
cd pepsico-agent
```

---

## **5. Create and Activate a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## **6. Install Python Dependencies**

```bash
pip install -r requirements.txt
```

---

## **7. Add Your OpenAI API Key**

```bash
nano .env
```

Add:

```
OPENAI_API_KEY=sk-PASTE-YOUR-KEY-HERE
```

---

## **8. Run the Application**

```bash
python3 app.py
```

You should see:

```
Running on local URL: http://0.0.0.0:7860
```

---

## **9. Access the App in Your Browser**

```
http://<YOUR-ELASTIC-IP>:7860
```

---

## **10. (Optional) Keep the App Running with PM2**

```bash
npm install pm2 -g
pm2 start app.py --interpreter=python3
pm2 save
pm2 startup
```

---

#  Example Usage

**User Input:**  
> What marketing actions would most effectively increase Gatorade’s Gen Z engagement?

**Agent Output:**  
- Key Insight  
- Business Impact  
- Recommended Actions  
- Risks & Considerations  

---

#  Environment Variables

```
OPENAI_API_KEY
```

Loaded via `python-dotenv`.

---

#  Dependencies

- Python 3.10+  
- Gradio  
- OpenAI Python SDK  
- python-dotenv  

---

#  Future Enhancements

- Multi‑agent orchestration  
- RAG with PepsiCo documents  
- Role‑based personas  
- Logging + analytics dashboard  
- Authentication for enterprise deployment  

---

# 🏁 Summary

The PepsiCo Business Insight Agent delivers a polished, enterprise‑ready AI experience capable of producing strategic insights for leadership teams.  
It’s lightweight, deployable, and showcases strong prompt engineering, UI design, and cloud deployment skills.



