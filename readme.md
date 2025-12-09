# 🧪 AI Robustness & Fairness Test Suite

### Automated Testing Framework for Evaluating AI Text Classification Reliability

This project demonstrates how to design **automated robustness and fairness tests** for an AI text classification system.  
It includes a **local mock AI model**, **pytest test suite**, and **professional QA engineering structure** suitable for real-world AI/ML testing.

The goal is to validate that an AI classifier is:

- **Robust** → consistent predictions despite formatting noise  
- **Fair** → consistent predictions across demographic variations  
- **Reliable** → correctly handles malformed or missing inputs  

---

## ⭐ Key Features

- **Robustness Testing**  
  Ensures consistent predictions across:
  - Upper/lower case  
  - Extra spaces  
  - Punctuation  
  - Text permutations  

- ⚖️ **Fairness Testing**  
  Ensures same sentiment/label for:
  - Male vs Female terms  
  - Nationality swaps  
  - Similar structured sentences  

- **Negative Testing**
  - Missing payload  
  - Empty text  
  - Invalid types  

- **Local Flask-Based Mock AI Service**  
  Fully controlled & predictable behavior for safe testing.

- **Clean Pytest Setup**  
  Reusable, parametrized tests, modular utilities.

---

## 📁 Project Structure

```text
ai-robustness-fairness-tests/
├── mock_api/              # Local AI model simulation (Flask)
│   └── server.py
├── utils/                 # API client and helper utilities
│   └── api_client.py
├── tests/                 # Robustness, fairness, and negative tests
│   ├── test_robustness.py
│   ├── test_fairness.py
│   ├── test_negative_inputs.py
│   └── __init__.py
├── .env.example           # Environment variable template
├── requirements.txt
└── README.md

----

🧱 Architecture Overview


flowchart TD
    A["Pytest Test Suite"] --> B["API Client (requests)"]
    B --> C["Local Mock AI Server (Flask classifier)"]
    C --> D["Prediction + Confidence Response"]

    subgraph R["Robustness Tests"]
        R1["Case Variation"]
        R2["Punctuation Noise"]
        R3["Spacing Variations"]
    end

    subgraph F["Fairness Tests"]
        F1["Gender Swap"]
        F2["Nationality Swap"]
        F3["Neutrality Check"]
    end

    A --> R
    A --> F

This diagram visualizes how your pytest tests interact with the API client and the local mock AI server.



🚀 How to Run the Project

1️⃣ Activate Virtual Environment

cd ai-robustness-fairness-tests
source .venv/bin/activate

2️⃣ Start the Mock AI Server (Terminal 1)

python3 mock_api/server.py

3️⃣ Run Tests (Terminal 2)

cd ai-robustness-fairness-tests
source .venv/bin/activate
pytest -v

4️⃣ Run Specific Tests

pytest tests/test_robustness.py -v
pytest tests/test_fairness.py -v
pytest tests/test_negative_inputs.py -v


✔️ Test Coverage Summary

| Input Variant     | Expected   |
| ----------------- | ---------- |
| CASE variation    | Same label |
| Extra spaces      | Same label |
| Punctuation noise | Same label |


Fairness Tests

| Variant Pair                       | Expected         |
| ---------------------------------- | ---------------- |
| “He is…” vs “She is…”              | Equal prediction |
| “Indian people” vs “German people” | Equal prediction |
| “man” vs “woman”                   | Equal prediction |


Negative Tests

-Missing payload → 400

-Empty string → 400

-Invalid types → 400

----

🧠 Why This Project Is Useful for AI QA Roles

Modern AI systems must be:

Bias-resistant

Robust against noise

Consistent across demographic variations

This project demonstrates:

✔ Real-world ML testing scenarios
✔ Methodical robustness checks
✔ Practical fairness evaluation
✔ Clean automated testing architecture
