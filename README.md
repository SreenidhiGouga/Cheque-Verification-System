# Cheque-Verification-System
---
### 🚨 Problem  
Manual cheque verification is time-consuming, error-prone, and vulnerable to fraud. Traditional banking systems lack automated signature validation, leading to delayed processing and potential financial losses.

---

### 🌐 Solution  
This system automates the cheque verification process using computer vision and deep learning techniques. It verifies signature authenticity in real-time and improves security, speed, and accuracy across financial workflows by leveraging:

✅ Signature extraction from cheque images  
✅ OCR-based detail extraction  
✅ CNN-based signature verification  
✅ Real-time fraud detection and feedback  

---

### 🛠️ Tools & Technologies  

- **OpenCV**: For image preprocessing and signature isolation  
- **Tesseract OCR**: For extracting printed cheque details  
- **CNN (Keras/Scikit-learn)**: For signature forgery detection  
- **Flask**: For building the web-based application  
- **PostgreSQL**: For database storage and retrieval  
- **Python**: For integrating all components and logic  

---

### 📁 Project Structure

cheque-verification/
├── app/                  # Flask application code
│   ├── static/           # Frontend assets
│   ├── templates/        # HTML templates
│   ├── model/            # CNN model logic
│   └── routes.py         # App routes
├── database/             # PostgreSQL models and config
├── ocr/                  # OCR logic
├── utils/                # Helper functions
├── requirements.txt      # Python dependencies
└── run.py                # Entry point

---

### 💻 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SreenidhiGouga/ChequeVerification.git
   cd ChequeVerification


2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```



3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL** and update credentials in config files.

5. **Run the app**

   ```bash
   python run.py
   ```

---

### ▶️ Usage

1. Upload a scanned cheque image through the web interface.
2. The system extracts the signature and relevant details using OCR.
3. CNN model compares the signature against a reference dataset.
4. Output: **Verified** or **Forgery Detected**.

---

### 📌 Future Enhancements

* User authentication for secure access
* Multi-bank cheque format compatibility
* REST API for bank system integration
* Admin dashboard and analytics

---

### 👩‍💻 Author

**S G Sreenidhi**
📧 [sreenidhigouga@gmail.com](mailto:sreenidhigouga@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/sreenidhi-gouga)
🔗 [GitHub](https://github.com/SreenidhiGouga)

---

### 📄 License

This project is intended for academic and demonstration purposes. 





