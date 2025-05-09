## 🚀 API Testing Tool

A dynamic REST API testing tool built with a **shared frontend-backend architecture** to demonstrate real-world API integration, proxy-based request handling, and dynamic user input processing.

---

### 📌 Purpose

This project was built to showcase:

* 🔄 **Shared system architecture**: decoupled frontend and backend structure.
* 🔧 **Dynamic API handling**: sending user-defined REST API requests through a proxy.
* ⚙️ **Data flow control**: capturing, transmitting, and processing data across the stack.
* 📬 **Endpoint & method management**: supporting GET, POST, PUT, DELETE, etc., with headers, params, and body data.

---

### 🛠 Tech Stack

| Layer    | Technology                                      |
| -------- | ----------------------------------------------- |
| Frontend | HTML, JavaScript, Axios                         |
| Backend  | Flask (Python)                                  |
| Hosting  | GitHub Pages (Frontend), Flask Server (Backend) |

---

### 🧠 Key Features

* 📤 **User-submitted form** to input:

  * API method (GET, POST, etc.)
  * Target URL
  * Headers
  * Query parameters
  * Body data

* 📡 **Frontend-to-backend communication** via `axios` to transmit input data to the Flask server.

* 🔀 **Flask as a proxy server** that:

  * Constructs and sends the request to the external API.
  * Receives and parses the response.
  * Returns response data to the frontend.

* 📊 **Dynamic response rendering** in HTML:

  * Status code
  * Response headers
  * JSON or raw response body

---

### 🧱 Architectural Highlights

* 🔗 **Loosely coupled system**:

  * Frontend and backend are completely dislocated and deployable independently.
  * Enables horizontal scaling and separation of concerns.

* 🛡️ **Proxy architecture**:

  * Enables secure, controlled API testing by shielding frontend from CORS and key exposure.

* 🧰 **Built with job-readiness in mind**:

  * Demonstrates real skills in endpoint management, error handling, and full request lifecycle handling.

---

### 📁 Folder Structure

```
├── frontend/
│   └── index.html
│   └── main.js
├── backend/
│   └── app.py
│   └── requirements.txt
```

---

### ⚡ Getting Started

#### Frontend (GitHub Pages / Local)

```bash
Open frontend/index.html in any browser
```

#### Backend (Flask Server)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

---

### 🎯 Why I Built This

As an entry-level web developer aiming to showcase **real-world, job-ready skills**, I built this tool to:

* Demonstrate architectural thinking (decoupled, distributed systems)
* Solve practical problems (CORS handling, API testing)
* Exhibit dynamic data processing and API integration logic
* Show I can build not just code — but complete, scalable systems

---

### 📸 Screenshots (Optional)

![screencapture-abdullahstackhub-github-io-apitesterfrontend-2025-05-08-23_14_56](https://github.com/user-attachments/assets/789fc4c2-fdb1-4b28-85c7-0c1459379957)


---

### 📂 Future Improvements

* Replace Flask with **FastAPI** or **Express.js** for performance gains
* Add history tab (localStorage-based)
* Allow saving & reusing API configurations
* Add request duration timer and better error visual feedback

---

### 📬 Contact

**Developer**: Abdullah 

**Professional Linkedin**:([Abdullah Hussain](https://www.linkedin.com/in/abdullah-hussain-194796357/))
