# Agora Assignment

Automation project for demoqa.com form using Selenium, Pytest, and Page Object Model.

## 🧪 How to Run the Tests

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/agora_project.git
cd agora_project
```

### 2. Initialize virtual env
```bash
python -m venv venv
venv\Scripts\activate  # for Windows
pip install -r requirements.txt
```

### 3. Run the tests
```
pytest tests/test_form.py -v
```

### 4. You have an option to configure on which browser to run
##### 🌐 Browser Configuration
Currently the tests are configured to run on Chrome as defaul, but can be easily extended with additional browser handlers.
 you can add command-line browser selection to your project and run tests on a different browser (like Firefox) via:
 
```
pytest --browser=firefox
```
