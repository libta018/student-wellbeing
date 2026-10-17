
import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

st.set_page_config(page_title="Student Wellbeing", page_icon="🌙", layout="wide")
model = joblib.load("Mental_Health_Model.pkl")

st.markdown("""
<style>
.stApp {background:#0b0b1c;color:#f4f1ff}
.block-container {max-width:1050px;padding:1rem}
h1 {font-size:1.9rem!important}
div[data-testid="stForm"] {
    background:#171831;border:1px solid #343454;
    border-radius:16px;padding:12px
}
div[data-testid="stFormSubmitButton"] button {
    background:#ad8aff;color:#100d25;border:0;
    border-radius:10px;font-weight:700;min-height:40px
}
</style>
""", unsafe_allow_html=True)

st.caption("✦ STUDENT WELLBEING LAB")
st.title("How's your digital rhythm treating you?")
st.write("Explore how your daily habits relate to your wellbeing score.")

left, right = st.columns([1.3, 0.9], gap="medium")

with left:
    with st.form("habits"):
        st.subheader("👤 About you")
        a,b = st.columns(2)
        age = a.number_input("Age",1,100,21)
        gender = b.selectbox("Gender",["Male","Female","Other"])
        country = st.text_input("Country","India")
        level = st.selectbox("Academic level",
            ["Undergraduate","Postgraduate","High School"])

        st.subheader("🌿 Daily rhythm")
        a,b = st.columns(2)
        sleep = a.slider("Sleep (hours/night)",0.,24.,7.)
        study = b.slider("Study (hours/day)",0.,24.,4.)
        activity = st.slider("Physical activity (hours/day)",0.,24.,2.)
        stress = st.select_slider("Stress level",
            ["Low","Medium","High","Very High"],value="Medium")

        st.subheader("📱 Digital habits")
        usage = st.slider("Social media (hours/day)",0.,24.,4.)
        unlocks = st.number_input("Phone unlocks/day",0,10000,100)
        platform = st.selectbox("Main platform",
            ["Instagram","TikTok","Facebook","YouTube","Other"])
        purpose = st.selectbox("Main purpose",
            ["Entertainment","Education","Socialization","Other"])
        submit = st.form_submit_button("✨ Predict my score",use_container_width=True)

with right:
    st.subheader("Your wellbeing snapshot")

    if submit:
        try:
            data = pd.DataFrame([{
                "Age":age,
                "Avg_Daily_Usage_Hours":usage,
                "Daily_Unlocks":unlocks,
                "Study_Hours":study,
                "Physical_Activity_Hours":activity,
                "Sleep_Hours_Per_Night":sleep,
                "Stress_Level":stress,
                "Gender":gender,
                "Academic_Level":level,
                "Most_Used_Platform":platform,
                "Purpose_Of_Use":purpose,
                "Grouped_country":country
            }])

            score = float(model.predict(data)[0])
            score = max(0,min(10,score))

            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=score,
                number={"suffix":" / 10","valueformat":".2f",
                        "font":{"size":28,"color":"#eee7ff"}},
                gauge={
                    "shape":"angular",
                    "axis":{"range":[0,10],"tickvals":[0,5,10],
                            "tickfont":{"color":"#eee7ff","size":10}},
                    "bar":{"color":"#ad8aff","thickness":0.22},
                    "bgcolor":"#171831","borderwidth":0,
                    "steps":[
                        {"range":[0,4],"color":"#39233f"},
                        {"range":[4,7],"color":"#29264c"},
                        {"range":[7,10],"color":"#24453f"}
                    ]
                }
            ))

            fig.update_layout(
                height=230,paper_bgcolor="#171831",
                font_color="#eee7ff",
                margin=dict(t=15,b=0,l=5,r=5)
            )
            st.plotly_chart(fig,use_container_width=True,
                            config={"displayModeBar":False})
            st.caption("Model estimate only — not a clinical mental health assessment.")

        except Exception as e:
            st.error(f"Prediction error: {e}")
    else:
        st.info("Fill in your habits and click Predict my score.")


