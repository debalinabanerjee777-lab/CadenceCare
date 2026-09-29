import streamlit as st
import time

st.set_page_config(page_title="CadenceCare", page_icon="❤️", layout="centered")

st.markdown("""
<style>
    .stButton>button { background-color: #ff4b6e; color: white; border-radius: 20px; width: 100%; font-weight: bold; height: 50px; }
    .action-box { background-color: #fff0f3; border-left: 5px solid #ff4b6e; padding: 15px; border-radius: 10px; margin-top: 10px; }
    .emergency { background-color: #ff0000; color: white; padding: 15px; border-radius: 10px; text-align: center; font-weight: bold; font-size: 18px; }
</style>
""", unsafe_allow_html=True)

# ----- PART 1: NAME SECTION (Tomar purono ta) -----
st.title("❤️ CadenceCare")
st.markdown("### Your Personal AI Health Companion 🩺")

name = st.text_input("Your Name? ✨", value="NAME")
if st.button("Welcome Me"):
    st.balloons()
    st.success(f"Hello {name}, Welcome to CadenceCare! ❤️")

st.markdown("---")

# ----- PART 2: AI DOCTOR WITH IMMEDIATE ACTION -----
def get_immediate_action(question):
    q = question.lower()
    
    if "stroke" in q:
        return {"type": "EMERGENCY", "title": "🚨 STROKE - Call Emergency NOW!", "action": ["1. CALL 102 / 108 Ambulance IMMEDIATELY", "2. Note the time when symptoms started", "3. DO NOT give food, water or medicine", "4. Lay patient flat, head slightly elevated", "5. FAST Check: Face droop, Arm weakness, Speech difficulty"], "note": "Medical Emergency! Go to ER immediately."}
    elif "chest" in q or "heart" in q:
        return {"type": "EMERGENCY", "title": "🚨 CHEST PAIN - Possible Heart Attack!", "action": ["1. CALL 102 / 108 Immediately, sit and rest", "2. Chew 1 Aspirin if not allergic (if doctor advised before)", "3. Loosen tight clothes, stay calm", "4. DO NOT drive yourself"], "note": "Every minute matters. Don't delay."}
    elif "bleeding" in q or "cut" in q:
        return {"type": "FIRST AID", "title": "🩹 Bleeding / Cut", "action": ["1. Apply firm pressure with clean cloth for 10 mins", "2. Elevate injured part", "3. Wash with clean water after bleeding stops", "4. Apply bandage"], "note": "If bleeding doesn't stop in 15 mins, go to ER."}
    elif "fever" in q or "jor" in q:
        return {"type": "CARE", "title": "🤒 Fever", "action": ["1. Rest and drink lots of water / ORS", "2. Check temp every 2 hours", "3. Cold sponge on forehead", "4. Wear light clothes"], "note": "If >102°F for 2 days, see doctor."}
    elif "head" in q:
        return {"type": "CARE", "title": "🤕 Headache", "action": ["1. Rest in dark room 30 mins", "2. Drink 2 glasses water", "3. Avoid phone screen", "4. Gentle neck massage"], "note": "If severe with vomiting, seek help."}
    else:
        return {"type": "CARE", "title": f"🩺 For: '{question}'", "action": [f"1. Immediate: Stay calm for '{question}'", "2. Hydrate, rest, note symptoms", "3. Avoid self-medication", "4. Keep emergency contact ready"], "note": "General info only. Consult family doctor for personal advice."}

st.subheader("👨‍⚕️ Ask AI Doctor")
user_q = st.text_input("How are you feeling today?", placeholder="Ex: what can i do in stroke")

if st.button("Ask Doctor 🩺"):
    if user_q:
        with st.spinner("Doctor is thinking..."):
            time.sleep(1)
        result = get_immediate_action(user_q)
        
        if result["type"] == "EMERGENCY":
            st.markdown(f"<div class='emergency'>{result['title']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"### {result['title']}")
        
        st.markdown(f"<div class='action-box'><b>IMMEDIATE ACTION:</b><br>{'<br>'.join(result['action'])}</div>", unsafe_allow_html=True)
        st.warning(f"⚠️ {result['note']}")
    else:
        st.error("Please type your question!")

st.caption("Disclaimer: For educational purpose only. Not a replacement for professional medical advice.")