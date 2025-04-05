# Sentiment Analysis Project

## Overview
This project is a Sentiment Analysis web application that analyzes text input and determines whether the sentiment is **Positive, Negative, or Neutral**. The backend is built using **Flask** and **TextBlob**, while the frontend is developed with **React.js**, **Vite**, and **Tailwind CSS**.

## Tech Stack
- Frontend: React.js, Vite, Tailwind CSS
- Backend: Flask, TextBlob
- API Communication: Fetch API
- Deployment: Local development using Flask

## Features
- Users can input text and analyze its sentiment.
- The backend processes text and returns a sentiment score.
- Simple and intuitive UI built with Tailwind CSS.
- CORS-enabled backend to allow frontend communication.

## Installation & Setup

### Backend (Flask API)
1. **Clone the repository**
   ```sh
   git clone <your-repo-url>
   cd sentiment-analysis
   ```
2. **Create a virtual environment** (Optional but recommended)
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Flask server**
   ```sh
   python app.py
   ```
   The server will start on `http://127.0.0.1:5000`

### Frontend (React + Vite)
1. **Navigate to the frontend folder**
   ```sh
   cd frontend
   ```
2. **Install dependencies**
   ```sh
   npm install
   ```
3. **Run the frontend**
   ```sh
   npm run dev
   ```
   The application will be available at `http://localhost:5173`

## API Endpoint
- **POST `/analyze`**
  - **Request Body:** `{ "text": "Your text here" }`
  - **Response:** `{ "sentiment": "Positive", "score": 0.5 }`

## Contributing
Feel free to submit issues and pull requests if you want to contribute!

## License
This project is open-source and available under the MIT License.

