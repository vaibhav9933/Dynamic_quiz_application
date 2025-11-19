# 🧠 Dynamic Quiz Application with Timer, Difficulty Levels & Result Analysis

A fully interactive **Dynamic Quiz Application** built using **HTML, CSS, JavaScript**, featuring:

- Category selection  
- Difficulty levels  
- Countdown timer for each question  
- Automatic next question on timeout  
- Detailed result analysis  
- Fully automated testing using **Selenium (Python)**  
- Responsive UI  
- Live deployed version on Vercel  

---

## 🚀 Live Demo (Hosted on Vercel)

🔗 **https://dynamic-quiz-application-iota.vercel.app/**

---

## 🎥 Demo Video (Screen Recording)

🔗 **Loom Video:**  
https://www.loom.com/share/4e6e68a9109e48f0a1c2f6e7e3efce7b

### 📁 Backup Demo (Google Drive)
https://drive.google.com/file/d/112i6tRZeMh_53Sl23oW1dy2he2UoHpb7/view?usp=sharing

---

## 📂 Project Structure

Dynamic_quiz_application/
│
├── index.html
├── style.css
├── script.js
│
├── run_quiz.py # Selenium automation script
│
├── artifacts/
│ ├── screenshots/ # All auto-generated screenshots
│ └── logs/
│
└── README.md


---

## 📌 Features

### ✔ **Category Selection**
Choose from multiple quiz categories (GK, CS, etc.)

### ✔ **Difficulty Selection**
- Easy  
- Medium  
- Hard  

### ✔ **Dynamic Question Loading**
Questions load based on category & difficulty.

### ✔ **Timer for Each Question**
- 10 seconds per question  
- Auto-marks wrong if time runs out  
- Automatically loads next question  

### ✔ **Result Analysis**
Shows:
- Total Score  
- Correct Answers  
- Wrong Answers  

### ✔ **Responsive UI**
Clean and simple layout for desktop and mobile.

### ✔ **Selenium-Based Automated Testing**
- Opens quiz automatically  
- Takes screenshots  
- Selects options  
- Navigates through quiz  
- Saves artifacts to `/artifacts/`

---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|----------|
| **HTML** | Structure |
| **CSS** | Styling |
| **JavaScript** | Quiz logic + timer |
| **Python** | Testing automation |
| **Selenium** | Browser automation |
| **ChromeDriver** | WebDriver execution |
| **Vercel** | Deployment |

---

## 🧪 Selenium Automation Script

The project includes a complete automated script:

### **run_quiz.py**
```python
# (Script already included in your repository)
# Opens quiz, clicks options, captures screenshots, and saves artifacts.

📸 Automation Outputs

Found inside:

artifacts/screenshots/


Auto-generated screenshots include:

Landing page

First question

After answering each question

Final result page

🧩 How to Run Project Locally
1️⃣ Clone the repository
git clone https://github.com/vaibhav9933/Dynamic_quiz_application

2️⃣ Open index.html

Just double-click:

index.html


No server required.

🧪 How to Run Selenium Automated Tests
1️⃣ Install dependencies
pip install selenium

2️⃣ Ensure ChromeDriver is installed

Download from:
https://chromedriver.chromium.org/

3️⃣ Run automation
python run_quiz.py


Results are saved in:

artifacts/screenshots/

🌐 Deployment (Vercel)

This project is deployed using Vercel for fast static hosting.

Live link:
👉 https://dynamic-quiz-application-iota.vercel.app/
