# 🚀 Lightweight API Testing Tool

![Flask](https://img.shields.io/badge/Backend-Flask-blue)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2C%20CSS%2C%20JS-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

> A lightweight, web-based API testing tool to test **REST APIs** — supports **GET**, **POST**, **PUT**, **OPTIONS**, and **DELETE** methods.  
> Designed to be fast, simple, and powerful.  
> _Think of it as Postman, but minimal and web-native._

---

## ✨ Features

- ✅ Test **GET**, **POST**, **PUT**, **OPTIONS**, **DELETE** requests
- ✅ Send **Headers**, **Query Params**, **Body** (JSON, Form-Data)
- ✅ View **Status Code**, **Response Time**, **Response Size**
- ✅ Built with **Flask (Python)** and **Vanilla JS** + **Bootstrap**
- ✅ **Frontend and Backend are Independent**
- ✅ Simple architecture — easy to understand and extend

---

## 🛠 Tech Stack

| Area | Technologies |
|:----:|:-------------|
| Backend | Flask (Python) |
| Frontend | HTML, CSS, Bootstrap, JavaScript (Axios) |

---

## 🧐 How It Works

1. **Frontend** collects the API request details (URL, headers, parameters, body, method).
2. Sends the data to **Flask backend** using **Axios**.
3. Flask has dedicated endpoints (`/send_get`, `/send_post`, etc.) for each method.
4. Flask makes the actual API request based on user's input.
5. Flask sends back:
   - Response headers
   - Response body
   - Status code
   - Response time (ms)
   - Response size
6. **Frontend** dynamically shows the response to the user.

---

## 🏩 Project Structure

```
📁 project-root/
 ├── 📄 app.py            # Flask backend
 ├── 📄 requirements.txt  # Python dependencies
 ├── 📁 static/            # Static files (CSS, JS)
 ├── 📁 templates/         # HTML templates
 └── 📄 README.md          # (You are here)
```

---

## 🚀 Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Flask server:**
   ```bash
   python app.py
   ```

4. **Start the Frontend:**
   - Open the `index.html` using **Live Server** (VS Code Extension).

---

## 🧪 Usage

- Enter your **API URL**.
- Select the **HTTP method**.
- Add **headers**, **params**, and **body** (if needed).
- Hit **Send**.
- View the **response** in a beautiful, clean format — including:
  - Status Code
  - Headers
  - Body
  - Response Time
  - Size

---

## 🎯 Purpose of This Project

- **Demonstrate** skills in API management and data handling.
- Showcase **separation of frontend/backend** architecture.
- **Real-world project** for handling APIs, form-data, JSON, etc.
- Built **from scratch** with **Flask** and **Vanilla JS** without heavy frameworks.

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and share it!

---

## 🙏 Credits

- **Built with ❤️ by Abdullah Hussain**
- Tools used: Flask, Vanilla JavaScript, Bootstrap

---

