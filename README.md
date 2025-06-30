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
cheque_verification/
├── app/                        # Main Flask application logic
├── data/                       # Dataset or sample cheque images
├── env/                        # Python virtual environment (optional to track)
├── static/                     # CSS, JS, and other static assets
├── templates/                  # HTML frontend templates
├── cheque_verification_model.h5  # Trained CNN model file
├── preprocess.py               # Script for image preprocessing
├── train_model.py              # Model training script
├── requirements.txt            # Python dependencies
└── app.py                      # Entry point for running the app
````
---

### 📦 Model File

Download the pretrained CNN model used for signature verification:  
🔗 [cheque_verification_model.h5 (Google Drive)](https://drive.google.com/file/d/1yP6ypb8tbEVWI2tfQ14X2tw8PT-9-cW_/view?usp=sharing)

Place the downloaded file in the `app/model/` directory before running the application.

---

### 📂 Data Files

Download the sample cheque image dataset used for training and testing:  
🔗 [data/ folder (Google Drive)](https://drive.google.com/drive/folders/19OTerwqbhTtSCjUZNm3gU106m3oqZ5vx?usp=sharing)

After downloading, place the folder in the project root directory as shown in the structure above.

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
