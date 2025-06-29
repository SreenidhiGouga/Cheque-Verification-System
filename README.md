# 🧾 Cheque Verification System

### 🚨 Problem  
Manual cheque verification is time-consuming, error-prone, and vulnerable to fraud. Traditional banking systems lack automated signature validation, leading to delayed processing and potential financial losses.

---

### 🌐 Solution  
This system automates the cheque verification process using computer vision and deep learning techniques. It verifies signature authenticity in real-time and improves security, speed, and accuracy across financial workflows by leveraging:

- ✅ Signature extraction from cheque images  
- ✅ OCR-based detail extraction  
- ✅ CNN-based signature verification  
- ✅ Real-time fraud detection and feedback  

---

### 🛠️ Tools & Technologies  

- **Python** – Core development language  
- **Flask** – Backend web framework  
- **PostgreSQL** – Database for storing verification records  
- **OpenCV** – Image preprocessing and signature isolation  
- **Tesseract OCR** – Text extraction from cheque  
- **CNN (Keras / Scikit-learn)** – Signature forgery detection  

---

### 📁 Project Structure

```

cheque-verification/
├── app/                   # Flask application code
│   ├── static/            # Frontend assets (CSS, JS, images)
│   ├── templates/         # HTML templates
│   ├── model/             # CNN model logic
│   └── routes.py          # Flask routes and logic
├── database/              # PostgreSQL setup and schema
├── ocr/                   # OCR modules and helpers
├── utils/                 # Utility functions
├── requirements.txt       # Python dependencies
└── run.py                 # Main application entry point

````

---

### 💻 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SreenidhiGouga/ChequeVerification.git
   cd ChequeVerification
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure PostgreSQL**
   Set up your PostgreSQL database and update connection details in the config file.

5. **Run the application**

   ```bash
   python run.py
   ```

---

### ▶️ Usage

* Upload a scanned cheque image through the web interface.
* The system extracts printed text and signature using OCR and image processing.
* CNN model analyzes the signature against a reference.
* Displays output as **Verified** or **Forgery Detected**.

---

### 📌 Future Enhancements

* User authentication for secure access
* Multi-bank cheque format compatibility
* REST API for integration with external banking systems
* Admin dashboard with real-time analytics

---

### 👩‍💻 Author

**S G Sreenidhi**
📧 [sreenidhigouga@gmail.com](mailto:sreenidhigouga@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/sreenidhi-gouga)
🔗 [GitHub](https://github.com/SreenidhiGouga)

---
