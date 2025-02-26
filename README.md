#FlowMate - Period Companion

## Project Overview

*FlowMate is an AI-powered chatbot designed to help women track their menstrual cycles, receive timely reminders, and get guidance on period-related concerns. It offers suggestions for pain relief, lifestyle tips, and general menstrual health information.*.


### *Features 🚀*
- 🩸 **Menstrual Cycle Tracking**: Users can log their last period date and cycle length.
- 🔔 **Period Reminders**: Automatically sends reminders when the next period is due.
- 💬 **AI Chatbot**: Provides responses to period-related queries using keyword-based matching.
- 💡 **Health & Wellness Tips**: Suggests remedies for cramps, bloating, mood swings, and more.
- 🔍 **Simple & User-Friendly Interface**: Built using Streamlit for an intuitive experience.

## Project Steps

### 1. Setup the Environment

- *Install Python 3.x*: Ensure Python 3.6 or higher is installed on your system.
  
- *Create a Virtual Environment* (optional):
    bash
    python -m venv venv
    
    Activate the virtual environment:
    - On Windows:
      bash
      .\venv\Scripts\activate
      
    - On macOS/Linux:
      bash
      source venv/bin/activate
      

- *Install Required Libraries*:
   ## Tech Stack 🛠️
- **Frontend**: Streamlit (Python-based UI)
- **Backend**: Flask (for API handling)
- **Database**: SQLite (for storing user data)
- **Scheduler**: `schedule` library for sending reminders
- **Language**: Python
    

### 2. Create the Main Application (app.py)

### 3. Run the Application

To run the Streamlit app, use the following command:
```bash
streamlit run app.py
