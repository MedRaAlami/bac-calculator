# 🎓 Moroccan Baccalaureate Grade Calculator (CLI)

## 📌 Overview

A Python command-line tool that simulates the **Moroccan Baccalaureate (Bac)** final average.

It calculates:

* 📘 Regional exam (1BAC)
* 📗 National exam (2BAC)
* 📊 Continuous assessment (CC)

Then determines:

* 🎯 Final average (**Moyenne Générale**)
* 🏅 Result classification (Pass, Merit, Distinction, etc.)

---

## 🎯 Purpose

* Help Moroccan students estimate their Bac results
* Provide a clear simulation of the grading system
* Practice Python using real-world logic

---

## ⚙️ Features

* Supports all major streams:

  * Sciences (Math, Experimental, Technology)
  * Economics & Management
* Weighted subject calculations
* Input validation (no crashes)
* Detects 0 in national exams (→ remedial)
* Clean and user-friendly CLI experience

---

## 🧮 Formula

Moyenne Générale = ((2 × National) + Regional + CC) / 4

---

## 🧠 Result Classification

| Average  | Result           |
| -------- | ---------------- |
| ≥ 16     | High Distinction |
| 14 – <16 | Distinction      |
| 12 – <14 | Merit            |
| 10 – <12 | Pass             |
| 7 – <10  | Remedial         |
| < 7      | Repeat           |

⚠️ Any 0 in national exams → automatic remedial

---

## 🚀 How to Run

```bash
python bac_calculator.py
```

---

## 📦 Requirements

* Python 3.x
* No external libraries required

---

## 🧪 Example

```text
Enter your first name: Mohamed
Enter your last name: El Alami
...
Your overall baccalaureate average is: 14.32
Distinction
```

---

## 🔧 Future Improvements

* GUI version (Tkinter / Web)
* Export results to file
* Multilingual support (FR / AR / EN)

---

## 👨‍💻 Author

Mohamed Rayan El Alami
Casablanca, Morocco
