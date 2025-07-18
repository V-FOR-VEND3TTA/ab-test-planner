# 📄 Project Overview: A/B Test Planner

## 🎯 Purpose

The **A/B Test Planner** is a lightweight web tool that helps marketers and product teams plan structured A/B tests. It allows users to define experiments, create test variants, set success metrics (KPIs), and track baseline vs. goal outcomes—all before implementation.

Designed for teams focused on **data-driven customer acquisition and retention**, this tool improves clarity, consistency, and collaboration in test design.

---

## 🛠️ Tech Stack

* **Backend**: Django (Python)
* **Frontend**: Bootstrap 4
* **Forms & Validation**: Django Forms
* **Templating**: Django Templates
* **Database**: SQLite (default, can be switched)

---

## 🧩 Key Features

* Create and manage A/B tests
* Define:

  * Test name and description
  * Start and end dates
  * Test variants (e.g., "Version A", "Version B")
  * Outcome metrics (e.g., click-through rate, conversion rate)
  * Baseline values and goal targets
* View a detailed summary of each test
* Minimal, focused UI built for quick planning

---

## 📂 Folder Structure

```bash
ab_test_planner/
├── manage.py
├── tests/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   │   └── tests/
│   │       ├── home.html
│   │       ├── create_test.html
│   │       └── view_test.html
│   └── ...
├── ab_test_planner/
│   ├── settings.py
│   ├── urls.py
│   └── ...
```

---

## 🚀 Getting Started

1. **Clone the repo**

   ```bash
   git clone https://github.com/yourusername/ab-test-planner.git
   cd ab-test-planner
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations & run the server**

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

4. **Access the tool**
   Open `http://127.0.0.1:8000/` in your browser.

---

## 📄 Example Use Case

> A growth marketer wants to test two email subject lines. She uses the A/B Test Planner to define "Subject A" and "Subject B", set the conversion metric as "Open Rate", input the current baseline (22%) and desired goal (30%), and set the test to run for 2 weeks. The team uses the plan to align execution and measurement.

---

## 📌 Future Improvements

* PDF export of test plan
* User authentication for saving test history
* Dashboard with test status tracking
* Integration with analytics APIs (e.g., GA4, Mixpanel)
* Tagging and categorization of tests

---

## 👥 Ideal Users

* Performance Marketers
* CRO Specialists
* Growth Teams
* Founders & Startups
* UX Researchers

---

## 🧠 Why This Matters

Many teams run A/B tests without a proper planning structure, leading to vague outcomes and inconclusive data. This tool provides a **clear, repeatable framework** to increase the success rate and business impact of A/B testing.
