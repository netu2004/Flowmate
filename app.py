import streamlit as st
import sqlite3
import schedule
import time
from datetime import datetime, timedelta



# Database setup
conn = sqlite3.connect('period_tracker.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        last_period TEXT,
        cycle_length INTEGER
    )
''')
conn.commit()

# Streamlit UI
st.title("FlowMate - Period Companion ")

st.write("""FlowMate is designed to help women track their menstrual cycles, get timely reminders,
and receive AI-powered guidance on period-related concerns. It provides suggestions for pain relief, 
lifestyle tips, and general menstrual health information by just using the key words like cramps,
late period,exercise,stomach pain,mood swings,heavy bleeding,irregular periods,bloating,headache""")

# User Input for Tracking
st.header("Track Your Period")
name = st.text_input("Enter Your Name")
email = st.text_input("Enter Your Email")
last_period = st.date_input("Last Period Date")
cycle_length = st.number_input("Cycle Length (days)", min_value=20, max_value=40, value=28)

if st.button("Save My Data"):
    cursor.execute("INSERT INTO users (name, email, last_period, cycle_length) VALUES (?, ?, ?, ?)", 
                   (name, email, last_period, cycle_length))
    conn.commit()
    st.success("Your data has been saved!")

# Chatbot Feature (Enhanced Responses)
st.header("Ask FlowMate Anything About Periods!")
user_question = st.text_input("Ask me anything about periods...")

if st.button("Ask"):
    responses = {
        "cramps": "Cramps can be relieved by using a heating pad, drinking warm fluids, and light stretching.",
        "late period": "Periods can be delayed due to stress, diet changes, or hormonal imbalances. Consider tracking your cycle regularly.",
        "exercise": "Light exercises like yoga, walking, and stretching can help relieve period pain.",
        "stomach pain": "A heating pad, herbal tea, and rest can help with stomach pain during periods.",
        "mood swings": "Hormonal changes can cause mood swings. Try relaxation techniques like meditation or listening to soothing music.",
        "heavy bleeding": "If your period is unusually heavy, consider consulting a doctor. Hydration and iron-rich foods can help.",
        "irregular periods": "Irregular cycles can be due to stress, diet, PCOS, or hormonal imbalances. Consider maintaining a healthy lifestyle.",
        "bloating": "Drinking water and reducing salty foods can help with period bloating.",
        "headache": "Period headaches can be relieved with hydration, rest, and avoiding caffeine or processed foods."
    }
    
    # Basic keyword-based chatbot response
    response = None
    for key in responses:
        if key in user_question.lower():
            response = responses[key]
            break
    
    if response:
        st.write(response)
    else:
        st.write("I'm still learning! Try using keywords like 'cramps', 'late period', or 'exercise'. Stay healthy ❤️")

# Function to send reminders (Mock)
def send_reminder():
    users = cursor.execute("SELECT email, last_period, cycle_length FROM users").fetchall()
    for user in users:
        email, last_period, cycle_length = user
        next_period = datetime.strptime(last_period, "%Y-%m-%d") + timedelta(days=cycle_length)
        if datetime.today().date() == next_period.date():
            print(f"Reminder: Your period is due soon, {email}! Stay prepared.")

# Schedule the reminder to run daily
schedule.every().day.at("09:00").do(send_reminder)

# Background job to check reminders once a day
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(86400)  # Sleep for a day

# Run the scheduler in the background
import threading
thread = threading.Thread(target=run_scheduler, daemon=True)
thread.start()
